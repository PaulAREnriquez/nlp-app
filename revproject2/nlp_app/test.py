import requests

url = "https://mak76u80ef.execute-api.ap-southeast-1.amazonaws.com/Prod/predict" # API PAM

query = input("Input text: ")

data = {"body": "{\"data\": \""+query+"\"}"}
resp = requests.post(url, json = data)
print(resp.text)