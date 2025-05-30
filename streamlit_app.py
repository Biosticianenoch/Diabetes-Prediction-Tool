import streamlit as st
import pickle

st.title('Diabetes Prediction Tool')

st.write('This tool is designed to make real world prediction of Diabetes Outcomes in Real world settings')

# Load saved models
diabetes_model = pickle.load(open(diabetes_model.sav"), 'rb')
