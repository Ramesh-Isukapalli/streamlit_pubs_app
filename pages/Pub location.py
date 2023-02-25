import streamlit as st
import pandas as pd

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

st.markdown("<h2 style='text-align: center; color: #ffffff;'>Pubs Location&#127758</h2>",unsafe_allow_html=True)
st.markdown("<br>",unsafe_allow_html=True)

location_option = st.radio("Select an option based on which you want to see location of a pub:",
                    ('postcode', 'local_authority'), horizontal=True)


if location_option == 'postcode':
    show_df = st.selectbox("Click on dropdown to view by postcodes:",
                            (tuple(df['postcode'].unique())))
    #Display map by postcode
    st.map(df[df['postcode']==show_df])

    st.markdown("<h5>Name of the pub:",unsafe_allow_html=True)
    st.write(df[df['postcode']==show_df].name.iloc[0])
    st.markdown("<h5>Address of the pub:",unsafe_allow_html=True)
    st.write(df[df['postcode']==show_df].address.iloc[0])
    st.markdown("<h5>Local Authority of the pub:",unsafe_allow_html=True)
    st.write(df[df['postcode']==show_df].local_authority.iloc[0])

elif location_option == 'local_authority':
    show_df = st.selectbox("Click on dropdown to view by local_authority:",
                            (tuple(df['local_authority'].unique())))
    #Display map by local_authority
    st.map(df[df['local_authority']==show_df])

    st.markdown("<h4>Pubs available in the selected local_authority:",unsafe_allow_html=True)
    for i in df[df['local_authority']==show_df].name:
        st.write(i)
