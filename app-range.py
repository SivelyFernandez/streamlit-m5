import pandas as pd 
import streamlit as st 

st.title('Streamlit_range')
DATA_URL= ('dataset.csv')

@st.cache
def load_data_byrange(startid, endid):
    data = pd.read_csv(DATA_URL)
    filtered_data_byrange = data[(data['index']>=startid)&(data['index']>=startid)] 
    return filtered_data_byrange

startid = st.text_input('Start index :')
endid = st.text_input('End index : ')
btnRange= st.button('Search by range')

if (btnRange):
    filteredbyrange = load_data_byrange(int(startid), int(endid))
    count_row = filteredbyrange.shape[0]
    st.write(f"Total items : {count_row}")

    st.dataframe(filteredbyrange)




