import pandas as pd
import streamlit as st


@st.cache_data
def load_from_url(url):
    return pd.read_csv(url)