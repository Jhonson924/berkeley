# Berkeley: Capstone Project: 
Berkeley Capstone Project: 💳 Fraud Detection ML&AI Model in Bank Financial Transactions. 

## 📌 Project Overview

This project focuses on detecting fraudulent financial transactions using supervised machine learning models. By integrating transactional, user, and card-level data, we build predictive models capable of flagging high-risk transactions in real-time. The solution is designed for financial institutions, payment processors, and fraud analysts seeking to reduce losses and enhance fraud prevention.

The dataset combines multiple sources:

Transaction logs (amounts, timestamps, merchants)

User profiles (demographics, card usage behavior)

Card metadata (card type, chip status, issuing bank)

## 📖 Notebooks

## [Juypter Notebook](https://github.com/Jhonson924/berkeley/blob/main/FinancialTransaction_FraudDetectionModel/financialTransactionFraudDetection.ipynb)

## [XGBoost (Resampled) Deployment model Files (pkl)](https://github.com/Jhonson924/berkeley/tree/main/FinancialTransaction_FraudDetectionModel/model%20pkl)

Explore our modular Jupyter Notebooks:

Exploratory Analysis – EDA on transaction, card, and user data

Data Preparation – Merging and cleaning multi-source data

Modeling & Evaluation – Baseline and SMOTE-resampled model training

Interpretability with SHAP – Feature importance and local explanations

Deployment – Exporting models and building a FastAPI inference service

## 🔑 Key Features Considered

Transaction amount & timestamp

Merchant and MCC category

Card type, brand, chip usage

User credit profile and region

Historical fraud label

## 🚀 Project Workflow

Data Loading – Load and combine transaction, user, and card datasets

Data Cleaning & Preprocessing – Fix types, encode categories, fill missing values

Exploratory Data Analysis – Distributions, correlations, outlier checks

Feature Engineering – Derived columns, label encoding, scaling

Train/Test Split

Baseline Modeling – Logistic Regression, KNN, Decision Trees, Random Forest, XGBoost, SVM

Anomaly Detection Models – Isolation Forest, One-Class SVM

Address Class Imbalance – Resampling using SMOTE

Resampled Models – XGBoost, LightGBM, CatBoost, and others

Model Evaluation – ROC-AUC, F1, Precision, Recall

SHAP Explainability – Local and global model interpretation

Deployment – Save models, build FastAPI for real-time scoring

## 📊 Key Findings

XGBoost (Resampled) and LightGBM (Resampled) achieved near-perfect performance (AUC = 1.0)

Use of chip, transaction amount, zip code, and merchant type were top fraud predictors

Resampling significantly improved recall, making models more fraud-sensitive

SHAP values provided transparent insights, revealing that certain zip codes and missing chip usage highly increased fraud risk

## 🎯 Business & Technical Recommendations

✅ Deploy XGBoost (Resampled) as the primary model for production

✅ Implement custom probability thresholding for alert tuning

✅ Use SHAP explanations in analyst dashboards to justify model decisions

✅ Continuously monitor for drift and retrain regularly

✅ Avoid using anomaly-only models like Isolation Forest in production due to poor recall

## 🔬 Future Enhancements

Integrate real-time streaming data pipelines for fraud scoring

Incorporate device fingerprinting and geolocation as features

Implement ensemble voting of top resampled models

Track model drift and performance decay over time

Expand to multi-class fraud types (e.g., identity theft vs. transaction replay)

## 🛠️ Tech Stack

Python: pandas, NumPy, scikit-learn, imbalanced-learn, SHAP, XGBoost, LightGBM, CatBoost

Data Visualization: Matplotlib, Seaborn

Model Deployment: FastAPI, Joblib

Evaluation Metrics: Precision, Recall, F1, ROC-AUC

Resampling: SMOTE

Explainability: SHAP (waterfall, beeswarm, summary plots)

## 👥 Contributors

Developed by Johnson Susainathan as part of an end-to-end ML&AI fraud detection pipeline project.

Berkeley's Professional Certificate in Machine Learning and Artificial Intelligence!

It was completed as part of their final Capstone project under the supervision of Professor [Viviana Márquez](https://www.linkedin.com/in/vivianamarquez/). 