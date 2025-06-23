# ❤️ Heart Disease Prediction Project

![Streamlit](https://img.shields.io/badge/Streamlit-Enabled-blueviolet)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Used-orange)
![Pandas](https://img.shields.io/badge/Pandas-Used-darkblue)
![NumPy](https://img.shields.io/badge/NumPy-Used-lightgrey)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Used-green)
![Seaborn](https://img.shields.io/badge/Seaborn-Used-teal)
![Joblib](https://img.shields.io/badge/Joblib-Used-purple)
![Pyngrok](https://img.shields.io/badge/Pyngrok-Used-black)
![Status](https://img.shields.io/badge/Status-Ongoing-yellow)

This project builds a predictive model to identify heart disease using various ML techniques, with a Streamlit interface and Ngrok deployment.

---

## 🔍 Project Overview

This project includes:

- 🧹 Data preprocessing: handling missing values, encoding, scaling.
- 📉 PCA for dimensionality reduction.
- 🧠 Supervised ML: Logistic Regression, Decision Tree, Random Forest, SVM.
- 🔬 Feature selection: RFE, Chi-square, Feature Importance.
- 📊 Unsupervised ML: KMeans and Hierarchical Clustering.
- 🧪 Model evaluation: accuracy, precision, recall, F1-score, AUC, confusion matrix.
- 🛠️ Hyperparameter tuning: GridSearchCV & RandomizedSearchCV.
- 💾 Model deployment using joblib pipeline.
- 🌐 Streamlit Web App for real-time predictions.
- 🌍 Ngrok for public sharing.

---

## ✅ Required Packages

| Package        | Version | Description                      |
| -------------- | ------- | -------------------------------- |
| `streamlit`    | 1.37.1  | Web app UI                       |
| `scikit-learn` | 1.4.2   | Machine learning algorithms      |
| `pandas`       | 2.2.2   | Data manipulation                |
| `numpy`        | 1.26.4  | Numerical computations           |
| `matplotlib`   | 3.8.4   | Visualizations                   |
| `seaborn`      | 0.13.2  | Statistical data visualization   |
| `joblib`       | 1.4.2   | Model saving/loading             |
| `pyngrok`      | 6.1.0   | Ngrok integration for deployment |


## 🚀 Run Locally

```bash
python run.py
```
### Install requirements

```bash
pip install -r requirements.txt
```
---
### Expose publicly using Ngrok

Go to https://dashboard.ngrok.com and sign in or register

Copy the auth tokens from https://dashboard.ngrok.com/get-started/setup

Add auth tokens
```bash
ngrok config add-authtoken <YOUR_AUTHTOKEN>
```
-Run the app
-In a new terninal:
```bash
ngrok http 8501
```
Copy the generated https://xxxxx.ngrok-free.app URL and open it in a browser.
---

### 📊 Model Performance

You can view evaluation metrics (accuracy, precision, recall, F1-score, AUC) in:
results/evaluation_metrics.txt
The final model is a RandomForestClassifier with optimized hyperparameters, trained via a pipeline with StandardScaler.

---
### 🧠 Final Model Info

🔎 Model: Random Forest (tuned)

⚙️ Wrapped in: Scikit-learn Pipeline (with scaling)

📦 Exported as: models/final_model.pkl
---



### 🧑‍💻 Author
Mohammed Helal
📧 mhmdhlalnajy74@gmail.com
Built during the Sprints AI Bootcamp
