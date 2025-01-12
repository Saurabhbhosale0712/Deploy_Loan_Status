
import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load the model
with open("model.pkl", 'rb') as f:
    model = pickle.load(f)

st.header("Loan Status Prediction 💰💹")

# Input fields
col1, col2 = st.columns(2)
with col1:
    person_age = st.number_input("Age of the person", min_value=18, max_value=100, value=30)
with col2:
    person_gender = st.selectbox("Gender of the person", ("Male", "Female"))

col3, col4 = st.columns(2)
with col3:
    person_education = st.selectbox("Highest education level ", 
                                    ("High School", "Associate", "Bachelor", "Master", "Doctorate"))
with col4:
    person_income = st.number_input("Annual income (12.5%)", min_value=0.0)

# Condition 4: Highlight annual income check
if person_income < 30000:
    st.warning("Note: Annual income is above the threshold of 30,000 for loan approval.")

col5, col6 = st.columns(2)
with col5:
    person_emp_exp = st.number_input("Years of employment experience", min_value=0, max_value=50)
with col6:
    person_home_ownership = st.selectbox("Home ownership status (6.9%)", 
                                         ("RENT", "MORTGAGE", "OWN", "OTHER"))

# Condition 5: Highlight home ownership check
if person_home_ownership not in ["OWN", "MORTGAGE"]:
    st.warning("Note: Homeownership status may reduce the chances of loan approval.")

col7 = st.columns(1)[0]  # Corrected typo in the column call
with col7:
    loan_amnt = st.number_input("Loan amount requested (5.9%)")


col8, col9 = st.columns(2)
with col8:
    loan_intent = st.selectbox("Purpose of the loan", 
                               ("EDUCATION", "MEDICAL", "VENTURE", "PERSONAL", 
                                "DEBTCONSOLIDATION", "HOMEIMPROVEMENT"))
with col9:
    loan_int_rate = st.number_input("Loan interest rate (15.8%)", min_value=5.42, max_value=20.00)

# Condition 3: Highlight interest rate check
if loan_int_rate < 10.0:
    st.warning("Note: Loan interest rate is above the threshold of 10% for improve the chance approval.")

col10, col11 = st.columns(2)
with col10:
    if person_income > 0:  # Prevent division by zero
        loan_percent_income = loan_amnt / person_income  # Calculate loan amount as a percentage of income
    else:
        loan_percent_income = 0  # Set to 0 if income is 0 to avoid division by zero
    
    st.write(f"Loan amount as a percentage of income Calculated (16.5%): {loan_percent_income * 100:.2f}%")

# Condition 2: Highlight loan percent income check
if loan_percent_income > 0.4:
    st.warning("Note: Loan amount exceeds 40% of income, which may result in rejection.")

with col11:
    cb_person_cred_hist_length = st.number_input("Length of credit history in years", min_value=2, max_value=30, step=1)

col12, col13 = st.columns(2)
with col12:
    credit_score = st.number_input("Credit score of the person (5.6%)", min_value=300, max_value=950)

# Condition 6: Highlight credit score check
if credit_score < 600:
    st.warning("Note: Credit score is below 600, which reduces the chances of loan approval.")

with col13:
    previous_loan_defaults_on_file = st.selectbox("Indicator of previous loan defaults (22.6%)", ("No", "Yes"))

# Condition 1: Highlight previous loan defaults check
if previous_loan_defaults_on_file == "Yes":
    st.warning("Note: Previous loan defaults detected, which may result in rejection.")

# Map categorical inputs to numerical
gender_map = {'Male': 1, 'Female': 0}  # Fixed case sensitivity in keys
education_map = {"High School": 0, "Associate": 1, "Bachelor": 2, "Master": 3, "Doctorate": 4}
home_ownership_map = {"RENT": 0, "MORTGAGE": 1, "OWN": 2, "OTHER": 3}
loan_intent_map = {"EDUCATION": 0, "MEDICAL": 1, "VENTURE": 2, "PERSONAL": 3, "DEBTCONSOLIDATION": 4, "HOMEIMPROVEMENT": 5}
previous_default_map = {"No": 0, "Yes": 1}

person_gender = gender_map[person_gender]
person_education = education_map[person_education]
person_home_ownership = home_ownership_map[person_home_ownership]
loan_intent = loan_intent_map[loan_intent]
previous_loan_defaults_on_file = previous_default_map[previous_loan_defaults_on_file]

# Create input array for prediction
input_data = [
    person_age,
    person_gender,
    person_education,
    person_income,
    person_emp_exp,
    person_home_ownership,
    loan_amnt,
    loan_intent,
    loan_int_rate,
    loan_percent_income,
    cb_person_cred_hist_length,
    credit_score,
    previous_loan_defaults_on_file
]

# Predict button
if st.button("Classify Loan Status"):
    # Make prediction
    prediction = model.predict([input_data])

    # Display result
    loan_status = "Approved 😊" if prediction[0] == 1 else "Rejected 😔"
    st.success(f"Loan Status: {loan_status}")
