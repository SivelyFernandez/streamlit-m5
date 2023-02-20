import streamlit as st
import pandas as pd 

st.title("Streamlit - Search namers")
DATA_URL = ("dataset.csv")

@st.cache
def load_data_byName(name):
    data = pd.read_csv(DATA_URL)
    filtered_data = data[data["name"].str.contains(name)]
    return filtered_data

myName = st.text_input("Name: ")
if(myName):
    filtered = load_data_byName(myName)
    count_row = filtered.shape[0]
    st.write(f"Total names: {count_row}")

    st.dataframe(filtered)