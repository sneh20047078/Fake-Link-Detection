# app.py

from flask import Flask, render_template, request, redirect, url_for, session
import joblib
import os
from sklearn.metrics import precision_score, recall_score, f1_score

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session support
model_names = ["Logistic Regression", "Random Forest", "Naive Bayes", "SVM", "Decision Tree"]

# Load models and vectorizer
vectorizer = joblib.load('models/vectorizer.pkl')
models = {name: joblib.load(f'models/{name}.pkl') for name in model_names}
accuracies = joblib.load('models/accuracies.pkl')
label_map = {0: 'Benign', 1: 'Malware', 2: 'Defacement', 3: 'Phishing'}

# Model metrics (fill in actual values as needed)
model_metrics = {
    "Logistic Regression": {"rmse": 0.603, "precision": 0.947, "accuracy": 0.947, "recall": 0.947, "f1": 0.936, "time": "0.008 sec"},
    "Random Forest": {"rmse": 0.533, "precision": 0.957, "accuracy": 0.958, "recall": 0.958, "f1": 0.952, "time": "0.818 sec"},
    "Naive Bayes": {"rmse": 0.735, "precision": 0.92, "accuracy": 0.913, "recall": 0.913, "f1": 0.891, "time": "0.001 sec"},
    "SVM": {"rmse": 0.579, "precision": 0.954, "accuracy": 0.953, "recall": 0.953, "f1": 0.944, "time": "10.717 sec"},
    "Decision Tree": {"rmse": 0.555, "precision": 0.951, "accuracy": 0.955, "recall": 0.955, "f1": 0.95, "time": "0.004 sec"}
}

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    selected_model = "Logistic Regression"
    per_model_results = None
    url_to_show = ""
    if request.method == 'POST':
        url = request.form['url']
        url_to_show = url
        selected_model = request.form['model']
        vectorized = vectorizer.transform([url])
        per_model_results = {}
        for name, model in models.items():
            pred = model.predict(vectorized)[0]
            if hasattr(model, "predict_proba"):
                proba = model.predict_proba(vectorized)[0].max()
            else:
                proba = None
            per_model_results[name] = {
                "prediction": label_map[pred],
                "probability": round(proba, 3) if proba is not None else "N/A"
            }
        pred = models[selected_model].predict(vectorized)[0]
        prediction = label_map[pred]
        # Store results in session and redirect
        session['prediction'] = prediction
        session['selected_model'] = selected_model
        session['per_model_results'] = per_model_results
        session['url_to_show'] = url_to_show
        return redirect(url_for('index'))
    else:
        # On GET, load from session if available, then clear
        prediction = session.pop('prediction', None)
        selected_model = session.pop('selected_model', "Logistic Regression")
        per_model_results = session.pop('per_model_results', None)
        url_to_show = session.pop('url_to_show', "")

    return render_template('index.html', model_names=model_names, accuracies=accuracies,
                           prediction=prediction, selected_model=selected_model, model_metrics=model_metrics, per_model_results=per_model_results, url_to_show=url_to_show)

if __name__ == '__main__':
    app.run(debug=True)
