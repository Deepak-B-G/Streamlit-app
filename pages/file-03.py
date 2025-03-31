import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Sample

st.set_page_config(page_title="Snowflake Integration", page_icon="snow",layout="wide")

SNOWFLAKE_URL = (
    "snowflake://Deepak:GDGkde8G9hUUrSW@KABRHSH-ZR75202/MY_DATABASE/MY_SCHEMA?"
    "warehouse=COMPUTE_WH"
)

@st.cache_data
def get_data():
    engine = create_engine(SNOWFLAKE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying with ORM
    data = session.query(Sample).all()
    
    # Convert ORM objects to DataFrame
    df = pd.DataFrame(
        [{col.name: getattr(row, col.name) for col in Sample.__table__.columns} for row in data]
    )

    session.close()
    return df

st.title("This is the use of another table")

if st.button("Load Data"):
    st.markdown("Load the data from the sample data")
    df = get_data()
    st.dataframe(df) 
