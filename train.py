from transformers import AutoTokenizer, AutoModelForCausalLM

#Note: model = tokenizer at the double quotes
model = AutoModelForCausalLM.from_pretrained("", trust_remote_code=True) #Any model from HuggingFace
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-7B-Instruct", trust_remote_code=True) #Any model from HuggingFace

tokenizer.pad_token = tokenizer.eos_token

model.save_pretrained("<your-model-folder-name>",safe_serialization=False)
tokenizer.save_pretrained("<your-model-folder-name>")
