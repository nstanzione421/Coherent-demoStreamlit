import pandas as pd
import streamlit as st
import json
import requests
import asyncio
import aiohttp

from ref import *


def to_request(inputs, request_meta):
    # Turn dataframe into JSON data structure
    data_js = inputs.to_json(orient='records')
    data_ls = json.loads(data_js)
    #Create array of JSON requests
    req = []
    for i in range(len(inputs)):
        request_data = {}
        y = data_ls[i]
        request_data['inputs'] = y
        request = {
            'request_data': request_data,
            'request_meta': request_meta
        }
        req.append(request)
    return req

def write_results(x):
    #Write threading results to array of JSON repsonses
    results = []
    for i in range(len(x)):
        arr = {}
        Premium = x[i]['response_data']['outputs']['Premium_Annual']
        # CapitalReq =  x[i]['response_data']['outputs']['CapitalReq']
        arr['Premium'] = Premium
        # arr['CapitalReq'] = CapitalReq
        results.append(arr)
    return results

#aSync Functionality
async def async_batch_call(url, headers, data_list):
    async with aiohttp.ClientSession() as session:
        tasks =[session.post(url, headers=headers, json=data) for data in data_list]
        responses = await asyncio.gather(*tasks)
        results = []
        for resp in responses:
            results.append(await resp.json())
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

# # Function Creations

# def to_json(x):
#     # Turn dataframe into JSON data structure
#     data_js_r = x.to_json(orient='records')
#     data_js = json.loads(data_js_r)
#     # res = json.dumps(data_js)
#     inputs['tblCenus'] = data_js
#     request_data = {}
#     request_data['inputs'] = inputs
#     request = {
#         'request_data': request_data,
#         'request_meta': request_meta
#     }
#     return request

# def spark_call(payload):
#     response = requests.request("POST", url, headers=headers, data=json.dumps(payload), allow_redirects=False)
#     return response.json()

# def result(x):
#     #Write threading results to array of JSON repsonses
#     results = []
#     for i in range(len(x)):
#         arr = {}
#         Reserve = x[i]['response_data']['outputs']['Reserve']
#         CapitalReq =  x[i]['response_data']['outputs']['CapitalReq']
#         arr['Reserve'] = Reserve
#         arr['CapitalReq'] = CapitalReq
#         results.append(arr)
#     return results




