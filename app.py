import streamlit as st  # pip install streamlit
import pandas as pd  # pip install pandas
# import plotly.express as px  # pip install plotly-express
import base64  # Standard Python Module
from io import StringIO, BytesIO  # Standard Python Module

st.set_page_config(page_title='CSV Plotter')
st.title('CSV Plotter 📈')
st.subheader('Feed me with your CSV file')

uploaded_file = st.file_uploader('Choose a CSV file', type='csv')

if uploaded_file:
    st.markdown('---')
    df = pd.read_csv(uploaded_file)
    dtime = df['Date & Time'][0]
    edtime = df['Date & Time'].iat[-1]
    st.dataframe(df)
    length = len(uploaded_file.name)

    # -- PLOT DATAFRAME
    # fig = px.line(
    #     df,
    #     x= 'Date & Time',
    #     y= 'ECG_Data',
    # )

    st.markdown('---')
    st.subheader('Patient Details : ')
    st.markdown(f'→ Patient Name : {uploaded_file.name[slice(length - 4)]}')
    st.markdown(f'→ Patient Age : {dtime[slice(1,11)]}')
    st.markdown(f'→ ECG Date : {dtime[slice(1,11)]}')
    st.markdown(f'→ Start Time : {dtime[slice(12,24)]}')
    st.markdown(f'→ End Time : {edtime[slice(12,24)]}')
    st.markdown('---')
    st.markdown(f"<p style='text-align: center; font-weight: bold'>{uploaded_file.name[slice(length - 4)]} ECG Plot</p>", unsafe_allow_html=True)
    st.plotly_chart(fig)
