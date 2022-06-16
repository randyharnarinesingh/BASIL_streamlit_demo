import streamlit as st

@st.cache
def my_func():
     pass

st.title('Other useful widgets')

st.subheader('st.button')
if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')

st.subheader('st.radio')
agree = st.checkbox('I agree')
if agree:
     st.write('Great!')

st.subheader('st.checkbox')
genre = st.radio("What's your favorite movie genre",['Comedy', 'Drama', 'Documentary'])
if genre == 'Comedy':
     st.write('You selected comedy.')
else:
     st.write("You didn't select comedy.")

st.subheader('Color picker')
color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)

st.subheader('Upload file')
file = st.file_uploader("Choose a file")