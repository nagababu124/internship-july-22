from dataclasses import field
from operator import index
from tkinter.tix import COLUMN
import streamlit as st
import numpy as np
import pandas as pd


def app():
    
    st.title('Home')
    st.info("Fields")
    fields = pd.read_csv("Fields.csv")
    st.dataframe(fields)

    st.info("Data")
    df = pd.read_csv("clean_openPubs.csv")
    st.dataframe(df)

    st.info("Satistical Analysis")
    st.dataframe(df.describe())

    st.info("Applications")
    df2 = pd.read_csv("Applications.csv")
    st.dataframe(df2)




