# Set constant values
import os
from dotenv import load_dotenv
load_dotenv()

url = 'https://excel.uat.us.coherent.global/presales/api/v3/folders/NickStanzione/services/Fixed%20Indexed%20Annuity/Execute'

tenant = 'presales'
content_type = 'application/json'

request_meta = {
    "call_purpose": "Illustration Tool",
    "source_system": "SPARK",
    "correlation_id": "",
    "service_category": "",
}

headers = {
    'content-type': content_type,
    'x-synthetic-key': os.getenv('API_KEY'),
    'x-tenant-name': tenant
}

inputs = {            
    "age": 55,
    "allocation_option": 2,
    "frequency": 1,
    "gender": "M",
    "income_duration": "10",
    "income_start_age": 70,
    "index_table": [
        {
            "Available Index": "S&P 500 Index",
            "Choice": True,
            "Portion": 0.5
        },
        {
            "Available Index": "Nasdaq-100 Index",
            "Choice": True,
            "Portion": 0.5
        },
        {
            "Available Index": "Russel 2000 Index",
            "Choice": False,
            "Portion": 0
        },
        {
            "Available Index": "BlackRock iBLD Claria Index",
            "Choice": False,
            "Portion": 0
        },
        {
            "Available Index": "Bloomberg US Dynamic Balance Index II",
            "Choice": False,
            "Portion": 0
        },
        {
            "Available Index": "PIMCO Tactical Balanced Index",
            "Choice": False,
            "Portion": 0
        },
        {
            "Available Index": "Bloomberg US Dynamic Balance II ER Index",
            "Choice": False,
            "Portion": 0
        },
        {
            "Available Index": "PIMCO Tactical Balanced ER Index",
            "Choice": False,
            "Portion": 0
        },
        {
            "Available Index": "BlackRock iBLD Claria® ER Index",
            "Choice": False,
            "Portion": 0
        }
    ],
    "interest_choice": "Index",
    "premium": 150000,
    "rider_choice": False,
    "runsolver": False,
    "solveWithdrawal": 90000,
    "term": 10
}