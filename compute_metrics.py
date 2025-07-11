import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, mean_squared_error
import time
import numpy as np

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

model_metrics = {}

for name, model in models.items():
    print(f"Training {name}...")
    model.fit(X_train, y_train)
    start = time.time()
    y_pred = model.predict(X_test)
    elapsed = time.time() - start
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted', zero_division=0)
    recall = recall_score(y_test, y_pred, average='weighted', zero_division=0)
    f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    model_metrics[name] = {
        "rmse": round(rmse, 3),
        "precision": round(precision, 3),
        "accuracy": round(accuracy, 3),
        "recall": round(recall, 3),
        "f1": round(f1, 3),
        "time": f"{elapsed:.3f} sec"
    }

print("\nModel Metrics (copy these into your Flask app):")
import pprint; pprint.pprint(model_metrics) 