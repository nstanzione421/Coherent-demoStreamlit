import requests
import pandas as pd
import streamlit as st
from helpers import *
from ref import *


# Initiate Data App
st.title("Fund Selection Tool")

check, default, change = st.tabs(["Fund Check", "Default Lineup", "Change Lineup"])

st.markdown('')


#Get inputs and return Spark API response
fund = check.text_input('Enter Fund Ticker', value="")

try:
    req_check = lookup_json(fund)
    if check.button('Check Fund'):
        resp_check = spark_call(req_check)
        out1 = resp_check['response_data']['outputs']['lookup.boolAvailable']
        out2 = resp_check['response_data']['outputs']['lookup.arrPlanTypes']
        out3 = resp_check['response_data']['outputs']['lookup.tblStatistics']
        out4 = resp_check['response_data']['outputs']['lookup.FundType']

        arr = pd.json_normalize(out2)
        tbl = pd.json_normalize(out3)

except NameError:
    pass

try:
    check.text('Fund Availibility: {}'.format(out1))
    if out1:
        check.text('Fund Type: {}'.format(out4))
        check.text('Plan Availability')
        check.table(arr)
        check.text('Plan Statistics')
        check.table(tbl)

except: 
    pass


#Get inputs and return Spark API response
plan = default.text_input('Enter Plan Type', value="")

try:
    req_def = default_json(plan)
    if default.button('Check Plan'):
        resp_def = spark_call(req_def)
        rdef = resp_def['response_data']['outputs']['pricing.tblDefaultFundLineup']

        tbldef = pd.json_normalize(rdef)

except NameError:
    pass

try:
    default.text('Default Lineup')
    default.table(tbldef)

except: 
    pass

#Get inputs and return Spark API response
add = change.text_input('Add Fund', value="")
remove = change.text_input('Remove Fund', value="")

try:
    req_chng = change_json(plan, add, remove)
    if change.button('Change Lineup'):
        resp_chng = spark_call(req_chng)
        new = resp_chng['response_data']['outputs']['pricing.tblNewFundLineup']
        old = resp_chng['response_data']['outputs']['pricing.DefaultPrice']
        price = resp_chng['response_data']['outputs']['pricing.NewPrice']
        new = pd.json_normalize(new)

        req_add = lookup_json(add)        
        resp_add = spark_call(req_add)
        outadd = resp_add['response_data']['outputs']['lookup.boolAvailable']

except:
    pass

try:
    change.text('Added Fund Available: {}'.format(outadd))
    change.text('Old Price: {}'.format(old))
    change.text('New Price: {}'.format(price))
    change.text('New Lineup')
    change.table(new)

except: 
    pass
    

# try:
#     data = pd.read_csv(file)
#     upload.text("Upload success!")
#     upload.text(data)
# except ValueError:
#     upload.text("Waiting for file...")

# tier1Match = provisions.number_input('CB113: SRC 1 - TIER 1 MATCH %', 0, 100, 100, 5)
# tier1Max = provisions.slider('CB114: SRC 1 - TIER 1 MAX MATCH %', 0, 10, 2)
# tier2Match = provisions.number_input('CB113: SRC 1 - TIER 2 MATCH %', 0, 100, 50, 5)
# tier2Max = provisions.slider('CB114: SRC 1 - TIER 2 MAX MATCH %', tier1Max, 10+tier1Max, tier1Max+1)
# trueUp = provisions.selectbox("CB269: Plan has Match True Up", ("Yes", "No"))

# provs = [tier1Match, tier1Max, tier2Match, tier2Max, trueUp]


#     req = to_json(data, provs)
#     provisions.text(req)
#     if provisions.button('Calculate'):
#         resp = spark_call(req)
#         # results.text(resp)
#         out1 = resp['response_data']['outputs']['CurrFormula']
#         out2 = resp['response_data']['outputs']['CurrFormulaCost']
#         out3 = resp['response_data']['outputs']['BasicSHCost']
#         out4 = resp['response_data']['outputs']['EnhancedSHCost']
#         out5 = resp['response_data']['outputs']['NECCost']
#         out6 = resp['response_data']['outputs']['QACACost']

#         diff3 = out3 - out2
#         diff4 = out4 - out2
#         diff5 = out5 - out2
#         diff6 = out6 - out2 
#     else:
#         provisions.warning('Waiting for Spark Call')

#     if resp['status'] == 'Success':
#         provisions.success('Spark Call Success!')
#     else:
#         pass

# except NameError:
#     pass

# try:
#     with results:
#         st.subheader('Current Cost: :blue[${:0,.0f}]'.format(out2).replace('$-','-$'))
#         st.text('Current Formula: {}'.format(out1)) 
#         col1, col2, col3, col4 = st.columns(4)
#         col1.metric("Basic", '${:0,.0f}'.format(out3), round(diff3), 'inverse')
#         col2.metric("Enhanced", '${:0,.0f}'.format(out4), round(diff4), 'inverse')
#         col3.metric("NonElective", '${:0,.0f}'.format(out5), round(diff5), 'inverse')
#         col4.metric("QACA", '${:0,.0f}'.format(out6), round(diff6), 'inverse')
# except:
#     pass



