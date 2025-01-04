<<<<<<< HEAD
import streamlit as st
import math
import pickle

# Load the model
with open("model (3).pkl", 'rb') as f:
    model = pickle.load(f)

st.header("Loan Amount Prediction !!")

# Input fields
col1, col2 = st.columns(2)
with col1:
    person_age = st.number_input("Age of the person", min_value=18, max_value=100, value=30)
with col2:
    person_gender = st.selectbox("Gender of the person", ("Male", "Female"))

col3, col4 = st.columns(2)
with col3:
    person_education = st.selectbox("Highest education level", 
                                    ("High School", "Bachelor", "Associate", "Master", "Doctorate"))
with col4:
    person_income = st.number_input("Annual income", min_value=0.0, step=1000.0)

col5, col6 = st.columns(2)
with col5:
    person_emp_exp = st.number_input("Years of employment experience", min_value=0, max_value=50)
with col6: 
    person_home_ownership = st.selectbox("Home ownership status", 
                                         ("RENT", "MORTGAGE", "OWN", "OTHER"))

col7, col8 = st.columns(2)
with col7:
    loan_intent = st.selectbox("Purpose of the loan", 
                               ("EDUCATION", "MEDICAL", "VENTURE", "PERSONAL", 
                                "DEBTCONSOLIDATION", "HOMEIMPROVEMENT"))
with col8:
    loan_int_rate = st.slider("Loan interest rate (range: 5.42 - 20)", 5.42, 20.0, 10.0)

col9, col10 = st.columns(2)
with col9:
    loan_percent_income = st.number_input("Loan amount as a percentage of annual income", min_value=0.0, max_value=0.66, step=0.01)
with col10:
    cb_person_cred_hist_length = st.number_input("Length of credit history in years", min_value=2.0, max_value=30.0, step=1.0)

col11, col12 = st.columns(2)
with col11:
    credit_score = st.number_input("Credit score of the person", min_value=300, max_value=850)
with col12:
    previous_loan_defaults_on_file = st.selectbox("Indicator of previous loan defaults", ("No", "Yes"))

# Map categorical inputs to numerical
gender_map = {'Male': 1, 'Female': 0}
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
    loan_intent,
    loan_int_rate,
    loan_percent_income,
    cb_person_cred_hist_length,
    credit_score,
    previous_loan_defaults_on_file
]

# Predict button
if st.button("Predict Loan Amount"):
    prediction = model.predict([input_data])
    st.success(f"The predicted loan amount is ${prediction[0]:,.2f}")
=======
import streamlit as st
import math
import pickle

# Load the model
with open("model (3).pkl", 'rb') as f:
    model = pickle.load(f)

st.header("Loan Amount Prediction !!")

# Input fields
col1, col2 = st.columns(2)
with col1:
    person_age = st.number_input("Age of the person", min_value=18, max_value=100, value=30)
with col2:
    person_gender = st.selectbox("Gender of the person", ("Male", "Female"))

col3, col4 = st.columns(2)
with col3:
    person_education = st.selectbox("Highest education level", 
                                    ("High School", "Bachelor", "Associate", "Master", "Doctorate"))
with col4:
    person_income = st.number_input("Annual income", min_value=0.0, step=1000.0)

col5, col6 = st.columns(2)
with col5:
    person_emp_exp = st.number_input("Years of employment experience", min_value=0, max_value=50)
with col6: 
    person_home_ownership = st.selectbox("Home ownership status", 
                                         ("RENT", "MORTGAGE", "OWN", "OTHER"))

col7, col8 = st.columns(2)
with col7:
    loan_intent = st.selectbox("Purpose of the loan", 
                               ("EDUCATION", "MEDICAL", "VENTURE", "PERSONAL", 
                                "DEBTCONSOLIDATION", "HOMEIMPROVEMENT"))
with col8:
    loan_int_rate = st.slider("Loan interest rate (range: 5.42 - 20)", 5.42, 20.0, 10.0)

col9, col10 = st.columns(2)
with col9:
    loan_percent_income = st.number_input("Loan amount as a percentage of annual income", min_value=0.0, max_value=0.66, step=0.01)
with col10:
    cb_person_cred_hist_length = st.number_input("Length of credit history in years", min_value=2.0, max_value=30.0, step=1.0)

col11, col12 = st.columns(2)
with col11:
    credit_score = st.number_input("Credit score of the person", min_value=300, max_value=850)
with col12:
    previous_loan_defaults_on_file = st.selectbox("Indicator of previous loan defaults", ("No", "Yes"))

# Map categorical inputs to numerical
gender_map = {'Male': 1, 'Female': 0}
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
    loan_intent,
    loan_int_rate,
    loan_percent_income,
    cb_person_cred_hist_length,
    credit_score,
    previous_loan_defaults_on_file
]

# Predict button
if st.button("Predict Loan Amount"):
    prediction = model.predict([input_data])
    st.success(f"The predicted loan amount is ${prediction[0]:,.2f}")
>>>>>>> 1f2e7330fa3467bc24e47ca05d4f88d11ad77a5e
