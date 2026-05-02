import streamlit as st
import joblib
from ai_explain import explain_email

# Load model
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.title("🔐 AI Phishing Detector")

email = st.text_area("Enter Email Text:")

if st.button("Analyze"):
    X = vectorizer.transform([email])
    prediction = model.predict(X)

    if prediction[0] == 1:
        st.error("⚠️ Phishing Detected")
    else:
        st.success("✅ Safe Email")

    st.subheader("AI Explanation:")
    st.write(explain_email(email))