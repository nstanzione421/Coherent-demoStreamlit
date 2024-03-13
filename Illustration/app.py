import requests
import pandas as pd
import streamlit as st
from helpers import *
from ref import *


# Initiate Data App
st.image('Coherent-Logo.png', width=200)

st.title("FIA Quoting Tool")

st.markdown('')

age = st.number_input('Enter Age: ', min_value=50, max_value=60, value=50)
w_age = st.number_input('Withdrawal Age: ', min_value=age, max_value=80, value=70)
interest = st.radio('Interest Choice: ', options=['Fixed','Index'])
premium = st.number_input('Single Premium Amount: ', min_value=10000, max_value=10000000, value=150000)

payload = create_spark_call(age, w_age, interest, premium)
st.markdown('')

try:
    if st.button('Calculate Income'):
        response = requests.request("POST", url, headers=headers, json=payload, allow_redirects=False)
except:
    pass

try:
    # res = get_data(req, url, headers)
    res = response.json()
    withdrawal = res['response_data']['outputs']['initial_withdrawal']
    ill_js = res['response_data']['outputs']['annuity_cashflow']
    illustration = pd.json_normalize(ill_js)
    illustration.rename(columns={'Interest Earned ': 'Interest Earned'}, inplace=True)
    print(illustration['Interest Earned'])
    illustration['Withdrawals'] = illustration['Withdrawals'].apply(lambda x: x * -1)
    illustration['COI'] = illustration['COI'].apply(lambda x: x * -1)
    st.subheader('Annual Income: :blue[${:0,.0f}]'.format(withdrawal).replace('$-','-$'))
    st.bar_chart(illustration, x='Age', y=['Beginning Cash Value', 'COI', 'Interest Earned', 'Withdrawals'], color=['#0066ff','#ff3300','#6699ff','#ff6666'])
    # st.bar_chart(illustration, x='Age', y=['Beginning Cash Value', 'Interest Earned', 'Withdrawals'], color=['#0066ff','#6699ff','#ff3300'])
    st.dataframe(illustration, hide_index=True)

except:
    pass