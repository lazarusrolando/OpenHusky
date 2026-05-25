from transformers import AutoTokenizer, AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-7B-Instruct", trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-7B-Instruct", trust_remote_code=True)

tokenizer.pad_token = tokenizer.eos_token

model.save_pretrained("./openhusky-7B-instruct",safe_serialization=False)
tokenizer.save_pretrained("./openhusky-7B-instruct")
