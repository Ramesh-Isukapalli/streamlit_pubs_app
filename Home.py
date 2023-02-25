from tkinter import N
import streamlit as st
import pandas as pd
import io

streamlit_style = """
            <style>
            @import url('https://fonts.googleapis.com/css2?family=Margarine&display=swap');

            html, body, [class*="css"]  {
            font-family: 'Margarine', cursive;
            }
            h2{
                background: #2C3531;
                box-shadow: 0 8px 32px 0 rgba( 31, 38, 135, 0.37 );
                backdrop-filter: blur( 4px );
                -webkit-backdrop-filter: blur( 4px );
                border-radius: 10px;
                border: 1px solid rgba( 255, 255, 255, 0.18 );
            }
            </style>
            """
st.markdown(streamlit_style, unsafe_allow_html=True)



df = pd.read_csv("data/pubs_cleaned.csv")
df.drop('Unnamed: 0',axis=1,inplace=True)

st.markdown("<h2 style='font-size: 35px; text-align: center; color: #ffffff;'>Welcome to Pub data House&#129346;</h2>",unsafe_allow_html=True)


st.markdown("<h4 style='font-size: 30px; color: #116466;'>Details of the data set</h4>",unsafe_allow_html=True)
data_info = st.radio('Click on the detail of data frame you want view:',
                      ('Shape', 'Head', 'Tail', 'Columns', 'Info', 'Descriptive Statistics'),
                      horizontal=True)

if data_info == 'Shape':
    st.write(f"Number rows in data frame: {df.shape[0]}")
    st.write(f"Number columns in data frame: {df.shape[1]}")
elif data_info == 'Head':
    st.write(df.head())
elif data_info == 'Tail':
    st.write(df.tail())
elif data_info == 'Columns':
    for column in list(df.columns):
        st.write(column)
elif data_info == 'Info':
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)
else:
    st.write(df.describe())


@st.cache
def convert_df(df):
    #IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(df)



st.markdown("<br>",unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center';>Click on below to downlaod dataset</h5>",unsafe_allow_html=True)
col1, col2, col3 , col4, col5 = st.columns(5)

with col1:
    pass
with col2:
    pass
with col4:
    pass
with col5:
    pass
with col3 :
    center_button = st.download_button(
     label="Download",
     data=csv,
     file_name='my_pubs.csv',
     mime='text/csv',
 )

