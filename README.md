# ❤️ Heart Disease Prediction Project

This project builds a predictive model to identify heart disease using various ML techniques, with a Streamlit interface and Ngrok deployment.

---

## 🗂️ Project Structure

Heart_Disease_Project/
│── data/
│ └── heart_disease.csv
│── notebooks/
│ ├── 01_data_preprocessing.ipynb
│ ├── 02_pca_analysis.ipynb
│ ├── 03_feature_selection.ipynb
│ ├── 04_supervised_learning.ipynb
│ ├── 05_unsupervised_learning.ipynb
│ ├── 06_hyperparameter_tuning.ipynb
│ └── 07_model_export_and_deployment.ipynb
│── models/
│ └── final_model.pkl
│── ui/
│ └── app.py
│── deployment/
│ └── ngrok_setup.txt
│── results/
│ └── evaluation_metrics.txt
│── README.md
│── requirements.txt

## ✅ Features

- 📊 Supervised ML: Logistic Regression, SVM, Decision Tree, Random Forest
- 📈 Unsupervised ML: KMeans, Hierarchical Clustering
- ⚙️ Hyperparameter Tuning: GridSearchCV, RandomizedSearchCV
- 🌐 Streamlit App with Ngrok public deployment
- 💾 Model pipeline exported as `.pkl`

---

## 🚀 Run Streamlit App

```bash
python run.py


## Install Requirements

```bash
pip install -r requirements.txt