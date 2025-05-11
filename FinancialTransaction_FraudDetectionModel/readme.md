# Berkeley: Capstone Project: 
Berkeley Capstone Project: Fraud 0Detection Model in Bank Financial Transactions. 

## Capstone Project Fraud Prevention and Detection ML/AI Model in Financial Transactions 

<What Apply classification methods and Compare>
Compare the results of k-nearest neighbors, logistic regression, decision trees, and support vector machines.

## [Juypter Notebook](https://github.com/Jhonson924/berkeley/blob/main/FinancialTransaction_FraudDetectionModel/financialTransactionFraudDetection.ipynb)

Contents

1. Business Understanding

    - 1.1. Overview
    - 1.2. Dataset
    - 1.3. Business Context
    - 1.4. Business Goal

2. Data Understanding

    - 2.1. Dataset understanding: cards_data
    - 2.2. Dataset understanding: mcc_codes
    - 2.3. Dataset understanding: users_data
    - 2.4. Dataset understanding: transactions_data
    - 2.5. Dataset understanding: train_fraud_labels
    * 2.5.1 Reading JSON file to dataframe and saving to CSV
    - 2.6. Data Understanding Summary

3. Exploratory Data Analysis (EDA)

    - 3.1. Data Exploration: using - cards_data
    - 3.1.1 Data Visualization
    - 3.1.2 Data Quality Checks
    - 3.2. Data Exploration: using - users_data
    - 3.1.1 Data Visualization
    - 3.1.2 Data Quality Checks
    - 3.3. Data Exploration: using - transactions_data
    - 3.1.1 Data Visualization
    - 3.1.2 Data Quality Checks
    - 3.4. Data Exploration: using - train_fraud_labels
    - 3.1.1 Data Visualization
    - 3.1.2 Data Quality Checks

4. Data Preparation

    - 4.1 Data Preparation: CardData
    - 4.1.1 Converting object to numeric datatype
    - 4.1.2 Converting 'has_chip' values to Binary
    - 4.1.3 Value Count CardBrand, CardType, hasChip
    - 4.1.4 Distibution of Cards
    - 4.1.5 Label Encodoing for CardBrand and CardType
    - 4.1.6 Rename ID to Card_ID
    - 4.1.7 TargetCardDta Columns to Merge
    
    - 4.2 Data Preparation: UserData
    - 4.2.1 Converting Object to numeric dataTypes
    - 4.2.2 Renaming Id to ClientID
    - 4.2.3 Label Enconding['gender']
    - 4.2.4 TargetUserData Columns

    - 4.3 Data Preparation: transactionData
    - 4.3.1 replace amount string column to float
    - 4.3.2 Convert date to datetime
    - 4.3.4 Transactions over time
    - 4.3.4 transactionData Errors: Unique
    - 4.3.5 FILLNA for errors
    - 4.3.6 ValueCount useChip, errors, mcc and merchantId
    - 4.3.7 Convert amount to numeric and coerce errors to NaN
    - 4.3.8 Create transactionType
    - 4.3.9 one-hot encoded columns
    - 4.3.10 Drop errors column check
    - 4.3.11 Label Encoding
    - 4.3.12 Transaction data columns to list

    - 4.4 Data Merge
    - 4.4.1 Merge transactionsData and CardsData
    - 4.4.2 Convert data field object to datetime
    - 4.4.3 Preprocessing Date & Time
    - 4.4.4 drop clientID and cardId
    - 4.4.5 Merge Transaction Data and dtTransactionData
    - 4.4.6 Merge User & Cards
    - 4.4.7 Drop Merge2 ClientID
    - 4.4.8 Merge Merge1 & Merge2 Data
    - 4.4.9 Merge Fraud Labels
    - 4.4.10 Prepare CSV File for targetData

    - 4.5 logTransformantion, PCA, KMeans++ : Apply

5. Modeling

    - 5.1 Prepare Features and Target
    - 5.2 Train/test Split
    - 5.3 Logistic Regression
    - 5.4 Decision Trees
    - 5.5 K-Nearest Neighbors (KNN)
    - 5.6 Random Forest
    - 5.7 SVM
    - 5.8 XGBoost
    - 5.9 Plot ROC Curves for all

6. Evaluation

    6.1 Cross-Validation, Grid Search and Hyperparameter Tuning
    - 6.1.1 Grid Search for Random Forests
    - 6.1.2 SVM with Grid Search
    - 6.1.3 K-Nearest Neighbors (KNN) with Grid Search
    - 6.1.4 Cross-validation for XGBoost

7. Timeseries Forecasting

8. Summary

9. Deployment

8. Key Findings
9. Model Performance Summary
10. Actionable Insights
11. Recommendations
12. Next Steps

#1. Business Understanding

##1.1. Overview
This comprehensive financial dataset combines transaction records, customer information, and card data from a banking institution, spanning across the 2010s decade.

##1.2. Dataset

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

##1.3. Business Context

The primary objective of this dataset is to facilitate the development and evaluation of machine learning models aimed at detecting fraudulent financial transactions

The goal of this project is to predict whether a given financial transaction is fraudulent or not, based on historical transaction data provided in the dataset.

    In financial systems, fraud detection is critical to prevent monetary loss, protect customers, and maintain trust in payment platforms.

    Early and accurate detection of fraud reduces financial risks and operational costs for banks, fintech companies, and e-commerce platforms.

    Build a binary classification model that, given a new transaction’s features (such as amount, timestamp, transaction type, etc.), predicts the likelihood that it is fraudulent(Fraud or Not Fraud)

##1.4. Business Goal

Fraud Detection and Security

#1. Business Understanding

##1.1. Overview
This comprehensive financial dataset combines transaction records, customer information, and card data from a banking institution, spanning across the 2010s decade.

##1.2. Dataset

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

##1.3. Business Context

The primary objective of this dataset is to facilitate the development and evaluation of machine learning models aimed at detecting fraudulent financial transactions

The goal of this project is to predict whether a given financial transaction is fraudulent or not, based on historical transaction data provided in the dataset.

    In financial systems, fraud detection is critical to prevent monetary loss, protect customers, and maintain trust in payment platforms.

    Early and accurate detection of fraud reduces financial risks and operational costs for banks, fintech companies, and e-commerce platforms.

    Build a binary classification model that, given a new transaction’s features (such as amount, timestamp, transaction type, etc.), predicts the likelihood that it is fraudulent(Fraud or Not Fraud)

##1.4. Business Goal

Fraud Detection and Security

- Build fraud detection model
- Create risk scoring models

