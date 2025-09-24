# 🛡️ Insurance Advisor – Streamlit App

[![Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![OpenAI](https://img.shields.io/badge/Powered%20by-OpenAI-412991.svg)](https://openai.com/)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)

An **AI-powered Insurance Advisor** built with **Streamlit** and **OpenAI GPT**, designed to answer insurance-related queries in a clean, user-friendly chat interface.  
It ensures that conversations remain strictly **insurance-focused**, rejecting off-topic questions gracefully.  

---

## 🚀 Demo

👉 Run locally:  
```bash
streamlit run insurance_streamlit_app.py
```

👉 Or try on [Streamlit Cloud](https://streamlit.io/cloud) *(if deployed)*  

![App Screenshot](docs/screenshot.png) <!-- Replace with actual screenshot -->

---

## ✨ Features

✅ Beautiful **chat-style interface** with custom styling  
✅ **User & Assistant chat bubbles** for clear separation  
✅ **Insurance keyword filter** – keeps queries relevant  
✅ Sidebar with **About & Disclaimer**  
✅ Clean **gradient background & modern UI**  
✅ Powered by **OpenAI GPT** for reliable responses  

---

## 📦 Installation

Clone this repository and install dependencies:

```bash
# Clone the repo
git clone https://github.com/yourusername/insurance-advisor.git
cd insurance-advisor

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

Create a **`.streamlit/secrets.toml`** file with your OpenAI API key:

```toml
OPENAI_API_KEY = "your_api_key_here"
```

---

## ▶️ Usage

Run the app:

```bash
streamlit run insurance_streamlit_app.py
```

Then open your browser at **`http://localhost:8501`**.

---

## 🖼️ Screenshots

### 💬 Chat Interface
![Chat Screenshot](docs/chat_example.png)

### 📑 Sidebar
![Sidebar Screenshot](docs/sidebar_example.png)

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) – interactive web UI  
- [OpenAI GPT](https://platform.openai.com/) – AI responses  
- [Python](https://www.python.org/) – app logic  

---

## 📜 Disclaimer

⚠️ This application is for **general insurance information only**.  
It does **not** replace professional financial, medical, or legal advice.  

---

## 🤝 Contributing

Contributions are welcome!  
1. Fork the repo  
2. Create a new branch (`feature/your-feature`)  
3. Commit changes and push  
4. Submit a Pull Request 🎉  

---

## 📄 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

### 👨‍💻 Author
Developed by [Your Name](https://github.com/yourusername)  
