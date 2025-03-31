import streamlit as st
import datetime 


@st.cache_resource
def now():
    return datetime.datetime.now()


if st.button("Show time"):
    st.write(now())
    st.write(datetime.datetime.now())

# Initialize session state
if "count" not in st.session_state:
    st.session_state.count = 0

def increment():
    st.session_state.count += 1

st.button("Increment", on_click=increment)
st.write(f"Count: {st.session_state.count}")


def submit_form():
    st.session_state.submitted = True

if "submitted" not in st.session_state:
    st.session_state.submitted = False

with st.form("my_form"):
    st.text_input("Enter your name:")
    st.form_submit_button("Submit", on_click=submit_form)

if st.session_state.submitted:
    st.toast("Form submitted successfully!")


import pandas as pd
from pathlib import Path  # ✅ Import pathlib

FILE_PATH = Path("data.csv")  # ✅ Convert string to Path object

def save_to_csv(name, email):
    df = pd.DataFrame([[name, email]], columns=["Name", "Email"])
    
    # ✅ Use FILE_PATH.exists() correctly
    df.to_csv(FILE_PATH, mode="a", header=not FILE_PATH.exists(), index=False)
    
    st.success("Data Saved!")

st.title("User Registration")

with st.form("user_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    submitted = st.form_submit_button("Submit")

if submitted:
    save_to_csv(name, email)



import streamlit as stm 
from streamlit_extras.buy_me_a_coffee import button 

stm.title("This is the Home Page Geeks.") 
stm.text("Geeks Home Page") 

button(username="Geeks", floating=False, width=250)
