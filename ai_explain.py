import requests

def explain_email(email):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi3",
                "prompt": f"Explain if this email is phishing:\n{email}",
                "stream": False   # 🔥 IMPORTANT FIX
            }
        )

        data = response.json()
        return data.get("response", "No response from AI")

    except Exception as e:
        return f"Error: {str(e)}"