from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import time
import warnings
from typing import Any

warnings.filterwarnings("ignore")

# =========================
# CONFIG
# =========================
model_name = "<your-model-folder-name>"

device = "cuda" if torch.cuda.is_available() else "cpu"

# Enable TF32 for RTX cards
torch.backends.cuda.matmul.allow_tf32 = True
torch.backends.cudnn.allow_tf32 = True

# =========================
# LOAD TOKENIZER
# =========================
tokenizer = AutoTokenizer.from_pretrained(
    model_name,
    use_fast=True
)

if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# =========================
# LOAD MODEL
# =========================
model: Any = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto",
    low_cpu_mem_usage=True,
)

# Optional compile for PyTorch 2+
if hasattr(torch, "compile"):
    model = torch.compile(model)

model.eval()

# =========================
# INPUT
# =========================
prompt = input("Enter your prompt: ")

messages = [
    {
        "role": "user",
        "content": prompt
    }
]

# =========================
# CHAT TEMPLATE
# =========================
if hasattr(tokenizer, "apply_chat_template"):

    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

else:
    text = prompt

# =========================
# TOKENIZE
# =========================
inputs = tokenizer(
    text,
    return_tensors="pt"
).to(device)

# =========================
# GENERATION
# =========================
with torch.inference_mode():

    torch.cuda.synchronize()
    start = time.time()

    outputs = model.generate(
        **inputs,

        # SPEED SETTINGS
        max_new_tokens=100,
        do_sample=False,

        # IMPORTANT
        use_cache=True,

        pad_token_id=tokenizer.pad_token_id,
        eos_token_id=tokenizer.eos_token_id,
    )

    torch.cuda.synchronize()
    end = time.time()

# =========================
# RESPONSE
# =========================
generated_tokens = outputs[0][inputs["input_ids"].shape[1]:]

response = tokenizer.decode(
    generated_tokens,
    skip_special_tokens=True
)

tokens_generated = len(generated_tokens)
speed = tokens_generated / (end - start)

# =========================
# OUTPUT
# =========================
print("\nAssistant:\n")
print(response)

print(f"\n[time] {end - start:.2f}s")
print(f"[speed] {speed:.2f} tok/s")
