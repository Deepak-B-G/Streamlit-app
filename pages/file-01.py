import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import time

# st.set_page_config(page_title="Page 1", page_icon="📄")


st.title("Streamlit Data Visualization & Loading")

# ✅ 1️⃣ Always Show Matplotlib Graph (Independent)
st.header("📊 Matplotlib Graph")
x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig)

# ✅ 2️⃣ Always Show Sorted Data Table (Independent)
st.header("📋 Sorted Data Table")
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Score": [90, 85, 88]
}
df = pd.DataFrame(data)
df_sorted = df.sort_values(by="Score", ascending=False)

st.dataframe(df_sorted)

# ✅ 3️⃣ Load Uber Data ONLY When Button is Clicked
st.header("🚖 Load Uber Data")
DATE_COLUMN = 'date/time'
DATA_URL = 'https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz'

@st.cache_resource
def load_data(nrows: int) -> pd.DataFrame:
    data = pd.read_csv(DATA_URL, nrows=nrows)
    data.rename(lambda x: str(x).lower(), axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

num = st.number_input("Enter number of Uber rows to load:", min_value=1, max_value=100, step=1, format="%d")
if st.button("Load Uber Data"):
    with st.spinner("Loading Uber Data..."):
        time.sleep(1)  # Simulating a delay
        data = load_data(num)
        st.write(data)
        st.success("Uber Data Loaded Successfully! ✅")

# ✅ 4️⃣ Always Show Plotly Chart (Independent)
st.header("📈 Plotly Chart")
df = px.data.iris()
st.write(df)

fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")  # ✅ Fixed color column
st.plotly_chart(fig)



st.title("Progress Bar Example")

# Create a number input
num = st.number_input("Enter a number:", min_value=1, max_value=100, step=1, value=10)

# Button to trigger loading
if st.button("Load Data"):
    progress_bar = st.progress(10)  # Initialize the progress bar

    for percent in range(1, 101):
        time.sleep(0.02)  # Simulating loading time
        progress_bar.progress(percent)  # Update the progress bar

    st.success("Data Loaded Successfully! ✅")


add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)


add_radio= st.sidebar.radio(
    "What is the option?",
    ("Option 1","Option 2","Option 3")
)

add_multiselect= st.sidebar.multiselect(
    "What is the option?",
    ("Option 1","Option 2","Option 3")
)

st.sidebar.write(f"Options choosen are {add_selectbox} and {add_radio} and {add_multiselect}")
st.write(f"Options choosen are {add_selectbox} and {add_radio} and {add_multiselect}")



col1, col2 = st.columns(2)
with col1:
    if st.button('Button 1'):
        st.write("Button 1 is Clicked")
with col2:
    if st.button('Button 2'):
        st.write("Button 2 is Clicked")
