import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.express as px
from tensorflow.keras.models import load_model

# Load model and scaler
model = load_model("model.h5")
scaler = pickle.load(open("scaler.pkl","rb"))

# Load dataset
df = pd.read_csv("Churn_Modelling.csv")

st.title("🏦 AI Customer Churn Analytics Dashboard")

st.sidebar.header("Navigation")

page = st.sidebar.radio("Go to",["Dashboard","Predict Churn"])

# ---------------- DASHBOARD ----------------

if page == "Dashboard":

    st.subheader("📊 Churn Overview")

    churn_rate = df["Exited"].mean()*100
    total_customers = len(df)

    col1,col2 = st.columns(2)

    col1.metric("Total Customers", total_customers)
    col2.metric("Churn Rate", f"{churn_rate:.2f}%")

    # Churn by country
    st.subheader("🌍 Churn by Country")

    country_chart = px.histogram(
        df,
        x="Geography",
        color="Exited",
        barmode="group"
    )

    st.plotly_chart(country_chart)

    # Churn by gender
    st.subheader("👥 Churn by Gender")

    gender_chart = px.histogram(
        df,
        x="Gender",
        color="Exited",
        barmode="group"
    )

    st.plotly_chart(gender_chart)

    # Age distribution
    st.subheader("📈 Age vs Churn")

    age_chart = px.histogram(
        df,
        x="Age",
        color="Exited",
        nbins=40
    )

    st.plotly_chart(age_chart)

    # Balance scatter
    st.subheader("💰 Balance vs Age")

    scatter = px.scatter(
        df,
        x="Age",
        y="Balance",
        color="Exited"
    )

    st.plotly_chart(scatter)

# ---------------- PREDICTION ----------------

if page == "Predict Churn":

    st.subheader("🔮 Predict Customer Churn")

    credit_score = st.number_input("Credit Score",350,900,600)
    gender = st.selectbox("Gender",["Male","Female"])
    age = st.slider("Age",18,100,35)
    tenure = st.slider("Tenure",0,10,3)
    balance = st.number_input("Balance",0.0,250000.0,60000.0)
    products = st.selectbox("Products",[1,2,3,4])
    credit_card = st.selectbox("Has Credit Card",[0,1])
    active = st.selectbox("Is Active Member",[0,1])
    salary = st.number_input("Estimated Salary",0.0,200000.0,50000.0)
    geo = st.selectbox("Country",["France","Germany","Spain"])

    gender = 1 if gender=="Male" else 0

    geo_germany = 1 if geo=="Germany" else 0
    geo_spain = 1 if geo=="Spain" else 0

    input_data = np.array([[

    credit_score,
    gender,
    age,
    tenure,
    balance,
    products,
    credit_card,
    active,
    salary,
    geo_germany,
    geo_spain

    ]])

    input_data = scaler.transform(input_data)

    if st.button("Predict"):

        prediction = model.predict(input_data)[0][0]

        st.subheader(f"Churn Probability: {prediction:.2f}")

        if prediction > 0.7:
            st.error("⚠️ High Risk Customer")
        elif prediction > 0.4:
            st.warning("⚠️ Medium Risk")
        else:
            st.success("✅ Customer likely to stay")