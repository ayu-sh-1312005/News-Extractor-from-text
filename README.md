# 📰 News Summarizer (Streamlit + LLM)

A simple and powerful **News Summarizer Web App** built using **Streamlit + LangChain + Groq LLM**.
It extracts **multiple news headlines and summaries** from a given article using an LLM.

---
🚀 Live Demo

👉 Try the app here:
🔗 https://news-extractor-from-text-kw9i4jutrdfqiskzdtj29a.streamlit.app/

## 🚀 Features

* 📰 Extract **multiple news items** from a single article
* ✨ Generate **professional headlines**
* 📄 Summarize news in **< 300 words**
* 🎨 Clean and modern **Streamlit UI**
* 🔐 Secure API key handling (no hardcoding)
* ⚡ Powered by **Groq LLaMA 3.3 (70B)**

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **LLM:** Groq (LLaMA 3.3 70B)
* **Framework:** LangChain
* **Language:** Python

---

## 📂 Project Structure

```
project/
│── app.py
│── requirements.txt
│── .env                # (local only, not pushed)
│── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/news-summarizer.git
cd news-summarizer
```

### 2. Create virtual environment (recommended)

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## 🔑 Environment Setup (Local)

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the App

```
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

## ☁️ Deployment (Streamlit Cloud)

1. Push code to GitHub
2. Go to Streamlit Cloud → New App
3. Select your repo
4. Add secrets in **App Settings → Secrets**

```
GROQ_API_KEY = "your_api_key"
```

5. Click **Deploy** 🚀

---

## 📥 Input

Paste a news article or paragraph.

---

## 📤 Output

The app returns structured JSON:

```
[
  {
    "title": "News Heading",
    "news": "Summary of the news"
  }
]
```

Displayed as clean UI cards.

---

## ⚠️ Notes

* Do NOT commit `.env` file
* LLM output may vary depending on input quality
* Ensure API key is valid before running

---

## 🔥 Future Improvements

* 🌐 URL-based news extraction
* 📊 Keyword highlighting
* 📱 Mobile responsive UI
* ⚡ Caching for faster responses
* 🤖 Multi-model support

---

## 👨‍💻 Author

**Ayush Gupta**

---

## ⭐ If you like this project

Give it a star on GitHub ⭐
