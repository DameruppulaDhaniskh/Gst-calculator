import streamlit as st
st.title("Retired Pension")
age=st.number_input("Enter age of employee")
salary=st.number_input("Enter salary before retirement")
if age<70:
    pension=salary*0.5
elif age<80:
    pension=salary*0.35
elif age>80:
    pension=salary*0.25
if age<60:
    st.write("Not eligible for retirement")
else:
    st.write("Eligible")

st.write(f"Pension is {pension}")





