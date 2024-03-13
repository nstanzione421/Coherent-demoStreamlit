# Set constant values
# import os
# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st

url = 'https://excel.uat.us.coherent.global/presales/api/v3/folders/DemoStanz/services/DisabilityIncome/Execute'

tenant = 'presales'
content_type = 'application/json'

request_meta = {
    "call_purpose": "Quote Tool",
    "source_system": "SPARK",
    "correlation_id": "",
    "service_category": "",
}

headers = {
    'content-type': content_type,
    'x-synthetic-key': st.secrets["API_KEY"], # os.getenv('API_KEY'),
    'x-tenant-name': tenant
}

