import streamlit as st
import datetime

st.title('Date and time widgets')

st.header('Date selection')
d = st.date_input(
     "When's your birthday",
     datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)

st.header('Time selection')
t = st.time_input('Set an alarm for', datetime.time(8, 45))
st.write('Alarm is set for', t)