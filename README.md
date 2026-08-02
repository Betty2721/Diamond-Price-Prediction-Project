# 💎 Diamond Price Prediction Using Machine Learning

## 📌 Project Overview

This project predicts the market price of a diamond using Machine Learning regression algorithms. The goal is to build an accurate predictive model that estimates diamond prices based on their physical and quality characteristics. Multiple regression models were trained, evaluated, and compared to identify the best-performing model.

The final model was deployed as an interactive Streamlit web application, allowing users to enter diamond attributes and receive real-time price predictions.

---

## 🎯 Business Problem

Diamond pricing is influenced by several factors such as carat, cut, color, clarity, and dimensions. Estimating the correct market price manually can be difficult and inconsistent.

This project aims to automate the pricing process by developing a machine learning model that accurately predicts diamond prices, helping buyers, sellers, and jewelers make informed decisions.

---

## 📂 Dataset

**Dataset:** Diamonds Dataset

### Dataset Summary

- **Number of Records:** 53,940
- **Features:** 9 Input Features
- **Target Variable:** Price

### Features

| Feature | Description |
|----------|-------------|
| Carat | Weight of the diamond |
| Cut | Quality of the cut |
| Color | Diamond color grade |
| Clarity | Diamond clarity grade |
| Depth | Total depth percentage |
| Table | Width of the diamond's top |
| X | Length (mm) |
| Y | Width (mm) |
| Z | Depth (mm) |

**Target**

- Price

---

## 🔍 Exploratory Data Analysis (EDA)

The following analyses were performed:

- Dataset overview
- Missing value analysis
- Duplicate value analysis
- Data type inspection
- Price distribution
- Carat distribution
- Correlation heatmap
- Feature relationships
- Outlier visualization

---

## ⚙ Data Preprocessing

The following preprocessing steps were applied:

- Feature and target separation
- Identification of numerical and categorical variables
- Ordinal Encoding for categorical features
- Train-test split (80% training, 20% testing)
- Feature scaling using StandardScaler

---

## 🤖 Regression Models Implemented

The following regression algorithms were trained and evaluated:

- Linear Regression
- Ridge Regression
- Lasso Regression
- Decision Tree Regression
- Random Forest Regression
- Gradient Boosting Regression
- Support Vector Regression (SVR)

### Bonus Models

- AdaBoost Regressor
- Extra Trees Regressor
- XGBoost Regressor
- LightGBM Regressor
- CatBoost Regressor

---

## 📊 Model Evaluation Metrics

Each model was evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

---

## 🏆 Best Model

After comparing all regression models, **XGBoost Regressor** achieved the best overall performance.

### Final Performance

| Metric | Value |
|----------|---------|
| MAE | 276.37 |
| MSE | 277,868.22 |
| RMSE | 527.13 |
| R² Score | 0.9825 |

### Why XGBoost?

- Highest R² Score
- Lowest RMSE
- Excellent prediction accuracy
- Strong generalization capability
- Handles nonlinear relationships effectively

---

## ⚙ Hyperparameter Tuning

The final model was optimized using **RandomizedSearchCV** with **5-Fold Cross Validation**.

### Tuned Parameters

- n_estimators
- learning_rate
- max_depth
- subsample
- colsample_bytree

---

## 🌐 Web Application

A Streamlit web application was developed for real-time predictions.

### Features

- Modern user interface
- Home page
- Project description
- Dataset information
- Model information
- Prediction form
- Prediction results
- Model comparison
- About team page

Users can enter diamond characteristics and instantly receive an estimated market price.

---

## 🛠 Technologies Used

### Programming Language

- Python

### Libraries

- Pandas
- NumPy
- Scikit-learn
- XGBoost
- LightGBM
- CatBoost
- Matplotlib
- Seaborn
- Plotly
- Joblib
- Streamlit

---

## 📁 Project Structure

```text
diamond-price-prediction/
│
├── data/
│   └── diamonds.csv
│
├── models/
│   ├── xgboost_model.pkl
│   ├── ordinal_encoder.pkl
│   └── scaler.pkl
│
├── pages/
│   ├── Project_Description.py
│   ├── Dataset_Information.py
│   ├── Model_Information.py
│   ├── Predict_Price.py
│   ├── Model_Comparison.py
│   └── About_Team.py
│
├── images/
│
├── notebook/
│   └── Diamond_Price_Prediction.ipynb
│
├── style.css
├── app.py
├── requirements.txt
└── README.md