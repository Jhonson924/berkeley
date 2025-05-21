# 💳 Fraud Detection Using Machine Learning

## 📌 Project Overview

This project focuses on detecting **fraudulent financial transactions** using **supervised machine learning models**. By integrating transactional, user, and card-level data, To build predictive models capable of flagging high-risk transactions in real-time. The solution is designed for financial institutions, payment processors, and fraud analysts seeking to reduce losses and enhance fraud prevention.

The dataset combines multiple sources:

[💳 Financial Transactions Dataset: Analytics](https://www.kaggle.com/datasets/computingvictor/transactions-fraud-datasets)

- transactions_data.csv: Main transaction records
- cards_data.csv: Credit/debit card details
- users_data.csv: User/customer demographic data
- mcc_codes.json: Merchant category classification
- train_fraud_labels.json:

## 📖 Notebooks

### [Juypter Notebook](https://github.com/Jhonson924/berkeley/blob/main/FinancialTransaction_FraudDetectionModel/financialTransactionFraudDetection.ipynb)

### [Deployment model Files (pkl)](https://github.com/Jhonson924/berkeley/tree/main/FinancialTransaction_FraudDetectionModel/model%20pkl)

- **Exploratory Analysis** – EDA on transaction, card, and user data
- **Data Preparation** – Merging and cleaning multi-source data
- **Modeling & Evaluation** – Baseline and SMOTE-resampled model training
- **Interpretability with SHAP** – Feature importance and local explanations
- **Deployment** – Exporting models and building a FastAPI inference service

## 🔑 Key Features Considered

- **Transaction amount & timestamp**
- **Merchant and MCC category**
- **Card type, brand, chip usage**
- **User credit profile and region**
- **Historical fraud label**

## 🚀 Project Workflow

1. **Data Loading** – Load and combine transaction, user, and card datasets
2. **Data Cleaning & Preprocessing** – Fix types, encode categories, fill missing values
3. **Exploratory Data Analysis** – Distributions, correlations, outlier checks
4. **Feature Engineering** – Derived columns, label encoding, scaling
5. **Train/Test Split**
6. **Baseline Modeling** – Logistic Regression, KNN, Decision Trees, Random Forest, XGBoost, SVM
7. **Anomaly Detection Models** – Isolation Forest, One-Class SVM
8. **Address Class Imbalance** – Resampling using SMOTE
9. **Resampled Models** – XGBoost, LightGBM, CatBoost, and others
10. **Model Evaluation** – ROC-AUC, F1, Precision, Recall
11. **SHAP Explainability** – Local and global model interpretation
12. **Deployment** – Save models, build FastAPI for real-time scoring

## 📊 Key Findings

- **XGBoost (Resampled)** and **LightGBM (Resampled)** achieved near-perfect performance (AUC = 1.0)
- **Use of chip**, **transaction amount**, **zip code**, and **merchant type** were top fraud predictors
- **Resampling significantly improved recall**, making models more fraud-sensitive
- **SHAP values provided transparent insights**, revealing that certain zip codes and missing chip usage highly increased fraud risk

## 🎯 Business & Technical Recommendations

- ✅ Deploy **XGBoost (Resampled)** as the primary model for production
- ✅ Implement **custom probability thresholding** for alert tuning
- ✅ Use **SHAP explanations in analyst dashboards** to justify model decisions
- ✅ Continuously **monitor for drift and retrain regularly**
- ✅ Avoid using anomaly-only models like Isolation Forest in production due to poor recall

## 🔬 Future Enhancements

- Integrate **real-time streaming data pipelines** for fraud scoring
- Incorporate **device fingerprinting and geolocation** as features
- Implement **ensemble voting** of top resampled models
- Track **model drift** and performance decay over time
- Expand to **multi-class fraud types** (e.g., identity theft vs. transaction replay)

## 🛠️ Tech Stack

- **Python**: pandas, NumPy, scikit-learn, imbalanced-learn, SHAP, XGBoost, LightGBM, CatBoost
- **Data Visualization**: Matplotlib, Seaborn
- **Model Deployment**: FastAPI, Joblib
- **Evaluation Metrics**: Precision, Recall, F1, ROC-AUC
- **Resampling**: SMOTE
- **Explainability**: SHAP (waterfall, beeswarm, summary plots)

## 👥 Contributors

Developed by Johnson Susainathan as part of an end-to-end ML fraud detection pipeline project. It was completed as part of their **final Capstone project** in the **Professional Certificate in Machine Learning and Artificial Intelligence**, under the supervision of **Professor  [Viviana Márquez](https://www.linkedin.com/in/vivianamarquez/)**

