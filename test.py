from ai_explain import explain_email
import joblib

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

email = input("Enter email: ")

X = vectorizer.transform([email])
prediction = model.predict(X)

if prediction[0] == 1:
    print("⚠️ Phishing")
else:
    print("✅ Safe")

# 🔥 ADD THIS
print("\nAI Explanation:")
print(explain_email(email))