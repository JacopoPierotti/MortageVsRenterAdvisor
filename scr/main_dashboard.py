import streamlit as st
from scr.preprocess import preprocess
from scr.table import table

st.title("Main Dashboard")

financial_inputs = preprocess()
table(financial_inputs)
