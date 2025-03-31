import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import runpy  

st.set_page_config(
    page_title="My App",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}  # ✅ Hides the default sidebar menu
)
# Snowflake connection URL
SNOWFLAKE_URL = (
    "snowflake://Deepak:GDGkde8G9hUUrSW@KABRHSH-ZR75202/MY_DATABASE/MY_SCHEMA?warehouse=COMPUTE_WH"
)

# Create SQLAlchemy engine
engine = create_engine(SNOWFLAKE_URL)

# Function to check credentials
def check_credentials(username, password):
    query = f"SELECT password_hash FROM users WHERE username = '{username}'"
    
    with engine.connect() as conn:
        result = pd.read_sql(query, conn)
    
    if result.empty:
        return False  # User not found
    
    stored_password = result.iloc[0]['password_hash']
    return password == stored_password  # Direct comparison since passwords are not hashed

# Streamlit UI
st.title("Login Page")

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "page" not in st.session_state:
    st.session_state.page = "login"  # Default page

if st.session_state.page == "login":
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if check_credentials(username, password):
            st.session_state.authenticated = True
            st.session_state.page = "home"  # Redirect after login
            st.success("Login successful! Redirecting...")
            st.rerun()
        else:
            st.error("Invalid username or password")

elif st.session_state.authenticated:
    st.title("Welcome to the App!")

    # ✅ Align buttons in two rows
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("File-01"):
            st.session_state.page = "file-01"
            st.rerun()
        if st.button("File-04"):
            st.session_state.page = "file-04"
            st.rerun()
    
    with col2:
        if st.button("File-02"):
            st.session_state.page = "file-02"
            st.rerun()
        if st.button("File-05"):
            st.session_state.page = "file-05"
            st.rerun()
    
    with col3:
        if st.button("File-03"):
            st.session_state.page = "file-03"
            st.rerun()
        if st.button("File-06"):
            st.session_state.page = "file-06"
            st.rerun()

    st.sidebar.button("Logout", on_click=lambda: st.session_state.update({"authenticated": False, "page": "login"}))

# ✅ Directly show respective page when user clicks a button
if st.session_state.page == "file-01":
    st.switch_page("pages/file-01.py")
if st.session_state.page == "file-02":
    st.switch_page("pages/file-02.py")
if st.session_state.page == "file-03":
    st.switch_page("pages/file-03.py")
if st.session_state.page == "file-04":
    st.switch_page("pages/file-04.py")
if st.session_state.page == "file-05":
    st.switch_page("pages/file-05.py")
if st.session_state.page == "file-06":
    st.switch_page("pages/_file-06.py") 

