from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class SalesData(Base):
    __tablename__ = "SALES_DATA"  # Match with Snowflake table name
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date)
    category = Column(String)
    product = Column(String)
    quantity_sold = Column(Integer)
    sales_amount = Column(Float)

class Sample(Base):
    __tablename__ = "MY_TABLE"
    id = Column(Integer, primary_key=True, autoincrement=False)  # Ensure it matches Snowflake's definition
    name = Column(String)  # VARCHAR
    age = Column(Integer)  # NUMBER
    city = Column(String)  # VARCHAR