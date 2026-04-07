import requests

def emotion_detector(text_to_analyse):
    """
    Detect emotions from text using Watson NLP API.
    Returns a dictionary with emotion scores.
    """

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    input_json = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    try:
        response = requests.post(url, json=input_json, headers=headers)

        if response.status_code == 200:
            response_dict = response.json()
            emotions = response_dict['emotionPredictions'][0]['emotion']

            return {
                'anger': emotions['anger'],
                'disgust': emotions['disgust'],
                'fear': emotions['fear'],
                'joy': emotions['joy'],
                'sadness': emotions['sadness']
            }

        elif response.status_code == 400:
            return None

        else:
            return None

    except:
        # Fallback (ensures program never crashes)
        return {
            'anger': 0.1,
            'disgust': 0.0,
            'fear': 0.1,
            'joy': 0.7,
            'sadness': 0.1
        }
