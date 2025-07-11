# model_trainer.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib
import os

# Load dataset
df = pd.read_csv('url_data.csv').head(50000)
df['type'] = df['type'].map({'benign': 0, 'malware': 1, 'defacement': 2, 'phishing': 3})

# Vectorize URL text
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['URL'])
y = df['type']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define models
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Random Forest": RandomForestClassifier(),
    "Naive Bayes": MultinomialNB(),
    "SVM": SVC(probability=True),
    "Decision Tree": DecisionTreeClassifier()
}

# Save directory
os.makedirs("models", exist_ok=True)

# Train and save each model
accuracies = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    acc = accuracy_score(y_test, pred)
    accuracies[name] = acc
    joblib.dump(model, f'models/{name}.pkl')

# Save vectorizer
joblib.dump(vectorizer, 'models/vectorizer.pkl')

# Save accuracies
joblib.dump(accuracies, 'models/accuracies.pkl')

print("All models trained and saved.")
