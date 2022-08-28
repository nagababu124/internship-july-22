import streamlit as st
import numpy as np
import pandas as pd

from math import sqrt
def app():
    st.title("Nearest Pub's")
    df = pd.read_csv("clean_openPubs.csv")

    st.write("Please Enter Your latitude and Longitude Below")
    lat=st.number_input('latitude')
    lon=st.number_input('longitude')
    new_df=df[['latitude','longitude']]
    inputs=np.array([lat,lon])
    distance=np.sqrt(np.sum((inputs-new_df)**2, axis=1))
    k = 5
    nearest_neighbor = distance.argsort()[:k]

    if st.button('search'):
        st.text("The locations corresponding to Nearest 5 Pubs ")
        st.map(df.iloc[nearest_neighbor])
        st.dataframe(df.iloc[nearest_neighbor][["name",'address','local_authority']])