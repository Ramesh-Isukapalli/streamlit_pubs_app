import streamlit as st
import pandas as pd
import haversine as hs

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

st.markdown("<h2 style='text-align: center; color: #ffffff;'>&#128205 Nearest Pubs Available &#128205</h2>",unsafe_allow_html=True)
st.markdown("<br>",unsafe_allow_html=True)

distance_method = st.radio("How do you want to find the nearest pubs?",
                    ('By Haversine Formula','By Euclidean Formula'), horizontal=True)

x1 = st.number_input("Enter the latitude of your location",format="%.6f")
y1 = st.number_input("Enter the longitude of your location",format="%.6f")

lat = list(df['latitude'])
lon = list(df['longitude'])
distance = []



if distance_method == 'By Haversine Formula':

    for x2, y2 in zip(lat, lon):
        distance.append(hs.haversine((x1,y1),(x2,y2)))
    df['distance'] = distance
    st.map(df.sort_values(by=['distance']).head(6).iloc[1:])

    pub_names = tuple(df.sort_values(by=['distance']).head(6).name.iloc[1:])
    local_authorities = tuple(df.sort_values(by=['distance']).head(6).local_authority.iloc[1:])
    distance_from_location = tuple(df.sort_values(by=['distance']).head(6).distance.iloc[1:])

    st.markdown("<h4 style='color: #116466;'>5 pubs nearest to your location</h4>",unsafe_allow_html=True)
    st.write(f"\n1. {pub_names[0]} pub run by {local_authorities[0]} is in the distance of {distance_from_location[0]} Km")
    st.write(f"\n2. {pub_names[1]} pub run by {local_authorities[1]} is in the distance of {distance_from_location[1]} Km")
    st.write(f"\n3. {pub_names[2]} pub run by {local_authorities[2]} is in the distance of {distance_from_location[2]} Km")
    st.write(f"\n4. {pub_names[3]} pub run by {local_authorities[3]} is in the distance of {distance_from_location[3]} Km")
    st.write(f"\n5. {pub_names[4]} pub run by {local_authorities[4]} is in the distance of {distance_from_location[4]} Km")

elif distance_method == 'By Euclidean Formula':
    for x2, y2 in zip(lat, lon):
        distance.append(((x2-x1)**2 + (y2-y1)**2)**0.5)
    df['distance'] = distance
    st.map(df.sort_values(by=['distance']).head(6).iloc[1:])

    pub_names = tuple(df.sort_values(by=['distance']).head(6).name.iloc[1:])
    local_authorities = tuple(df.sort_values(by=['distance']).head(6).local_authority.iloc[1:])
    distance_from_location = tuple(df.sort_values(by=['distance']).head(6).distance.iloc[1:])

    st.markdown("<h4 style='color: #116466;'>5 pubs nearest to your location</h4>",unsafe_allow_html=True)
    st.write(f"\n1. {pub_names[0]} pub run by {local_authorities[0]}")
    st.write(f"\n2. {pub_names[1]} pub run by {local_authorities[1]}")
    st.write(f"\n3. {pub_names[2]} pub run by {local_authorities[2]}")
    st.write(f"\n4. {pub_names[3]} pub run by {local_authorities[3]}")
    st.write(f"\n5. {pub_names[4]} pub run by {local_authorities[4]}")


