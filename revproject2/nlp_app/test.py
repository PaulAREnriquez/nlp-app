import requests

#url = "https://qek33lyhqa.execute-api.ap-northeast-1.amazonaws.com/Prod/predict" # AWS API Gateway URL

# url = "https://w2qqzmtg1f.execute-api.ap-southeast-1.amazonaws.com/Prod/predict" # API ARN
url = "https://mak76u80ef.execute-api.ap-southeast-1.amazonaws.com/Prod/predict" # API PAM

query = input("Input text: ")

data = {"body": "{\"data\": \""+query+"\"}"}
resp = requests.post(url, json = data)
print(resp.text)