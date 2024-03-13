import requests
import pandas as pd
import streamlit as st
from helpers import *
from ref import *


# Initiate Data App
st.title("Plan Quoting Tool")
st.markdown('')

#Set-up drag & drop input for csv upload into dataframe
file = st.file_uploader("Drop your census file here to load", type={"csv"})

#Upload file and return message when complete
try:
    inputs = pd.read_csv(file)
    st.text("Upload success!")
    req = to_request(inputs, request_meta)
except ValueError:
    st.text("Waiting for file...")

#Function to Run Batch
# @st.cache(suppress_st_warning=True)
def get_data(req, url, headers): 
    store = asyncio.run(async_batch_call(url, headers, req))
    z = write_results(store)
    return z

#Set up Calculate button to control making API Call
try:
    if st.button('Calculate Premium'):
        res = get_data(req, url, headers)
except:
    pass

#Return premium from API Call response if avaiable
try:
    # res = get_data(req, url, headers)
    res_df = pd.json_normalize(res)
    premium = res_df['Premium'].sum()
    st.subheader('Annual Premium: :blue[${:0,.0f}]'.format(premium).replace('$-','-$'))
except:
    pass


