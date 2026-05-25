from transformers import AutoTokenizer, AutoModelForCausalLM

#Any model from the HuggingFace
model_name = ""

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    dtype="auto"
)

if model == True:
    print("Model loaded successfully!")
else :
    print("Failed to load the model.")
