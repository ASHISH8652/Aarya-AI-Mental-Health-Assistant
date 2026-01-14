import streamlit as st
import pickle
import re
from transformers import pipeline
import matplotlib.pyplot as plt
import pandas as pd
import datetime

# =========================================================
# 1️⃣ PAGE CONFIG (MUST BE FIRST)
# =========================================================
st.set_page_config(
    page_title="Aarya – AI Mental Health Assistant",
    page_icon="🩺",
    layout="centered",
    initial_sidebar_state="expanded"
)

# =========================================================
# 2️⃣ GLOBAL CSS
# =========================================================
st.markdown("""
<style>
html, body, [class*="css"] { animation: none !important; }

.stApp {
    background: linear-gradient(135deg, #0f172a, #020617);
    color: #e5e7eb;
}

.chat-bubble {
    padding: 16px 20px;
    border-radius: 18px;
    margin: 14px 0;
    max-width: 78%;
    line-height: 1.6;
    animation: fadeIn 0.6s ease-in-out;
}

.user-bubble {
    background: linear-gradient(135deg, #1e40af, #1e3a8a);
    color: white;
    margin-left: auto;
    border-bottom-right-radius: 6px;
}

.assistant-bubble {
    background: linear-gradient(135deg, #064e3b, #022c22);
    color: #ecfdf5;
    margin-right: auto;
    border-bottom-left-radius: 6px;
}

.emergency {
    background: #7f1d1d;
    color: #fee2e2;
    padding: 18px;
    border-radius: 16px;
    animation: pulse 1.5s infinite;
}

.meta {
    font-size: 13px;
    opacity: 0.75;
    margin-bottom: 8px;
}

.footer {
    font-size: 12px;
    opacity: 0.6;
    text-align: center;
    margin-top: 40px;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(8px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes pulse {
    0% { box-shadow: 0 0 0 0 rgba(239,68,68,0.4); }
    70% { box-shadow: 0 0 0 14px rgba(239,68,68,0); }
    100% { box-shadow: 0 0 0 0 rgba(239,68,68,0); }
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# 3️⃣ SESSION STATE
# =========================================================
if "intro_seen" not in st.session_state:
    st.session_state.intro_seen = False

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "emotional_state" not in st.session_state:
    st.session_state.emotional_state = []

if "negative_count" not in st.session_state:
    st.session_state.negative_count = 0

if "daily_moods" not in st.session_state:
    st.session_state.daily_moods = {}

if "language" not in st.session_state:
    st.session_state.language = "English"

# =========================================================
# 4️⃣ INTRO SCREEN
# =========================================================
if not st.session_state.intro_seen:
    st.markdown("""
    <div style="text-align:center; padding:50px;">
        <h1>🩺 Hello, I’m Aarya</h1>
        <p style="font-size:18px;">
        I’m here to listen — calmly, safely, and without judgment.
        </p>
        <hr style="opacity:0.3;">
        <p style="font-size:14px; opacity:0.7;">
        ⚠️ I’m not a medical professional.<br>
        If you are in immediate danger, please contact emergency services.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Begin Conversation 💬"):
        st.session_state.intro_seen = True
        st.rerun()

    st.stop()

# =========================================================
# 5️⃣ SIDEBAR CONTROLS
# =========================================================
st.sidebar.title("🧠 Aarya Control Panel")

st.session_state.language = st.sidebar.selectbox(
    "🌐 Language",
    ["English", "Hindi (Coming Soon)"]
)

st.sidebar.markdown("---")

if st.sidebar.button("🔄 Reset Session"):
    st.session_state.chat_history = []
    st.session_state.emotional_state = []
    st.session_state.daily_moods = {}
    st.session_state.negative_count = 0
    st.rerun()

if st.session_state.daily_moods:
    df_download = pd.DataFrame(
        st.session_state.daily_moods.items(),
        columns=["Date", "Mood"]
    )
    csv = df_download.to_csv(index=False).encode("utf-8")
    st.sidebar.download_button(
        "⬇️ Download Mood History",
        csv,
        "mood_history.csv",
        "text/csv"
    )

st.sidebar.markdown("---")
st.sidebar.markdown("### 🔒 Future Upgrades")
st.sidebar.markdown("🎤 Voice Chat")
st.sidebar.markdown("🧩 CBT Therapy")
st.sidebar.markdown("👤 Secure Login")
st.sidebar.markdown("☁️ Cloud Sync")

# =========================================================
# 6️⃣ LOAD MODELS
# =========================================================
sentiment_model = pickle.load(open("sentiment_model.pkl", "rb"))
vectorizer = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

emotion_ai = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=3
)

# =========================================================
# 7️⃣ NLP HELPERS
# =========================================================
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"[^a-z\s]", "", text)
    return re.sub(r"\s+", " ", text).strip()

def predict_sentiment(text):
    text = clean_text(text)
    vec = vectorizer.transform([text])
    pred = sentiment_model.predict(vec)[0]
    prob = sentiment_model.predict_proba(vec).max() * 100
    label = "Positive" if pred == 1 else "Negative"
    return ("Neutral", round(prob, 2)) if prob < 60 else (label, round(prob, 2))

EMERGENCY_WORDS = [
    "suicide", "kill myself", "end my life",
    "i want to die", "self harm"
]

def detect_emergency(text):
    return any(w in text.lower() for w in EMERGENCY_WORDS)

def nurse_reply(sentiment, negative_count):
    if sentiment == "Emergency":
        return (
            "🚨 I’m really concerned about your safety.\n\n"
            "📞 AASRA (India): 91-9820466726\n"
            "📞 Emergency: 112\n\n"
            "You are not alone."
        )
    if negative_count >= 3:
        return "💙 I’ve noticed this has been heavy for you. I’m here with you."
    if sentiment == "Negative":
        return "💭 That sounds really difficult. Want to share more?"
    if sentiment == "Positive":
        return "😊 I’m glad to hear that. What helped today?"
    return "🙂 I’m listening."

# =========================================================
# 8️⃣ APP HEADER
# =========================================================
st.markdown("## 🧠 Aarya – Your AI Mental Health Assistant")
st.markdown("*A calm, safe space to talk.*")

# =========================================================
# 9️⃣ CHAT FLOW
# =========================================================
user_input = st.text_input("How are you feeling today?")

if user_input:
    if detect_emergency(user_input):
        sentiment, confidence = "Emergency", 100
    else:
        sentiment, confidence = predict_sentiment(user_input)

    today = datetime.date.today().isoformat()
    st.session_state.daily_moods[today] = sentiment

    st.session_state.emotional_state.append(sentiment)
    st.session_state.negative_count = (
        st.session_state.negative_count + 1 if sentiment == "Negative" else 0
    )

    emotions = emotion_ai(user_input)[0]
    emotion_text = ", ".join(
        f"{e['label']} ({e['score']*100:.1f}%)" for e in emotions
    )

    reply = nurse_reply(sentiment, st.session_state.negative_count)

    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Aarya", reply))

# =========================================================
# 🔟 CHAT HISTORY RENDER
# =========================================================
for role, text in st.session_state.chat_history:
    if role == "You":
        st.markdown(
            f"<div class='chat-bubble user-bubble'>👤 <b>You</b><br>{text}</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<div class='chat-bubble assistant-bubble'>🩺 <b>Aarya</b><br>{text}</div>",
            unsafe_allow_html=True
        )

# =========================================================
# 1️⃣1️⃣ MOOD ANALYTICS
# =========================================================
if st.session_state.daily_moods:
    st.markdown("### 📊 Mood Distribution")

    mood_df = pd.DataFrame(
        st.session_state.daily_moods.items(),
        columns=["Date", "Mood"]
    )

    mood_counts = mood_df["Mood"].value_counts()

    fig, ax = plt.subplots()
    mood_counts.plot(kind="bar", ax=ax)
    ax.set_xlabel("Mood")
    ax.set_ylabel("Count")
    ax.set_title("Mood Overview")

    st.pyplot(fig)

    st.markdown("### 📅 Your Mood Journal")
    st.dataframe(mood_df, use_container_width=True)

# =========================================================
# 🔹 FOOTER
# =========================================================
st.markdown("""
<div class='footer'>
⚠️ This AI assistant does not replace professional mental health care.
</div>
""", unsafe_allow_html=True)

