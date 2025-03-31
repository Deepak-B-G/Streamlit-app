import streamlit as st
import pandas as pd
import numpy as np


if "counter" not in st.session_state:
    st.session_state.counter = 0

def increment():
    st.session_state.counter += 1

st.button("Increment", on_click=increment)
st.write("Counter:", st.session_state.counter)


@st.cache_data
def load_data():
    # Load data from an Excel file
    df = pd.read_excel("C:/Users/WL225DT/OneDrive - EY/Desktop/new_template_ready.xlsm", engine='openpyxl',sheet_name = "input_template")
    return df

# Load the data
df = load_data()

# Display the dataframe in the Streamlit app
st.dataframe(df)


chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data)


df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=["lat", "lon"],
)
st.map(df)


@st.dialog("Cast your vote")
def vote(item):
    st.write(f"Why is {item} your favorite?")
    reason = st.text_input("Because...")
    if st.button("Submit"):
        st.session_state.vote = {"item": item, "reason": reason}
        st.rerun()

if "vote" not in st.session_state:
    st.write("Vote for your favorite")
    if st.button("A"):
        vote("A")
    if st.button("B"):
        vote("B")
else:
    f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"