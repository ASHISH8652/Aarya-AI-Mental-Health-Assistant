# 🩺 Aarya – Your AI Mental Health Assistant

## 🧠 Aarya – AI Mental Health Assistant

Aarya is an **AI-powered mental health assistant** designed to provide empathetic conversation, emotional awareness, and basic mental health guidance using **Natural Language Processing (NLP)** and **Machine Learning**. The application is built with **Python** and deployed using **Streamlit**, offering a clean, human-like interface similar to a digital nurse or mental health companion.

## 🌱 Overview

**Aarya** is an **AI-powered mental health assistant** designed to provide **calm, empathetic, and emotionally aware conversations**.  
It acts like a **digital mental-health nurse**, helping users reflect on emotions while promoting safety, awareness, and ethical AI use.

Built using **Python, NLP, and Machine Learning**, and deployed with **Streamlit**, Aarya focuses on **empathy-first design** rather than medical diagnosis.

> ⚠️ **Disclaimer:** This application is for educational and supportive purposes only.
> It is **not a replacement for professional medical advice, diagnosis, or treatment**.

---

## 🌟 Key Features

* 💬 **Conversational Mental Health Support** – Friendly, empathetic chat interface
* 😊 **Emotion Detection** – Detects emotions such as joy, sadness, anger, fear, and neutrality
* 📊 **Sentiment Analysis** – Classifies user input as positive, negative, or neutral
* 🚨 **Emergency Keyword Detection** – Identifies crisis-related keywords and provides safety guidance
* 📈 **Emotional Trend Visualization** – Tracks emotional changes during the session
* 🔄 **Session Reset** – Allows users to start fresh conversations
* 🌙 **Dark UI Theme** – Calm, modern, and user-friendly design

---

## 🏗️ Project Structure



## 🏗️ Project Architecture

```
Aarya-AI-Mental-Health-Assistant/
│
├── app.py                     # Main Streamlit application
├── requirements.txt           # Python dependencies
├── sentiment_model.pkl        # Trained ML sentiment model
├── tfidf_vectorizer.pkl       # TF-IDF vectorizer for text processing
├── emotion_chatbot.ipynb      # Jupyter notebook (development & testing)
├── README.md                  # Project documentation
├── LICENSE                    # MIT License
└── .gitignore                 # Ignored files
```

---

## ⚙️ Technologies Used

* **Python 3.9+**
* **Streamlit** – Web application framework
* **Scikit-learn** – Machine learning models
* **NLTK / Text Processing** – Text cleaning & analysis
* **Matplotlib** – Emotion trend visualization
* **Pickle** – Model serialization

---

## 🧠 How It Works

1. User enters a message describing their feelings
2. Text is cleaned and preprocessed
3. Emotion detection model predicts emotional probabilities
4. Sentiment analysis classifies overall sentiment
5. Emergency keywords are checked for safety
6. Aarya responds with an empathetic, context-aware message
7. Emotional trends are visualized for the session

---

## 🚀 Installation & Local Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/ASHISH8652/Aarya-AI-Mental-Health-Assistant.git
cd Aarya-AI-Mental-Health-Assistant
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
streamlit run app.py
```

The app will open in your browser at:

```
http://localhost:8501
```

---

## 🌐 Deployment

This project is optimized for deployment on **Streamlit Cloud**.

This project is deployed on Streamlit Cloud.

Live App:

https://aarya-ai-mental-health-assistant.streamlit.app/


Steps:

1. Push code to GitHub
2. Go to [https://share.streamlit.io](https://share.streamlit.io)
3. Connect GitHub repository
4. Select `app.py` as the main file
5. Deploy 🎉

---

## 🔐 Ethics & Safety

* Emergency-related inputs are handled with priority
* The app avoids giving medical diagnoses
* Encourages seeking professional help when needed
* Designed with empathy-first responses

---

## 📌 Future Enhancements

* 🤖 Integration with Large Language Models (LLMs)
* 🧾 User authentication & chat history
* 🌍 Multi-language support
* 📱 Mobile-optimized UI
* 🏥 Integration with professional resources

---

## 👨‍💻 Author

**Ashish Kumar Prusty**
B.Tech Student | AI & ML Enthusiast
GitHub: [https://github.com/ASHISH8652](https://github.com/ASHISH8652)

---

## 📜 License

This project is licensed under the **MIT License**.

---

> *“Technology should not replace human care — it should support it.”* 💙
