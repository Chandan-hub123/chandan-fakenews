import pickle
from preprocess import clean_text   # ✅ THIS LINE IS IMPORTANT

model = pickle.load(open("model/model.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

def predict_news(text):
    cleaned_text = clean_text(text)

    if len(cleaned_text.split()) < 5:
        return "⚠️ Please enter detailed news"

    vector = vectorizer.transform([cleaned_text])

    prediction = model.predict(vector)[0]
    confidence = max(model.predict_proba(vector)[0])

    if confidence < 0.5:
        return f"⚠️ Uncertain Prediction (Confidence: {confidence:.2f})"

    if prediction == 1:
        return f"🟢 Real News (Confidence: {confidence:.2f})"
    else:
        return f"🔴 Fake News (Confidence: {confidence:.2f})"