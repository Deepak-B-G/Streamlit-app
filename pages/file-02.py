import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import SalesData

st.set_page_config(page_title="Snowflake Integration", page_icon="random")

# ✅ Snowflake Connection URL (SQLAlchemy)
SNOWFLAKE_URL = (
    "snowflake://Deepak:GDGkde8G9hUUrSW@KABRHSH-ZR75202/MY_DATABASE/MY_SCHEMA?"
    "warehouse=COMPUTE_WH"
)

# ✅ Function to Fetch Data Using ORM
@st.cache_data
def get_sales_data():
    engine = create_engine(SNOWFLAKE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying with ORM
    data = session.query(SalesData).all()
    
    # Convert ORM objects to DataFrame
    df = pd.DataFrame(
        [{col.name: getattr(row, col.name) for col in SalesData.__table__.columns} for row in data]
    )

    session.close()
    return df

# ✅ Streamlit UI
st.title("📊 Sales Data Visualization (Snowflake)")

st.markdown("⏳ Fetching data from Snowflake using ORM...")
df = get_sales_data()
st.dataframe(df)
st.success("✅ Data Loaded Successfully!")

# 📊 Sales Over Time (Line Chart)

with st.expander("Line Chart"):
    st.subheader("📈 Sales Over Time")
    fig1 = px.line(df, x="date", y="sales_amount", title="Sales Trend", markers=True)
    st.plotly_chart(fig1)

# 📊 Category-wise Sales (Bar Chart)
st.subheader("📊 Category-wise Sales")
fig2 = px.bar(df, x="category", y="sales_amount", color="category", title="Sales by Category")
st.plotly_chart(fig2)

# 📊 Quantity Sold Per Product (Pie Chart)
st.subheader("📦 Quantity Sold Per Product")
fig3 = px.pie(df, names="product", values="quantity_sold", title="Quantity Distribution")
st.plotly_chart(fig3)
