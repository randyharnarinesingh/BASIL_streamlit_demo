import os
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Logo and header
st.image('./basil.jpg',width=100,caption='Our favorite spice')
st.title('BASIL app - Title')

# File loading
st.sidebar.header('File loading - Heading')
# st.text('I am a text block - Text')
file_list = [x for x in os.listdir() if x.endswith('.csv')]
file_selection = st.sidebar.selectbox('Select a file',file_list)
# st.write(file_selection)

# FIle preview
st.header('File preview')
df = pd.read_csv(file_selection)
st.dataframe(df)

# Aggregated view
st.header('Grouped view - Means')
df_agg = df.groupby('variety').mean()
st.dataframe(df_agg)

# Column selection
st.sidebar.header('Column selection')
column_list = df.select_dtypes('number').columns
col_selection = st.sidebar.selectbox('Select a column', column_list)

# Distribution plot
st.header('Distribution plots')
fig, ax = plt.subplots()
sns.kdeplot(df[col_selection], ax=ax)
st.pyplot(fig)

# Double-column plot
st.header('Double column split')
col1, col2 = st.columns(2)

fig2, ax2 = plt.subplots()
fig3, ax3 = plt.subplots()
ax2.scatter(df['petal.length'],df['variety'])
col1.write("I am a randomly textly block of text information full of text.")
col1.pyplot(fig2)
col1.write("There was some text above. I am also some text below.")

hist_col = col2.selectbox("Pick a column:",column_list)
df.hist(hist_col,by='variety',ax=ax3)
col2.pyplot(fig3)

# File download functionality
st.header('File download')
st.download_button(
    label="Download aggregated data as CSV",
    data=df_agg.to_csv(index=False).encode('utf-8'),
    file_name='my_df.csv',
    mime='text/csv',
)