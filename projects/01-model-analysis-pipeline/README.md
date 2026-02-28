# Project 01: Model Analysis & Pipeline Implementation
> Part of the Agentic AI Development & Security Series

## 🎯 Overview
This project evaluates the architectural trade-offs between utilizing a **Large Language Model (LLM)** for reasoning versus a **Small Language Model (SLM)** for specialized classification. It implements a production-grade, modular Scikit-learn pipeline for reproducible agentic workflows.

## 📊 1. Written Analysis: Mixtral vs. BERT
| Feature | Mixtral-8x7B (Fine-tuned) | BERT-Base (Classifier) |
| :--- | :--- | :--- |
| **Primary Use** | Complex Reasoning / Intent | High-speed Routing / PII Filtering |
| **Latency** | ~2,000ms - 5,000ms | < 100ms |
| **Cost** | High ($/Token or GPU VRAM) | Low (CPU-compatible) |
| **Reliability** | Potential for Hallucination | Deterministic Class Labels |

**Strategic Choice:** For this pipeline, we leverage the **Small Classifier** for initial data triage to minimize costs, routing to the **Large Model** only when high-reasoning confidence is required.

## ⚙️ 2. Pipeline Configuration
The system uses a `pipeline_config.yaml` to decouple model hyperparameters from execution logic. This ensures that a change in model version (e.g., upgrading from `v1` to `v2`) does not require a code refactor.



## 🛠️ 3. Implementation
The pipeline is built using **Scikit-learn** with custom transformers:
* **Modular:** Each step (Cleaning, Vectorization, Classification) is isolated.
* **Reproducible:** Random states and hyperparameters are locked via YAML.
* **Scalable:** The `TextCleaner` class handles preprocessing for various agent inputs.

## 🔐 4. Accountability & Compliance
* **Monitoring:** The **Lead ML Engineer** is responsible for monitoring model drift every 24 hours.
* **Compliance:** The **Security Officer** audits the pipeline for PII leakage during the `TextCleaner` phase to ensure data privacy standards (GDPR/SOC2) are met.

## 🧪 5. Reflection
Our versioning strategy (Semantic Versioning) combined with YAML-based configuration allows for seamless rollbacks if a model update fails security benchmarks. By prioritizing modularity, we ensure that as the "Agentic Brain" evolves, the supporting infrastructure remains stable and auditable.