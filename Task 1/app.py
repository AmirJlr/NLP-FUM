import streamlit as st
import pandas as pd

# HEAD
st.title('Anne Of Green Gables Quotes')
st.header('38 of the best book quotes from Anne of Green Gables')


col1, col2, col3 = st.columns(3)

# Image
with col1:
    st.write(' ')

with col2:
    st.image('./anne.jpg')

with col3:
    st.write(' ')



df = pd.read_csv('anne.csv')

st.header('Filter Quotes By Character :')
# select character
name = st.selectbox('Select Character :', df['Characters'].unique())

# search character Quotes
def lookup(name):
    return df[df.Characters == name].Quotes

data = lookup(name)


st.table(data)