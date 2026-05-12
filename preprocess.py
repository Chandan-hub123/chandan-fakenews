import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def load_data():
    fake = pd.read_csv("data/Fake.csv")
    real = pd.read_csv("data/True.csv")

    fake["label"] = 0
    real["label"] = 1

    data = pd.concat([fake, real])
    data = data.sample(frac=1, random_state=42).reset_index(drop=True)

    return data

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)

    words = text.split()
    words = [w for w in words if w not in stop_words]

    return " ".join(words)