
from django.shortcuts import render
from .forms import SentimentsForm
import requests

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
            resp = requests.post(url, json = data)
            context = {'result': resp.text, 'input': final_review}
            
    """_summary_
   
            
        
            # Text preprocessing
            cleaned_tweet = text_preprocess(final_review)

            # Using Our TfidfVectorizer to transform the tokens from our Training Data
            tfidf_tweet = NlpAppConfig.tfidf.transform(cleaned_tweet).toarray()

            # Converting our vector into tensor
            tfidf_tweet = torch.from_numpy(tfidf_tweet).type(torch.float)
            
            # Using our model to predict the sentiment
            prediction = NlpAppConfig.model_2.forward(tfidf_tweet)
            prediction = torch.softmax(prediction, dim=1)
            prediction = torch.argmax(prediction, dim=1)
            prediction = prediction.detach().cpu().numpy()
            
            if prediction[0] == 0:
                sentiment = "Negative"
            elif prediction[0] == 1:
                sentiment = "Neutral"
            else:
                sentiment = "Positive"

            context = {'result': sentiment, 'input': final_review}
            

    else:
        form = SentimentsForm()

     """
    
    context['form'] = form
    
    
    return render(request, 'analyze.html', context=context)



