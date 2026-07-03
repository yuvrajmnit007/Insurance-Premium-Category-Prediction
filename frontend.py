import streamlit as st
import requests

API_URL = "https://insurance-premium-category-prediction-1.onrender.com" 

st.title("Insurance Premium Category Predictor")
st.markdown("Enter your details below:")

# Input fields
age = st.number_input("Age", min_value=1, max_value=119, value=30)
weight = st.number_input("Weight (kg)", min_value=1.0, value=65.0)
height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.7)
income_lpa = st.number_input("Annual Income (LPA)", min_value=0.1, value=10.0)
smoker = st.selectbox("Are you a smoker?", options=[True, False])
city = st.text_input("City", value="Mumbai")
occupation = st.selectbox(
    "Occupation",
    ['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job']
)

if st.button("Predict Premium Category"):

    payload = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation,
    }

    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:

            result = response.json()

            prediction = result["response"]["predicted_category"]
            confidence = result["response"]["confidence"]
            probabilities = result["response"]["class_probabilities"]

            st.success(f"Predicted Premium Category: **{prediction}**")

            st.metric(
                label="Confidence",
                value=confidence
            )

            st.subheader("Class Probabilities")

            for cls, prob in probabilities.items():
                st.progress(float(prob[:-1]) / 100)
                st.write(f"**{cls} : {prob}**")

        else:
            st.error(response.text)

    except requests.exceptions.ConnectionError:
        st.error("Could not connect to FastAPI server.")