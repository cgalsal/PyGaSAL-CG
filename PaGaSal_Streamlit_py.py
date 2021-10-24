import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pages.Visulation
import pages.Prediction
import pages.Introduction

st.sidebar.title('Video Game Sales Prediction ')

PAGES = {
    "Introduction": pages.Introduction,
    "Data Visulation": pages.Visulation,
    "Prediction" : pages.Prediction
}
st.sidebar.title('Menu')
selection = st.sidebar.radio("", list(PAGES.keys()))
page = PAGES[selection]
page.app()
