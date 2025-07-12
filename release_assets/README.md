# Pre-trained Models and Dataset

This release contains the pre-trained machine learning models and dataset for the Fake Link Detection application.

## Contents

### Models
- `Logistic Regression.pkl` - Logistic Regression model
- `Random Forest.pkl` - Random Forest model  
- `Naive Bayes.pkl` - Naive Bayes model
- `SVM.pkl` - Support Vector Machine model
- `Decision Tree.pkl` - Decision Tree model
- `vectorizer.pkl` - TF-IDF vectorizer for text preprocessing
- `accuracies.pkl` - Model accuracy scores

### Dataset
- `url_data.csv` - Training dataset with URL features and labels

## Installation

1. **Download this release** and extract the files
2. **Create a `models` directory** in your project root
3. **Copy all `.pkl` files** to the `models/` directory
4. **Copy `url_data.csv`** to your project root
5. **Run the application**:
   ```bash
   python app.py
   ```

## Model Performance

The pre-trained models achieve the following performance metrics:

- **Logistic Regression**: 94.7% accuracy
- **Random Forest**: 95.8% accuracy  
- **Naive Bayes**: 91.3% accuracy
- **SVM**: 95.3% accuracy
- **Decision Tree**: 95.5% accuracy

## Dataset Information

The dataset contains:
- 50,000 URL samples
- 4 classes: Benign (0), Malware (1), Defacement (2), Phishing (3)
- TF-IDF features extracted from URL text

## Usage

After placing the files in the correct locations, you can:
1. Analyze URLs using the web interface
2. View model performance analytics
3. Compare predictions across all models

## Requirements

- Python 3.7+
- Flask
- scikit-learn
- pandas
- joblib

Install dependencies with:
```bash
pip install -r requirements.txt
``` 