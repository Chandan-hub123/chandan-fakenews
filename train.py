from preprocess import load_data, clean_text
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

# Models
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

# Metrics
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

import matplotlib.pyplot as plt
import seaborn as sns
import pickle

print("Loading data...")
data = load_data()

print("Processing data...")
data["content"] = data["title"] + " " + data["text"]
data["content"] = data["content"].apply(clean_text)

X = data["content"]
y = data["label"]

print("Vectorizing...")
vectorizer = TfidfVectorizer(max_features=7000, ngram_range=(1,2))
X = vectorizer.fit_transform(X)

print("Splitting...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train models (for comparison only)
models = {
    "Naive Bayes": MultinomialNB(),
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Random Forest": RandomForestClassifier(n_estimators=100)
}

accuracies = {}

for name, model in models.items():
    print(f"\nTraining {name}...")
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    accuracies[name] = acc

    print(f"{name} Accuracy:", acc)
    print("\nClassification Report:\n", classification_report(y_test, y_pred))

    cm = confusion_matrix(y_test, y_pred)
    print("Confusion Matrix:\n", cm)

    # Plot confusion matrix
    plt.figure()
    sns.heatmap(cm, annot=True)
    plt.title(f"{name} Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

# Plot accuracy comparison
plt.figure()
plt.bar(accuracies.keys(), accuracies.values())
plt.title("Model Accuracy Comparison")
plt.ylabel("Accuracy")
plt.xticks(rotation=30)
plt.show()

# FINAL MODEL (Stable choice)
print("\nTraining final model (Logistic Regression)...")
final_model = LogisticRegression(max_iter=1000)
final_model.fit(X_train, y_train)

# Save model
pickle.dump(final_model, open("model/model.pkl", "wb"))
pickle.dump(vectorizer, open("model/vectorizer.pkl", "wb"))

print("\nFinal Model Saved Successfully!")