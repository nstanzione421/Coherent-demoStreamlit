import pandas as pd
import streamlit as st
import json
import requests
from ref import *

# Function Creations

def lookup_json(fund):
    #intialize Dict objects
    inputs = {}
    request_data = {}
    #Create values for objects
    inputs['lookup.FundName'] = fund
    request_data['inputs'] = inputs
    #add Request meta variables
    request_meta['service_category'] = f'#Default#,lookup'
    
    request = {
        'request_data': request_data,
        'request_meta': request_meta
    }
    return request

def default_json(plan):
    #intialize Dict objects
    inputs = {}
    request_data = {}
    #Create values for objects
    inputs['pricing.PlanType'] = plan
    request_data['inputs'] = inputs
    #add Request meta variables
    request_meta['service_category'] = f'#Default#,pricing'
    
    request = {
        'request_data': request_data,
        'request_meta': request_meta
    }
    return request

def change_json(plan, add, remove):
    #intialize Dict objects
    inputs = {}
    request_data = {}
    #Create values for objects
    inputs['pricing.PlanType'] = plan
    inputs['pricing.arrAdd'] = [{'Add Fund': add}]
    inputs['pricing.arrRemove'] = [{'Remove': remove}]
    request_data['inputs'] = inputs
    #add Request meta variables
    request_meta['service_category'] = f'#Default#,pricing'
    
    request = {
        'request_data': request_data,
        'request_meta': request_meta
    }
    return request


def spark_call(payload):
    response = requests.request("POST", url, headers=headers, data=json.dumps(payload), allow_redirects=False)
    return response.json()

def result(x):
    #Write threading results to array of JSON repsonses
    results = []
    for i in range(len(x)):
        arr = {}
        Reserve = x[i]['response_data']['outputs']['Reserve']
        CapitalReq =  x[i]['response_data']['outputs']['CapitalReq']
        arr['Reserve'] = Reserve
        arr['CapitalReq'] = CapitalReq
        results.append(arr)
    return results



# def data_load(x):  
#     # Set-up file and read in data into a pandas dataframe
#     try:
#         data = pd.read_csv(x)
#         st.text("Upload success!")
#         buffer = io.StringIO()
#         data.info(buf=buffer)
#         s = buffer.getvalue()
#         st.text(s)
#         return data
#     except ValueError:
#         st.text("Waiting for file...")






