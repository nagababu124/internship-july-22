import streamlit as st
from multiapp import MultiApp
from apps import homePage,pubLocations,nearestPub # import your app modules here
from PIL import Image



app = MultiApp()

st.markdown("""
# Welcome To Open Pubs
### We're organising UK open data into location-based dashboards, surfacing the data available, and signposting the source.

This pub app is using the [streamlit-multiapps]() framework developed by [Nagababu Kona]().
""")
img = Image.open("Pubimg.png")
 
# display image using streamlit
# width is used to set the width of an image
st.image(img,width=800)

# Add all your application here
app.add_app("Home Page", homePage.app)
app.add_app("Pub Locations", pubLocations.app)
app.add_app("Find the nearest Pub", nearestPub.app)
# The main app
app.run()