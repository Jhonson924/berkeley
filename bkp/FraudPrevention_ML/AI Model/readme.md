# Berkeley: Capstone Project: 
Berkeley Capstone Project: Fraud Prevention and Detection in Bank Financial Transactions. 

## Capstone Project Fraud Prevention and Detection ML/AI Model in Financial Transactions 

<What Apply classification methods and Compare>
Compare the results of k-nearest neighbors, logistic regression, decision trees, and support vector machines.

## [Juypter Notebook](https://github.com/Jhonson924/berkeley/blob/main/DirectBankMarketing/BankMarketing.ipynb)

## 1. Problem Statement:
The primary objective of this dataset is to facilitate the development and evaluation of machine learning models aimed at detecting fraudulent financial transactions

The goal of this project is to predict whether a given financial transaction is fraudulent or not, based on historical transaction data provided in the dataset.

In financial systems, fraud detection is critical to prevent monetary loss, protect customers, and maintain trust in payment platforms.

Early and accurate detection of fraud reduces financial risks and operational costs for banks, fintech companies, and e-commerce platforms.

Build a binary classification model that, given a new transaction’s features (such as amount, timestamp, transaction type, etc.), predicts the likelihood that it is fraudulent(Fraud or Not Fraud)

### 1.1 Fraud Detection and Security
Build near-real-time fraud detection systems
Develop anomaly detection algorithms
Create risk scoring models
Implement transaction monitoring systems
Design security alert systems

### 1.2 Data Source 
💳 Financial Transactions Dataset: AnalyticsLinks to an external site.

5 datasets will be analyzed: Primary for Fraud analysis and detection model Only and this dataset are inter dependent.

transactions_data.csv: Main transaction records
- cards_data.csv: Credit/debit card details
- users_data.csv: User/customer demographic data
- mcc_codes.json: Merchant category classification
- train_fraud_labels.json:
Binary fraud labels for transactions (target), 
Indicates fraudulent vs. legitimate transactions
Ideal for training supervised fraud detection models
Each dataset contributes to building a holistic feature set for fraud detection.

### 1.3 Techniques to be Used
- Exploratory Data Analysis (EDA)

* Visualized the distribution of each feature to understand the data patterns.
Analyzed correlation matrices to identify relationships between numerical variables.
Plotted pairplots and scatter plots to detect possible outliers and interactions.
Derived insights into client profiles that are more likely to subscribe.
Categorical Variable Analysis
Data Preparation

- Handled missing values and duplicates.
* Performed data encoding for categorical variables.
Applied log transformation to reduce skewness and minimize the effect of outliers.
One-hot encoding was applied to categorical features. (Data Transformation)
Numerical features were scaled using Standard Scaler
Applied PCA to reduce dimensionality while preserving 95% variance.

### 1.4 Modeling

 - Baseline: Logistic Regression
 - Classical ML: Decision Tree, K-Nearest Neighbors, SVM
 - Ensemble Techniques: Random Forest, XGBoost(Optional
 - Optional: Neural Networks (for deeper patterns)
 - Tuning: Cross-validation, Grid Search
 - Optimization: Threshold tuning(balance precision and recall), cost-sensitive learning
 - Visualized decision boundaries to understand model behavior

### 1.5 Evaluation Metrics

- Accuracy: Overall prediction correctness
- Precision: Correct fraud predictions among all flagged frauds
- Recall: Coverage of actual fraudulent cases detected
- F1-Score: Balance between precision and recall.
- ROC-AUC: Probability the model ranks a random fraud higher than a non-fraud
- Deployment Summary: With Performance metrics

### 1.6 Expected Result/Goal
- High Recall for Fraud Detection: The model should correctly identify a significant proportion of fraudulent transactions, even at the cost of some false positives.

- Balanced Precision and F1-Score: While maximizing recall, the model should still achieve a balanced F1-score, avoiding too many false alarms that could lead to unnecessary interventions.

- Improved Performance with Ensemble Methods:  (e.g., Random Forest, XGBoost) are expected to outperform baseline models (like Logistic Regression) in detecting non-linear fraud patterns.

- Final cleaned, encoded, and reduced-dimensionality dataset supports potential integration into a near-real-time fraud detection system.

### 1.7 Key Usecase & Importance
Financial Impact: Fraudulent transactions cost financial institutions billions annually. Detecting them early helps reduce direct losses, chargebacks, and reputational damage.

Customer Trust and Security: Consumers expect secure digital transactions. Effective fraud detection systems build customer confidence and enhance user retention.

Regulatory and Compliance Requirements:  Financial regulators increasingly require institutions to implement automated fraud monitoring systems. Solution contributes to compliance readiness.

## 2. Data Understanding
**Data Sources:**

**Dataset Description:**

**Key Features:**

**Potential Challenges:**


## 3. Exploratory Data Analysis (EDA)
- Visualized the distribution of each feature to understand the data patterns.
- Analyzed correlation matrices to identify relationships between numerical variables.
- Plotted pairplots and scatter plots to detect possible outliers and interactions.
- Derived insights into client profiles that are more likely to subscribe.

**Relationship Between Variables:**


### Conclusion
