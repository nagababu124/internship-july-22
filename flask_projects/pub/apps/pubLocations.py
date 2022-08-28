import streamlit as st
import numpy as np
import pandas as pd

def app():
    st.title('Pub Locations')
    df = pd.read_csv("clean_openPubs.csv")
    opt=st.selectbox('',('Local Authority','Postal Code'))
    if opt=='Local Authority':
        option=st.selectbox(opt,df.local_authority.unique())

        if st.button("Search"):
                pubs_data = df[df["local_authority"]==option]
                "You searched for:",option
                "Total no of pubs in this location is:",len(pubs_data)
                st.map(pubs_data)
                st.dataframe(pubs_data[['name','address','local_authority']])
    else:
        pc=st.selectbox(opt,df.postcode.unique())

        if st.button("Search"):
                pubs_data = df.loc[df["postcode"]==pc]
                "You searched for:",pc
                "Total no of pubs in this location is:",len(pubs_data)
                st.map(pubs_data)
                st.dataframe(pubs_data[['name','address','postcode']])

    
 


        

