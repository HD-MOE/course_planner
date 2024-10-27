import streamlit as st

ecg_page = st.Page("streamlit_app.py", title="ECG Agent", icon= "🧭" )
about_us_page = st.Page("1_About Us.py", title="About Us", icon= "🧑🏻‍🏫" )
methodology_page = st.Page("2_Methodology.py", title="Methodology", icon= "🛠️" )

pg = st.navigation([ecg_page, about_us_page, methodology_page])
st.set_page_config(page_title="ECG Agent", page_icon="🧭", layout="wide")
pg.run()