# OpenHusky

A small repository for fine-tuning and running Hugging Face causal language models (Qwen-style instruct models) using a simple JSONL dataset.

Key files:
- `train.jsonl` — training data in JSONL format (`{"prompt": ..., "response": ...}` per line)
- `train.py` — saves a base instruct model into `./openhusky-7B-instruct/`
- `test.py` — interactive local inference for `./openhusky-7B-instruct/`
- `upload.py` — uploads `train.jsonl` to Hugging Face Hub as a dataset
- `SKILL.md` — high-level description of learned “skills”

---

## Prerequisites

- Python 3.10+
- PyTorch + CUDA (if using GPU)
- `transformers` and `huggingface_hub`

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Dataset format

`data/train.jsonl` must be JSON Lines where each line contains:

```json
{"prompt": "...", "response": "..."}
```

If any line is malformed, make sure to remove/fix it before training.

---

## Run a local inference test

`test.py` loads the model from:

- `your-model-folder-name`

Then it asks for a prompt from stdin and prints the generated response.

Run:

```bash
python test.py
```

---

## Save a base instruct model (7B)

`train.py` loads `any model from huggingface` and saves it locally into:

- `your-model-folder-name`

Run:

```bash
python train.py
```

---

## Upload dataset to Hugging Face Hub

`upload.py` logs in (using a token in the file) and uploads:

- local `data/train.jsonl`
- to repo `your-repo`
- as a dataset named `train.jsonl`

Run:

```bash
python upload.py
```

Note: Update the token in `upload.py` before running.

---

## Notes

- This repo currently focuses on lightweight scripts for saving/loading/uploading models.
- For real fine-tuning training loops (SFT), add the appropriate training pipeline and configuration.

