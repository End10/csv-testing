import requests

def KeyAccessTool(filePath, keyName):
    with open(filePath) as f:
        for x in f:
            key = x.removeprefix(keyName+":")
            key.strip()
            return key
    
#USA .gov API
govKey = (KeyAccessTool(r"C:\Users\Jamesb\OneDrive - The University of Chicago\Documents\API keys.txt","govKey"))

def govGetRequest(param):
    params = {
    'limit': '1',
    'api_key': govKey,
    }

response = requests.get('https://developer.nrel.gov/api/alt-fuel-stations/v1.json', params=params)
return response