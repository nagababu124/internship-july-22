import streamlit as st
import numpy as np
import pandas as pd
from pickle import load

df=pd.read_csv('diamonds.csv')

# Loading pretrained models from pickle file
label_enc=load(open('models/label_encoder.pkl','rb'))
scaler = load(open('models/standard_scaler.pkl', 'rb'))
dt_regressor=load(open('models/dt_model.pkl','rb'))


st.title('💎 Diamond Price Prediction 💎')

'Please fill all the Diamond properties.'

with st.form('my_form'):
    carat = st.number_input('Enter Carat Value')
    cut = st.selectbox(label='Select Cut of Diamond', options=df.cut.unique())
    color = st.selectbox(label='Select Color of Diamond', options=df.color.unique())
    clarity= st.selectbox(label='Select Clarity level of Diamond', options=df.clarity.unique())
    depth=st.number_input('Enter depth value of Diamond')
    table=st.number_input('Enter table value of Diamond')

    
    btn = st.form_submit_button(label='Predict')


if btn:
    if carat and cut and color and clarity and depth and table:
        query_num = pd.DataFrame({'carat':[carat], 'depth':[depth],'table':[table]})
        query_cat = pd.DataFrame({'cut':[cut], 'color':[color], 'clarity':[clarity]})
        color_encoder = {'J':1, 'I':2, 'H':3, 'G':4, 'F':5, 'E':6, 'D':7}

        query_cat['color'] = query_cat['color'].apply(lambda x : color_encoder[x])
        query_cat['cut'] = label_enc.transform(query_cat['cut'])
        query_cat['clarity'] = label_enc.transform(query_cat['clarity'])
        query_point = pd.concat([pd.DataFrame(query_num), pd.DataFrame(query_cat)], axis=1)
        scaler_n = scaler.transform(query_point)
        price = dt_regressor.predict(scaler_n)
        
        st.success(f"The price of Selected Diamond is $ {round(price[0] - 172,2)}")
        st.balloons()
    else:
        st.error('Enter all the values')    
        st.snow()

   

################################## BACKGROUND IMAGE CODE #######################################

page_bg_img = '''
<style>
.stApp {
background-image: url("https://th.bing.com/th/id/OIP.PZmlNMsYIp71xYCr9MwvLgHaFj?pid=ImgDet&rs=1");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

