# Food Delivery Time Prediction & Performance Analytics

An end-to-end machine learning and business intelligence project that
estimates food delivery duration and explores the operational and
environmental factors associated with delivery performance.

**Live Streamlit App:**
https://food-delivery-ai-nasrullah.streamlit.app/\
**GitHub Repository:**
https://github.com/Mohd-NasrullahSidd1137/Food-Delivery-Time-Prediction

------------------------------------------------------------------------

## Project Overview

This project combines exploratory data analysis (EDA), machine learning,
an interactive Streamlit application, and a Power BI dashboard.

The machine learning application predicts estimated delivery time from
order and courier details. The Power BI report explores delivery
performance across traffic levels, weather conditions, vehicle types,
time of day, delivery distance, and food preparation time.

## Project Objectives

-   Explore and understand food delivery data.
-   Clean missing values and prepare data for analysis and modelling.
-   Identify patterns and relationships among delivery-related
    variables.
-   Train and evaluate regression models to estimate delivery time.
-   Deploy the prediction workflow through Streamlit.
-   Build an interactive Power BI report for performance analysis.

## Dataset

**File:** `datasets/Food_Delivery_Times.csv`\
**Dataset size:** 1,000 records and 9 columns.

  -----------------------------------------------------------------------
  Column                              Description
  ----------------------------------- -----------------------------------
  `Order_ID`                          Unique order identifier

  `Distance_km`                       Delivery distance in kilometres

  `Weather`                           Weather condition

  `Traffic_Level`                     Traffic condition

  `Time_of_Day`                       Time period of the order

  `Vehicle_Type`                      Delivery vehicle

  `Preparation_Time_min`              Food preparation time in minutes

  `Courier_Experience_yrs`            Courier experience in years

  `Delivery_Time_min`                 Actual delivery time in minutes;
                                      prediction target
  -----------------------------------------------------------------------

## Exploratory Data Analysis

The analysis includes data inspection, missing-value analysis,
distribution analysis, outlier investigation, and relationship analysis.

### Key Findings

-   Delivery time has a positively skewed distribution.
-   Six potential delivery-time outliers were identified using the IQR
    method and retained for analysis.
-   Distance has a strong positive correlation with delivery time
    (approximately **0.781**).
-   Preparation time has a positive correlation with delivery time
    (approximately **0.307**).
-   Courier experience has a weak negative correlation with delivery
    time.
-   High traffic is associated with higher median delivery time.
-   Snowy weather has the highest median delivery time among the weather
    categories.
-   Vehicle types have relatively similar delivery-time distributions.

These findings describe associations in the dataset and should not be
interpreted as proof of causation.

### EDA Screenshots

![EDA Screenshot 1](Screenshots/eda%20part%201.PNG)

![EDA Screenshot 2](Screenshots/part%202%20str.PNG)

![EDA Screenshot 3](Screenshots/part%203%20str.PNG)

![EDA Screenshot 4](Screenshots/part%204%20str.PNG)

## Data Cleaning and Preprocessing

The dataset contains missing values in categorical fields and courier
experience. The preparation workflow includes:

-   Imputing missing categorical values using the mode.
-   Imputing missing courier experience values using the median.
-   Preparing numerical and categorical features for modelling.
-   Applying numerical scaling.
-   Encoding categorical variables using one-hot encoding.

The preprocessing workflow uses a `ColumnTransformer` with
`SimpleImputer`, `StandardScaler`, and
`OneHotEncoder(handle_unknown="ignore")`.

## Machine Learning

This is a regression task. The target variable is `Delivery_Time_min`.

### Models Evaluated

-   Linear Regression
-   Decision Tree Regressor
-   Random Forest Regressor
-   K-Neighbors Regressor
-   Gradient Boosting Regressor

### Evaluation Metrics

Models are evaluated using:

-   Mean Absolute Error (MAE)
-   Mean Squared Error (MSE)
-   Root Mean Squared Error (RMSE)
-   R-squared (R²)

The selected model is based on the lowest RMSE. Actual model scores are
not listed because the evaluation values have not been provided here.

The preprocessing and model workflow is saved with Joblib for use by the
Streamlit application.

## Streamlit Application

The interactive application allows users to enter delivery details and
receive an estimated delivery time.

**[Open the Live Streamlit
App](https://food-delivery-ai-nasrullah.streamlit.app/)**

### Application Inputs

-   Delivery distance
-   Weather condition
-   Traffic level
-   Time of day
-   Vehicle type
-   Food preparation time
-   Courier experience

### Application Screenshot

![Streamlit App](Screenshots/streamlit%20part%201.PNG)

## Power BI Dashboard

The Power BI report contains an introductory page and three analytical
pages.

### Intro Page

Project title and dashboard landing page.

![Dashboard Intro](Screenshots/Dashboard%20page%204.PNG)

### Page 1 --- Delivery Overview

KPI cards for total orders, average delivery time, average preparation
time, and average distance. Charts compare average delivery time by
traffic and weather, and show the distribution of orders by vehicle
type.

![Delivery Overview](Screenshots/Dashboard%20page%201.PNG)

### Page 2 --- Delivery Performance Analysis

Compares delivery time with distance and preparation time, and analyses
average delivery time by time of day.

![Delivery Performance Analysis](Screenshots/Dashboard%20page%202.PNG)

### Page 3 --- Key Factors Analysis

Examines average delivery time by weather and traffic level, including a
traffic-versus-weather matrix.

![Key Factors Analysis](Screenshots/Dashboard%20page%203.PNG)

**Power BI file:** `Dashboard/Dashboard.pbix`

## Technology Stack

  Area                      Tools / Libraries
  ------------------------- ---------------------
  Programming               Python
  Data analysis             Pandas, NumPy
  Data visualization        Matplotlib, Seaborn
  Machine learning          Scikit-learn
  Model persistence         Joblib
  Interactive application   Streamlit
  Business intelligence     Microsoft Power BI
  Version control           Git, GitHub

## Repository Structure

This tree reflects the folders and files visible in the project
screenshots. Add any additional notebook and root-level files to the
tree if they are present in your repository.

``` text
Food-Delivery-Time-Prediction/
│
├── Dashboard/
│   └── Dashboard.pbix
│
├── Screenshots/
│   ├── Dashboard page 1.PNG
│   ├── Dashboard page 2.PNG
│   ├── Dashboard page 3.PNG
│   ├── Dashboard page 4.PNG
│   ├── eda part 1.PNG
│   ├── part 2 str.PNG
│   ├── part 3 str.PNG
│   ├── part 4 str.PNG
│   └── streamlit part 1.PNG
│
├── datasets/
│   └── Food_Delivery_Times.csv
│
└── notebook/
    ├── .ipynb_checkpoints/
    └── models/
        └── food_delivery_prediction_model.pkl
```

## Run Locally

1.  Clone the repository:

    ``` bash
    git clone https://github.com/Mohd-NasrullahSidd1137/Food-Delivery-Time-Prediction.git
    ```

2.  Open the project directory:

    ``` bash
    cd Food-Delivery-Time-Prediction
    ```

3.  Create and activate a virtual environment (recommended):

    ``` bash
    python -m venv venv
    ```

    On Windows:

    ``` bash
    venv\Scripts\activate
    ```

4.  Install dependencies:

    ``` bash
    pip install -r requirements.txt
    ```

5.  Start the application:

    ``` bash
    streamlit run app.py
    ```

Ensure `requirements.txt`, `app.py`, and the saved model file are
present in the repository, and that the model path in `app.py` matches
the actual location of the model.

## Future Improvements

-   Add model performance metrics and model comparison visuals to the
    report.
-   Monitor prediction errors using new delivery records.
-   Add more operational KPIs and drill-through analysis.
-   Retrain and validate the model as new data becomes available.

## Author

**Mohd Nasrullah Siddiqui**

-   GitHub:
    [Mohd-NasrullahSidd1137](https://github.com/Mohd-NasrullahSidd1137)
-   Project Repository: [Food Delivery Time
    Prediction](https://github.com/Mohd-NasrullahSidd1137/Food-Delivery-Time-Prediction)
-   Live Demo: [Food Delivery
    AI](https://food-delivery-ai-nasrullah.streamlit.app/)

------------------------------------------------------------------------

If you find this project useful, explore the repository and share your
feedback.
