# 🍔 Food Delivery Time Prediction & Performance Analytics

An end-to-end Machine Learning project that predicts food delivery time based on delivery distance, weather conditions, traffic levels, time of day, vehicle type, preparation time, and courier experience.

The project combines **Python, Machine Learning, Power BI, and Streamlit** to transform delivery data into useful predictions and operational insights.

## 🚀 Live Demo

**[Launch Food Delivery AI App](https://food-delivery-ai-nasrullah.streamlit.app/)**

## 📌 Project Overview

Food delivery time can vary depending on several operational and environmental factors. This project uses Machine Learning regression models to estimate the expected delivery duration based on customer order and courier-related information.

The application allows users to enter delivery details and receive an estimated delivery time through an interactive Streamlit interface.

## 🎯 Project Objectives

- Analyze food delivery data using Exploratory Data Analysis (EDA).
- Clean and preprocess missing and inconsistent data.
- Identify factors affecting delivery duration.
- Build and evaluate multiple Machine Learning regression models.
- Select and save the best-performing model.
- Develop an interactive Power BI dashboard.
- Deploy a prediction application using Streamlit.

## 📂 Dataset Information

The dataset contains **1,000 records and 9 columns**.

| Column | Description |
|---|---|
| Order_ID | Unique order identifier |
| Distance_km | Delivery distance in kilometers |
| Weather | Weather conditions |
| Traffic_Level | Traffic intensity |
| Time_of_Day | Order time category |
| Vehicle_Type | Delivery vehicle |
| Preparation_Time_min | Food preparation duration |
| Courier_Experience_yrs | Courier experience |
| Delivery_Time_min | Target variable |

**Target Variable:** `Delivery_Time_min`

## 🛠️ Technologies Used

**Programming & Data Analysis**
- Python
- Pandas
- NumPy

**Data Visualization**
- Matplotlib
- Seaborn
- Power BI

**Machine Learning**
- Scikit-learn
- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- K-Nearest Neighbors (KNN)
- Gradient Boosting Regressor

**Deployment & Tools**
- Streamlit
- Joblib
- Jupyter Notebook
- Git & GitHub

## 🔍 Project Workflow

1. **Project Setup** – Environment and dataset preparation.
2. **Exploratory Data Analysis** – Understanding distributions, patterns, correlations, and outliers.
3. **Data Cleaning** – Handling missing values and checking duplicates.
4. **Feature Preprocessing** – Numerical scaling and categorical encoding.
5. **Model Building** – Training multiple regression algorithms.
6. **Model Evaluation** – Comparing models using MAE, MSE, RMSE, and R² Score.
7. **Model Saving** – Saving the selected model using Joblib.
8. **Power BI Dashboard** – Analyzing delivery performance and operational insights.
9. **Streamlit Application** – Building an interactive prediction interface.
10. **Deployment** – Publishing the application using Streamlit Community Cloud.

## 🤖 Machine Learning Models

The following regression algorithms were evaluated:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- K-Nearest Neighbors Regressor
- Gradient Boosting Regressor

### Evaluation Metrics

| Metric | Purpose |
|---|---|
| MAE | Measures average absolute prediction error |
| MSE | Measures average squared prediction error |
| RMSE | Measures prediction error in target units |
| R² Score | Measures explained variance |

The final model was selected based on the lowest RMSE from the evaluated models.

## 📊 Power BI Dashboard

The project includes a Power BI dashboard designed to analyze delivery performance and operational patterns.

Planned dashboard analysis includes:
- Total orders and average delivery time.
- Delivery performance by traffic level.
- Weather impact on delivery duration.
- Delivery trends by time of day.
- Vehicle-wise performance.
- Distance and preparation time analysis.

## 🌐 Streamlit Application Features

- Interactive delivery prediction form.
- Delivery distance input.
- Weather condition selection.
- Traffic level selection.
- Time-of-day selection.
- Vehicle type selection.
- Food preparation time input.
- Courier experience input.
- Estimated delivery time display.
- Delivery input summary.
- Home and About Project pages.

## 📁 Project Structure

```text
Food-Delivery-Time-Prediction/
│
├── datasets/
│   └── Food_Delivery_Times.csv
│
├── notebook/
│   ├── Food_Delivery_Analysis.ipynb
│   │
│   └── models/
│       └── food_delivery_prediction_model.pkl
│
├── app.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Mohd-NasrullahSidd1137/Food-Delivery-Time-Prediction.git
```

### 2. Navigate to the project directory

```bash
cd Food-Delivery-Time-Prediction
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your local browser.

## 📦 Requirements

```text
streamlit
pandas
numpy
scikit-learn
joblib
```

## 📈 Key Learning Outcomes

- Practical experience with end-to-end Machine Learning workflows.
- Data cleaning and exploratory data analysis.
- Regression model development and evaluation.
- Feature preprocessing using Scikit-learn pipelines.
- Model serialization and loading using Joblib.
- Interactive dashboard development with Power BI.
- Deployment of Machine Learning applications using Streamlit.

## 👨‍💻 Author

**Mohd Nasrullah Siddiqui**
