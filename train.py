import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Load data
df = pd.read_csv("email.csv")

# Convert text → numbers
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['text'])

# Labels
y = df['label'].map({'phishing':1, 'safe':0})

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model trained ✅")