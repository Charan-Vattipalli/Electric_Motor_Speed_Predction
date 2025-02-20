import streamlit as st
import pickle
import pandas as pd

# Load the trained ML model
MODEL_PATH = "C:/Users/Bobby/DS_Basha/Projects/EMS_project/updated/decision_tree_model.pkl"

try:
    with open(MODEL_PATH, "rb") as file:
        model = pickle.load(file)
    st.success("✅ Model loaded successfully!")
except Exception as e:
    st.error(f"❌ Error loading model: {e}")

# Streamlit Web App UI
st.title("Motor Speed Prediction App 🚀")

# Create input fields for user entry
ambient = st.number_input("Enter ambient:")
coolant = st.number_input("Enter coolant:")
u_d = st.number_input("Enter u_d:")
u_q = st.number_input("Enter u_q:")
torque = st.number_input("Enter torque:")
i_d = st.number_input("Enter i_d:")
i_q = st.number_input("Enter i_q:")
pm = st.number_input("Enter pm:")
stator_yoke = st.number_input("Enter stator_yoke:")
stator_tooth = st.number_input("Enter stator_tooth:")
stator_winding = st.number_input("Enter stator_winding:")

# Predict button
if st.button("Predict"):
    input_data = pd.DataFrame([[ambient, coolant, u_d,u_q,torque,i_d,i_q,pm,stator_yoke,stator_tooth,stator_winding]], columns=["ambient", "coolant", "u_d","u_q","torque","i_d","i_q","pm","stator_yoke","stator_tooth","stator_winding"])
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Motor Speed: {int(prediction)} RPM ")
