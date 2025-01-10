import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    response = requests.post(url, json=myobj, headers=header)
    
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    
    formated_response = json.loads(response.text)

    emotion = formated_response['emotionPredictions'][0]['emotion']

    dominant_emotion = [k for k, v in emotion.items() if v == max(emotion.values())][0]
    emotion['dominant_emotion'] = dominant_emotion

    return emotion
    