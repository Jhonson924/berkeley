# Berkeley: Capstone Project: 
Berkeley Capstone Project: Fraud Detection Model in Bank Financial Transactions. 

## Capstone Project Fraud Detection ML/AI Model in Financial Transactions 

<What Apply classification methods and Compare>
Compare the results of k-nearest neighbors, logistic regression, decision trees, and support vector machines.

## [Juypter Notebook](https://github.com/Jhonson924/berkeley/blob/main/FinancialTransaction_FraudDetectionModel/financialTransactionFraudDetection.ipynb)

## [Deployment model Files (pkl)](https://github.com/Jhonson924/berkeley/tree/main/FinancialTransaction_FraudDetectionModel/model%20pkl)


#1. Business Understanding

##1.1. Overview
This comprehensive financial dataset combines transaction records, customer information, and card data from a banking institution, spanning across the 2010s decade.

##1.2. Dataset

[💳 Financial Transactions Dataset: Analytics](https://www.kaggle.com/datasets/computingvictor/transactions-fraud-datasets)

Links to an external site.

5 datasets will be analyzed: Primarly for Fraud analysis and detection model

- transactions_data.csv: Main transaction records
- cards_data.csv: Credit/debit card details
- users_data.csv: User/customer demographic data
- mcc_codes.json: Merchant category classification
- train_fraud_labels.json:
    
-- Binary fraud labels for transactions (target),
-- Indicates fraudulent vs. legitimate transactions
-- Ideal for training supervised fraud detection models

Each dataset contributes to building a holistic feature set for fraud detection.

##1.3. Business Context

The primary objective of this dataset is to facilitate the development and evaluation of machine learning models aimed at detecting fraudulent financial transactions

The goal of this project is to predict whether a given financial transaction is fraudulent or not, based on historical transaction data provided in the dataset.

    In financial systems, fraud detection is critical to prevent monetary loss, protect customers, and maintain trust in payment platforms.

    Early and accurate detection of fraud reduces financial risks and operational costs for banks, fintech companies, and e-commerce platforms.

    Build a binary classification model that, given a new transaction’s features (such as amount, timestamp, transaction type, etc.), predicts the likelihood that it is fraudulent(Fraud or Not Fraud)

##1.4. Business Goal

Fraud Detection and Security

# 1. Business Understanding

## 1.1. Overview
This comprehensive financial dataset combines transaction records, customer information, and card data from a banking institution, spanning across the 2010s decade.

## 1.2. Dataset

💳 Financial Transactions Dataset: Analytics

Links to an external site.

5 datasets will be analyzed: Primarly for Fraud analysis and detection model

- transactions_data.csv: Main transaction records
- cards_data.csv: Credit/debit card details
- users_data.csv: User/customer demographic data
- mcc_codes.json: Merchant category classification
- train_fraud_labels.json:
    
-- Binary fraud labels for transactions (target),
-- Indicates fraudulent vs. legitimate transactions
-- Ideal for training supervised fraud detection models

Each dataset contributes to building a holistic feature set for fraud detection.

## 1.3. Business Context

The primary objective of this dataset is to facilitate the development and evaluation of machine learning models aimed at detecting fraudulent financial transactions

The goal of this project is to predict whether a given financial transaction is fraudulent or not, based on historical transaction data provided in the dataset.

    In financial systems, fraud detection is critical to prevent monetary loss, protect customers, and maintain trust in payment platforms.

    Early and accurate detection of fraud reduces financial risks and operational costs for banks, fintech companies, and e-commerce platforms.

    Build a binary classification model that, given a new transaction’s features (such as amount, timestamp, transaction type, etc.), predicts the likelihood that it is fraudulent(Fraud or Not Fraud)

## 1.4. Business Goal

Fraud Detection and Security

- Build fraud detection model
- Create risk scoring models


# 10. Key Findings

- The dataset is highly imbalanced with very few fraudulent transactions.

- Tree-based ensemble models (XGBoost, Random Forest) outperform simpler models (Logistic Regression, Decision Tree) in fraud detection.

- Random Forest with tuned hyperparameters achieved 99.88% accuracy and an ROC-AUC of 0.9997, identifying 60% of actual frauds with 96% precision.

- K-Nearest Neighbors and Decision Tree showed lower recall and AUC, making them less reliable for fraud detection in this context.

# 11. Actionable Insights

- Ensemble models are highly effective in fraud detection tasks.

- Precision is more critical than recall in production environments to avoid false alerts, but recall cannot be neglected for fraud control.

- ROC-AUC scores above 0.99 indicate that the models rank transactions very effectively in terms of fraud risk, which enables threshold-based decisioning.

# 12. Recommendations

Deploy XGBoost or tuned Random Forest in production for initial fraud scoring.
Fine-tune the classification threshold (e.g., 0.3 instead of 0.5) to balance recall and precision based on risk appetite.

Consider combining model predictions with rule-based alerts for high-risk scenarios.

Use the fraud probability output to build risk scoring dashboards for fraud analysts.
