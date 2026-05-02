# 🔐 AI Phishing Detection System

An AI-powered system that detects phishing emails using Machine Learning and provides human-like explanations using a local LLM.

---

## 🚀 Features

* Detects phishing vs safe emails
* Uses TF-IDF + Logistic Regression
* AI explanation using Ollama (phi3)
* Runs locally (no API required)

---

## 🛠️ Tech Stack

* Python
* Scikit-learn
* Ollama (phi3)
* Pandas, NumPy
* Requests

---

## ⚙️ Setup

```bash
pip install pandas scikit-learn joblib requests
python train.py
ollama run phi3
python test.py
```

---

## 🧪 Example

**Input:**
your account is suspended click now

**Output:**
⚠️ Phishing
AI Explanation: Uses urgency and suspicious language

---

## 🎯 Use Case

Helps detect phishing emails and supports cybersecurity analysis.

---

## 👨‍💻 Author

Aman Raj
