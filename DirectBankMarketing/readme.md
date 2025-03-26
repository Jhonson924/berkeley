# Berkeley
Berkeley ML/AI Modules and Practical application III: Portuguese Direct Bank Marketing via PhoneCalls

## Practical Application3 Portuguese Direct Bank Marketing via PhoneCalls <What Apply classification methods and Compare>
Compare the results of k-nearest neighbors, logistic regression, decision trees, and support vector machines.

## [Juypter Notebook](https://github.com/Jhonson924/berkeley/blob/main/DirectBankMarketing/BankMarketing.ipynb)

### Context
- The data is related with direct marketing campaigns (phone calls) of a Portuguese banking institution. 
- The classification goal is to predict if the client will subscribe a term deposit (variable y).

### Business Problem Statement

 Business Understanding
The primary goal of this analysis was to predict whether a client would subscribe to a term deposit after a marketing phone call. This predictive model can significantly enhance marketing efficiency and customer targeting, helping banks minimize costs and maximize campaign success.

---

### Data Understanding and Cleaning
1. **Data Sources:**
   - Three datasets were analyzed: `bank.csv`, `bank-full.csv`, and `bank-additional.csv`.
   - `bank.csv` and `bank-full.csv` contain 17 features, while `bank-additional.csv` contains 20 features with richer information.

2. **Data Cleaning:**
   - Handled missing values and duplicates.
   - Performed data encoding for categorical variables.
   - Applied log transformation to reduce skewness and minimize the effect of outliers.

3. **Data Transformation:**
   - One-hot encoding was applied to categorical features.
   - Numerical features were scaled using `StandardScaler`.
   - Applied `PCA` to reduce dimensionality while preserving 95% variance.

###  Exploratory Data Analysis (EDA)
1. Visualized the distribution of each feature to understand the data patterns.
2. Analyzed correlation matrices to identify relationships between numerical variables.
3. Plotted pairplots and scatter plots to detect possible outliers and interactions.
4. Derived insights into client profiles that are more likely to subscribe.

### Modeling and Evaluation
1. Built four classification models:
   - **Logistic Regression**
   - **Support Vector Machine (SVM)**
   - **Decision Trees**
   - **K-Nearest Neighbors (KNN)**

2. Applied cross-validation and hyperparameter tuning to optimize each model.
3. Performed threshold optimization to balance precision and recall.
4. Visualized decision boundaries to understand model behavior.

### Evaluation Metrics
Models were evaluated using the following metrics:
- **Accuracy:** Proportion of correctly predicted instances.
- **Precision:** Accuracy of positive predictions.
- **Recall:** Ability to detect actual positives.
- **F1-Score:** Balance between precision and recall.
- **ROC-AUC:** Ability to distinguish between classes.

### Key Findings
1. **Best Performing Models:**
   - **Logistic Regression and SVM** showed the highest accuracy and balanced precision-recall scores.
   - **Decision Trees** performed well but were prone to overfitting.
   - **KNN** struggled due to high-dimensionality.

2. **Threshold Optimization:**
   - Optimal thresholds varied per model but typically ranged between **0.3 and 0.6** for the best trade-off between precision and recall.

3. **Model Performance:**
   - Logistic Regression demonstrated the best generalization with high interpretability.
   - SVM performed similarly but was computationally more expensive.
   - Decision Trees provided interpretability but lacked robustness.
   - KNN was sensitive to feature scaling and dimensionality.

### Recommendations
1. **Model Deployment:**
   - Deploy **Logistic Regression** as the primary model due to its high performance and interpretability.
   - Use **SVM** as a secondary option for more complex decision boundaries.

2. **Marketing Strategy:**
   - Prioritize contacting clients with high predicted subscription probability.
   - Focus on improving data quality and adding features related to customer engagement and feedback.

3. **Future Improvements:**
   - Explore **ensemble methods** like Random Forest or Gradient Boosting for improved accuracy.
   - Implement **model explainability techniques** to increase trust and transparency.
   - Continuously monitor model performance and update as customer behaviors evolve.

### Next Steps
1. **Implementation and Monitoring:**
   - Integrate the model into the marketing workflow for real-time predictions.
   - Monitor model performance periodically to detect drift.

2. **Further Analysis:**
   - Conduct a **feature importance analysis** to identify the most influential factors.
   - Perform **customer segmentation** to identify different profiles for targeted marketing.

---

### Conclusion
The analysis demonstrates that predictive modeling can significantly enhance the efficiency of marketing campaigns by targeting clients more likely to subscribe to term deposits. By implementing the recommended models and strategies, banks can improve campaign success rates while reducing operational costs