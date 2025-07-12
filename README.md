# Fake Link Detection

A machine learning-based web application that analyzes URLs to detect malicious websites. The application uses multiple ML models to classify URLs into different categories: Benign, Malware, Defacement, and Phishing.

## Features

- **Multi-Model Analysis**: Uses 5 different machine learning models:
  - Logistic Regression
  - Random Forest
  - Naive Bayes
  - Support Vector Machine (SVM)
  - Decision Tree

- **Real-time Analysis**: Analyze any URL instantly with detailed predictions
- **Comprehensive Analytics**: View model performance metrics and per-link analytics
- **Interactive Dashboard**: Modern UI with charts and visualizations
- **Model Comparison**: Compare predictions across all models for a given URL



- Modern, responsive web interface
- Interactive model selection
- Real-time URL analysis
- Detailed analytics dashboard with charts
- Per-link model comparison

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/sneh20047078/Fake-Link-Detection.git
   cd Fake-Link-Detection
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download the dataset and train models**
   
   **Option A: Download pre-trained models**
   - Download the trained models from [releases](https://github.com/sneh20047078/Fake-Link-Detection/releases/tag/v1.0)
   - Extract to the `models/` directory
   
   **Option B: Train your own models**
   - Download the dataset: [URL Dataset for Malicious URL Detection](https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset)
   - Place `url_data.csv` in the project root
   - Run the training script:
     ```bash
     python model_trainer.py
     ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open your browser**
   Navigate to `http://localhost:5000`

## Usage

1. **Enter a URL**: Type any website URL in the input field
2. **Select a Model**: Choose from the available ML models
3. **Analyze**: Click "Analyze" to get the prediction
4. **View Analytics**: Click "Show Report/Analytics" to see detailed metrics

## Project Structure

```
URL Type Detector Version 2.0/
├── app.py                 # Main Flask application
├── model_trainer.py       # Model training script
├── compute_metrics.py     # Metrics calculation script
├── requirements.txt       # Python dependencies
├── url_data.csv          # Dataset 
├── models/               # Trained models directory 
│   ├── vectorizer.pkl
│   ├── accuracies.pkl
│   └── [model files].pkl
├── static/               # Static assets
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   ├── ambient.mp3
│   ├── favicon.ico
│   └── logo.svg
└── templates/            # HTML templates
    └── index.html
```

## Technologies Used

### Backend
- **Flask**: Web framework
- **scikit-learn**: Machine learning library
- **pandas**: Data manipulation
- **joblib**: Model serialization

### Frontend
- **HTML5/CSS3**: Structure and styling
- **Tailwind CSS**: Utility-first CSS framework
- **JavaScript**: Interactivity
- **Chart.js**: Data visualization
- **Lucide**: Icons
- **tsParticles**: Background animations

## Model Performance

The application includes comprehensive analytics showing:
- Accuracy, Precision, Recall, F1-score
- RMSE (Root Mean Square Error)
- Processing time for each model
- Per-link prediction probabilities

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Dataset: [URL Dataset for Malicious URL Detection](https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset)
- Icons: [Lucide](https://lucide.dev/)
- Charts: [Chart.js](https://www.chartjs.org/)
- CSS Framework: [Tailwind CSS](https://tailwindcss.com/)

## Project Report and Demo

- [Project Report (PDF)](Project_Report.pdf)
- [Working Demo Video (MP4)](Working_Demo.mp4)


Project Link: [https://github.com/sneh20047078/Fake-Link-Detection](https://github.com/sneh20047078/Fake-Link-Detection) 