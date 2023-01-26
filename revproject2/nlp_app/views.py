
from django.shortcuts import render
from .forms import SentimentsForm
import requests

import json
import torch

from .apps import NlpAppConfig
from .utils import text_preprocess

# Create your views here.
def home(request):
    
    """ This function renders the home page """
    
    return render(request, 'home.html')

def getPrediction(request):
    
    """ This function handles the review input and prediction of result """
    
    form = SentimentsForm(request.POST)
    context = {}

    if request.method == 'POST' :
        
        if form.is_valid():
            
            final_review = form['review'].value() #extracts the review to be analyzed'
            url = "https://mak76u80ef.execute-api.ap-southeast-1.amazonaws.com/Prod/predict"
            
            data = {"body": "{\"data\": \""+final_review+"\"}"}
            resp = requests.post(url,json = data)
            

            resp_data = json.loads(resp.text)
            result = resp_data.get('result')
            context = {'result': result, 'input': final_review}
            
    
    context['form'] = form
    return render(request, 'analyze.html', context=context)



