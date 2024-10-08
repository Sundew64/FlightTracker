# step 1: import requests
import requests

# step 2: call api with given endpoint and key
api_result = requests.get() # requests the data from the endpoint

# step 3: convert to dictionary and grab only the "data" value
api_result=api_result.json()
data = api_result['data']

# step 4: loop through the flights and check which flights are active

# step 5: if active, print the airline, date, departure airport and arrival airport