import streamlit as st
import pickle

st.title('Diabetes Prediction Tool')

st.write('This tool is designed to make real world prediction of Diabetes Outcomes in Real world settings')

# Load saved models
diabetes_model = pickle.load(open(diabetes_model.sav"), 'rb')

col1, col2, col3 = st.columns(3)

with col1:
    pregnancies = st.number_input("Number of Pregnancies", min_value=0)
with col2:
    glucose = st.number_input("Glucose Level")
with col3:
    blood_pressure = st.number_input("Blood Pressure value")

with col1:
    skin_thickness = st.number_input("Skin Thickness value")
with col2:
    insulin = st.number_input("Insulin Level")
with col3:
    bmi = st.number_input("BMI value")

with col1:
    diabetes_pedigree = st.number_input("Diabetes Pedigree Function value")
with col2:
    age = st.number_input("Age of the Person", min_value=1)

                             
