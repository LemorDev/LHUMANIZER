# 📝 LHUMANIZER: AI-to-Human Text Converter

A blazing-fast, Streamlit-based web application that leverages Groq's Llama 3.3 model to transform AI-generated academic drafts into natural, human-written prose. 

This tool was developed as an experimental side-project alongside an IT capstone project (a geo-fenced mobile incident reporting application for local municipalities) to explore advanced prompt engineering, API orchestration, and AI detection evasion.

## ✨ Features
* **Advanced Evasion Algorithms:** Utilizes custom prompt engineering techniques like **Clause Inversion**, **Strategic Imperfection**, and **Conversational Simplification** to consistently bypass leading AI detectors (ZeroGPT, Grammarly, Turnitin).
* **One-Shot Processing:** Abandons clunky iterative loops in favor of a single, highly optimized API payload that restructures entire paragraphs while maintaining academic cohesion.
* **Streamlit Web UI:** A clean, modern, and user-friendly browser interface.
* **Groq LPU Engine:** Powered by Meta's `llama-3.3-70b-versatile` model hosted on Groq for near-instant inference speeds.
* **Citation Protection:** Hard-coded algorithmic locks ensure APA and IEEE citations are never altered, deleted, or moved during the rewriting process.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Frontend:** Streamlit
* **LLM API:** Groq (`groq-python` client)
* **Environment Management:** `python-dotenv`

## 🚀 Installation & Setup

**1. Clone the repository**
```bash
git clone [https://github.com/YOUR_USERNAME/LHUMANIZER.git](https://github.com/YOUR_USERNAME/LHUMANIZER.git)
cd LHUMANIZER