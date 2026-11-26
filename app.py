
import streamlit as st
import pandas as pd
import numpy as np
import joblib
from pathlib import Path

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Food Delivery AI | Prediction",
    page_icon="🍔",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. CUSTOM CSS
# ==========================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #0B1120 0%, #111C30 55%, #17243A 100%);
    color: #F8FAFC;
}

[data-testid="stSidebar"] {
    background: #0A1324;
    border-right: 1px solid #26354B;
}

[data-testid="stSidebar"] * {
    color: #E2E8F0;
}

.main-title {
    font-size: 38px;
    font-weight: 800;
    color: #FFFFFF;
    letter-spacing: -1px;
}

.gradient-text {
    background: linear-gradient(90deg, #FF8A35, #FFB347);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    color: #A9B8CA;
    font-size: 14px;
    margin-bottom: 25px;
}

.section-title {
    color: #FFFFFF;
    font-size: 21px;
    font-weight: 600;
    margin-bottom: 12px;
}

.info-card {
    background: linear-gradient(135deg, #172943, #1C304B);
    padding: 22px;
    border: 1px solid #30445E;
    border-radius: 15px;
    margin-bottom: 15px;
}

.info-label {
    font-size: 12px;
    color: #A9B8CA;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.info-value {
    font-size: 23px;
    font-weight: 700;
    color: #FFFFFF;
    margin-top: 7px;
}

.result-card {
    background: linear-gradient(135deg, #1B3550, #203C55);
    border: 1px solid #FF923D;
    border-radius: 20px;
    padding: 30px;
    text-align: center;
    margin-top: 25px;
}

.result-label {
    color: #C4D3E4;
    font-size: 14px;
}

.result-number {
    font-size: 52px;
    font-weight: 800;
    color: #FF9A45;
    margin: 8px 0;
}

.result-unit {
    color: #E2E8F0;
    font-size: 15px;
}

div.stButton > button,
div[data-testid="stFormSubmitButton"] > button {
    background: linear-gradient(90deg, #F97316, #FB923C);
    color: white;
    border: none;
    border-radius: 10px;
    height: 48px;
    font-weight: 700;
    font-size: 15px;
    width: 100%;
    transition: 0.3s;
}

div.stButton > button:hover,
div[data-testid="stFormSubmitButton"] > button:hover {
    background: linear-gradient(90deg, #EA580C, #F97316);
    color: white;
    border: none;
    transform: translateY(-2px);
}

.stTextInput input,
.stNumberInput input {
    background-color: #192B41;
    color: white;
}

div[data-baseweb="select"] > div {
    background-color: #192B41;
    border-color: #344A63;
}

hr {
    border-color: #30445E;
}

footer {
    visibility: hidden;
}

#MainMenu {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# 3. LOAD MACHINE LEARNING MODEL
# ==========================================

from pathlib import Path
import joblib

BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = (
    BASE_DIR
    / "notebook"
    / "models"
    / "food_delivery_prediction_model.pkl"
)

print("Model Path:", MODEL_PATH)
print("Model Exists:", MODEL_PATH.exists())

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

try:
    model = load_model()
    model_loaded = True
    print("Model Loaded Successfully!")

except Exception as e:
    model = None
    model_loaded = False
    print("Model Loading Error:", e)


# ==========================================
# 4. SIDEBAR
# ==========================================

with st.sidebar:

    st.markdown("""
    <div style="text-align:center; padding:15px 0;">
        <div style="font-size:55px;">🍔</div>
        <h2 style="color:#FF963F;">Food Delivery AI</h2>
        <p style="color:#94A3B8; font-size:12px;">
            INTELLIGENT DELIVERY PREDICTION
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown("### Navigation")

    page = st.radio(
        "Select Page",
        ["🏠 Home", "🔮 Delivery Prediction", "ℹ️ About Project"],
        label_visibility="collapsed"
    )

    st.divider()

    st.markdown("### Technology Stack")

    st.markdown("""
    - 🐍 Python
    - 🐼 Pandas & NumPy
    - 🤖 Scikit-learn
    - 📊 Machine Learning
    - ⚡ Streamlit
    """)

    st.divider()

    if model_loaded:
        st.success("ML Model Loaded")
    else:
        st.error("Model Not Found")

    st.markdown("""
    <div style="font-size:11px; color:#8294AA; text-align:center;">
        FOOD DELIVERY AI<br>
        Machine Learning Project
    </div>
    """, unsafe_allow_html=True)



# ==========================================
# 5. HOME PAGE
# ==========================================

if page == "🏠 Home":

    st.markdown("""
    <div class="main-title">
        Smart Food Delivery <span class="gradient-text">Prediction</span>
    </div>

    <div class="subtitle">
        Predict delivery duration intelligently using Machine Learning.
        Make smarter delivery time estimates.
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1.5, 1])

    with col1:

        st.html("""
        <div class="info-card">
            <h2 style="color:white;">
                Welcome to Food Delivery AI 🚀
            </h2>

            <p style="color:#B8C7D9; line-height:1.9;">
                This application uses a trained Machine Learning
                model to estimate food delivery duration based on
                distance, weather, traffic, vehicle type,
                preparation time and courier experience.
            </p>

            <p style="color:#FF9A45; font-weight:600;">
                Smart Inputs. Intelligent Predictions.
            </p>
        </div>
        """)

        if st.button("Start Delivery Prediction →"):
            st.session_state["page"] = "🔮 Delivery Prediction"
            st.rerun()

    with col2:

        st.html("""
        <div class="info-card" style="text-align:center; padding:35px 15px;">
            <div style="font-size:90px;">🛵</div>
            <h3 style="color:#FFFFFF;">Fast & Smart</h3>
            <p style="color:#A9B8CA;">
                ML-powered delivery time estimation
            </p>
        </div>
        """)

    st.markdown("---")

    st.html("""
    <div class="section-title">
        Application Features
    </div>
    """)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.html("""
        <div class="info-card">
            <h2>📍</h2>
            <h4>Distance Analysis</h4>
            <p style="color:#A9B8CA;">
                Analyze delivery distance and its impact.
            </p>
        </div>
        """)

    with c2:
        st.html("""
        <div class="info-card">
            <h2>🌦️</h2>
            <h4>Weather & Traffic</h4>
            <p style="color:#A9B8CA;">
                Consider external delivery conditions.
            </p>
        </div>
        """)

    with c3:
        st.html("""
        <div class="info-card">
            <h2>🤖</h2>
            <h4>ML Prediction</h4>
            <p style="color:#A9B8CA;">
                Generate estimated delivery duration.
            </p>
        </div>
        """)


# ==========================================
# 6. DELIVERY PREDICTION PAGE
# ==========================================

elif page == "🔮 Delivery Prediction":

    st.markdown("""
    <div class="main-title">
        Delivery <span class="gradient-text">Prediction</span>
    </div>

    <div class="subtitle">
        Enter delivery details below to estimate the delivery time.
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">📦 Delivery Information</div>',
        unsafe_allow_html=True
    )

    with st.form("prediction_form"):

        col1, col2 = st.columns(2)

        with col1:

            st.markdown("#### 📍 Delivery Details")

            distance = st.number_input(
                "Delivery Distance (KM)",
                min_value=0.59,
                max_value=19.99,
                value=5.0,
                step=0.1
            )

            weather = st.selectbox(
                "Weather Conditions",
                ["Clear", "Windy", "Foggy", "Rainy", "Snowy"]
            )

            traffic = st.selectbox(
                "Traffic Level",
                ["Low", "Medium", "High"]
            )

            time_of_day = st.selectbox(
                "Time of Day",
                ["Morning", "Afternoon", "Evening", "Night"]
            )

        with col2:

            st.markdown("#### 🛵 Courier Information")

            vehicle = st.selectbox(
                "Vehicle Type",
                ["Bike", "Scooter", "Car"]
            )

            preparation = st.number_input(
                "Preparation Time (Minutes)",
                min_value=5,
                max_value=29,
                value=15
            )

            experience = st.number_input(
                "Courier Experience (Years)",
                min_value=0.0,
                max_value=9.0,
                value=2.0,
                step=0.5
            )

        st.markdown("---")

        submitted = st.form_submit_button(
            "🚀 Predict Delivery Time",
            use_container_width=True
        )


   

    # ======================================
    # 7. PREDICTION RESULT
    # ======================================

    if submitted:

        if not model_loaded:
            st.error(
                "Model file could not be loaded. "
                "Please check your models folder."
            )

        else:

            input_data = pd.DataFrame({
                "Distance_km": [distance],
                "Weather": [weather],
                "Traffic_Level": [traffic],
                "Time_of_Day": [time_of_day],
                "Vehicle_Type": [vehicle],
                "Preparation_Time_min": [preparation],
                "Courier_Experience_yrs": [experience]
            })

            try:
                prediction = float(model.predict(input_data)[0])
                prediction = max(0.0, prediction)

                # Prediction Result Card
                st.html(f"""
                <div style="
                    background: linear-gradient(135deg, #172F49, #203E59);
                    border: 1px solid #FF963F;
                    border-radius: 20px;
                    padding: 35px 20px;
                    text-align: center;
                    margin-top: 25px;
                    box-shadow: 0 8px 25px rgba(0,0,0,0.25);
                ">
                    <div style="
                        color: #FFFFFF;
                        font-size: 15px;
                        font-weight: 600;
                        letter-spacing: 2px;
                    ">
                        YOUR ESTIMATED DELIVERY TIME
                    </div>

                    <div style="
                        color: #FF963F;
                        font-size: 58px;
                        font-weight: 800;
                        margin: 15px 0 5px 0;
                    ">
                        {prediction:.1f}
                    </div>

                    <div style="
                        color: #FFFFFF;
                        font-size: 19px;
                        font-weight: 500;
                    ">
                        Minutes
                    </div>

                    <div style="
                        color: #D1DDEA;
                        font-size: 13px;
                        margin-top: 18px;
                    ">
                        Prediction generated using Machine Learning
                    </div>
                </div>
                """)

                # Delivery Summary
                st.markdown("## 📋 Delivery Summary")

                st.html("""
                <style>
                div[data-testid="stMetric"] {
                    background: linear-gradient(135deg, #172943, #203852);
                    border: 1px solid #38516D;
                    border-radius: 13px;
                    padding: 18px;
                }

                div[data-testid="stMetricLabel"] {
                    color: #E2EAF3 !important;
                    font-size: 14px !important;
                    font-weight: 600 !important;
                }

                div[data-testid="stMetricValue"] {
                    color: #FFAB62 !important;
                    font-size: 25px !important;
                    font-weight: 700 !important;
                }
                </style>
                """)

                r1, r2, r3 = st.columns(3)

                r1.metric("📍 Distance", f"{distance:.1f} KM")
                r2.metric("🚦 Traffic Level", traffic)
                r3.metric("🌦️ Weather", weather)

                r4, r5, r6 = st.columns(3)

                r4.metric("🛵 Vehicle Type", vehicle)
                r5.metric("🍳 Preparation Time", f"{preparation} min")
                r6.metric(
                    "👨‍✈️ Courier Experience",
                    f"{experience:.1f} years"
                )

                st.info(
                    "Note: This is an estimated delivery duration "
                    "generated by the Machine Learning model. "
                    "Actual delivery time may vary."
                )

            except Exception as e:
                st.error(f"Prediction failed: {e}")

# ==========================================
# 8. ABOUT PROJECT PAGE
# ==========================================

elif page == "ℹ️ About Project":

    st.markdown("""
    <div class="main-title">
        About <span class="gradient-text">Project</span>
    </div>

    <div class="subtitle">
        Understanding the technology behind Food Delivery AI.
    </div>
    """, unsafe_allow_html=True)

    # Project Overview
    st.html("""
    <div class="info-card">
        <h3 style="color:#FF963F;">Project Overview</h3>

        <p style="color:#B8C7D9; line-height:1.9;">
            Food Delivery Time Prediction is an end-to-end Machine
            Learning project designed to estimate delivery duration
            based on multiple operational and environmental factors.
        </p>
    </div>
    """)

    # Machine Learning Workflow
    st.markdown("### 🧠 Machine Learning Workflow")

    workflow = [
        "Exploratory Data Analysis",
        "Data Cleaning & Preprocessing",
        "Feature Engineering",
        "Machine Learning Model Training",
        "Model Evaluation & Selection",
        "Model Deployment with Streamlit"
    ]

    for i, step in enumerate(workflow, 1):
        st.markdown(f"**{i}.** {step}")

    st.markdown("---")

    # Technologies Used
    st.markdown("### 🛠️ Technologies Used")

    technologies = [
        "Python",
        "Pandas",
        "NumPy",
        "Matplotlib",
        "Seaborn",
        "Scikit-learn",
        "Joblib",
        "Streamlit"
    ]

    tech_cols = st.columns(4)

    for i, tech in enumerate(technologies):
        with tech_cols[i % 4]:
            st.markdown(f"**🔹 {tech}**")

    st.markdown("---")

    # Footer
    st.html("""
    <div style="
        text-align:center;
        color:#8294AA;
        padding:25px;
        font-size:14px;
    ">
        Food Delivery AI | Machine Learning Project
    </div>
    """)



# ==========================================
# 9. FOOTER
# ==========================================

st.markdown("---")

st.markdown("""
<div style="text-align:center; color:#8294AA; font-size:12px;
padding:15px;">
    FOOD DELIVERY AI · POWERED BY MACHINE LEARNING
</div>
""", unsafe_allow_html=True)
