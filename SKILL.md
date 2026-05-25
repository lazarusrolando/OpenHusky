# Skills for OpenHusky

This document summarizes the main “skills” the model can respond to, based on the current training dataset in `data/train.jsonl`.

> Note: These are conversational/knowledge skills (Q&A style). The model is not guaranteed to be correct for every edge case.

---

## 1) Programming Fundamentals (Basics + Concepts)
**What it covers:** core programming terminology and beginner explanations.

**Example trained prompts:**
- “What is Python?”
- “What is React?”
- “Explain HTML.”
- “What is JavaScript?”
- “What is CSS do?”
- “What is a function?”
- “What is a variable?”
- “What is a loop?”
- “What is an algorithm?”
- “What is recursion?”

---

## 2) Web Development (Frontend + Full-Stack Concepts)
**What it covers:** frontend frameworks, common web concepts, and web stack terminology.

**Example trained prompts:**
- “What is React?” / “What is React Native?”
- “What is Next.js?”
- “What is Vue.js?”
- “What is Angular?”
- “What is Bootstrap?”
- “What is TypeScript?”
- “What is REST API?”
- “What is GraphQL?”
- “What is DOM?” / “What is virtual DOM?”
- “What is server-side rendering?”

---

## 3) APIs, Backend, and Software Engineering Basics
**What it covers:** definitions and practical understanding of backend components.

**Example trained prompts:**
- “What is an API?”
- “What is Node.js?”
- “What is middleware?”
- “What is authentication?” / “What is authorization?”
- “What is caching?” / “What is CDN?”
- “What is CI/CD?” / “What is Jenkins?”
- “What is Docker?”

---

## 4) Databases & Data Modeling
**What it covers:** SQL/NoSQL concepts, storage terminology, and database operations.

**Example trained prompts:**
- “What is a database?”
- “What is SQL?”
- “What is MongoDB?”
- “What is ORM?”
- “What is normalization?”
- “What is ACID property?”
- “What is indexing in databases?”
- “What is sharding?”
- “What is replication in databases?”
- “What is ETL process?”

---

## 5) DevOps / Infrastructure / Cloud Computing
**What it covers:** cloud services, deployment, monitoring, and infrastructure concepts.

**Example trained prompts:**
- “What is cloud computing?”
- “What is AWS?” / “What is Azure?”
- “What is Kubernetes?”
- “What is Terraform?” / “What is Ansible?”
- “What is containerization?”
- “What is load balancing?”
- “What is observability?”
- “What is Prometheus?” / “What is Grafana?”

---

## 6) Cybersecurity (Common Threats + Defenses)
**What it covers:** basic threat definitions and defensive concepts.

**Example trained prompts:**
- “What is cybersecurity?”
- “What is encryption?”
- “What is VPN?”
- “What is phishing?”
- “What is malware?” / “What is ransomware?”
- “What is XSS?” / “What is CSRF?”
- “What is SQL injection?”
- “What is zero trust security?”
- “What is firewall?” / “What is endpoint protection?”

---

## 7) AI / Machine Learning / Deep Learning Concepts
**What it covers:** broad AI terminology and conceptual explanations.

**Example trained prompts:**
- “What is AI?” / “What is machine learning?”
- “What is deep learning?”
- “What is NLP?” / “What is transformer model?”
- “What is tokenization?” / “What is embedding in AI?”
- “What is inference in AI?”
- “What is overfitting?” / “What is underfitting?”
- “What is reinforcement learning?”
- “What is RAG in AI?” / “What is vector database?”

---

## 8) Generative AI & LLM Workflows (High-Level)
**What it covers:** general ideas about prompting, fine-tuning, and generative pipelines.

**Example trained prompts:**
- “What is prompt engineering?”
- “What is fine-tuning?”
- “What is LoRA training?”
- “What is quantization?”
- “What is prompt chaining?”
- “What is generative AI?”
- “What is hallucination?”
- “What is prompt injection?”

---

## 9) Career Guidance & Learning Strategy
**What it covers:** motivation, learning paths, interview/prep basics, and portfolio strategy.

**Example trained prompts:**
- “How do I improve coding skills?”
- “What should I learn first in programming?”
- “What project should I build?”
- “How do I prepare for coding interviews?”
- “How can I stay focused?”
- “How do I become productive?”
- “I need motivation”
- “How do I improve my portfolio?”
- “Can you help with programming?”

---

## 10) Light Conversational Support
**What it covers:** greeting/small talk and generic supportive responses.

**Example trained prompts:**
- “Hello”
- “Good morning”
- “How are you?”
- “What’s up?”
- “I am bored”
- “Thank you”
- “See you later”

---

# How to use this
- If you want the model to respond in a specific “skill” area, phrase your prompt using the same keywords as the examples (e.g., “What is SQL injection?”, “Explain RAG in AI”, “How do I prepare for interviews?”).
- For more control, you can ask for a format explicitly (example):
  - “Answer in 3 bullets, then give one example.”
  - “Give a short definition first, then pros/cons.”
- The model will typically answer in plain English (Q&A style) similar to the training responses.

---

# Dataset / upload notes (practical)
- If Hugging Face authentication fails during upload, re-run `upload.py` after updating your token (or skip uploading for now).
- If `data/train.jsonl` contains invalid/malformed JSONL lines, skip the broken line and continue processing (don’t crash the whole job).


