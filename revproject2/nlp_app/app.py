import json
import torch

from apps import NlpAppConfig
from utils import text_preprocess

def lambda_handler(event, context):
    
            body = json.loads(json.loads(event["body"])["body"])
            payload = body["data"]
            
            # Text preprocessing
            cleaned_tweet = text_preprocess(payload)

            # Using Our TfidfVectorizer to vectorize the preprocessed text
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

            context = {'result': sentiment, 'input': payload}
            
            return {
                "statusCode": 200,
                "body": json.dumps(context),
            }
    


