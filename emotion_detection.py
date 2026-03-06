import requests


def emotion_detector(text_to_analyze):
    if text_to_analyze is None or text_to_analyze.strip() == "":
        return {"error": "Invalid text! Please try again!"}

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
    except requests.exceptions.RequestException:
        return {"error": "Unable to connect to the emotion detection service."}

    if response.status_code == 200:
        formatted_response = response.json()
        emotions = formatted_response["emotionPredictions"][0]["emotion"]

        anger = emotions["anger"]
        disgust = emotions["disgust"]
        fear = emotions["fear"]
        joy = emotions["joy"]
        sadness = emotions["sadness"]

        dominant_emotion = max(emotions, key=emotions.get)

        return {
            "anger": anger,
            "disgust": disgust,
            "fear": fear,
            "joy": joy,
            "sadness": sadness,
            "dominant_emotion": dominant_emotion
        }

    if response.status_code == 400:
        return {"error": "Invalid text! Please try again!"}

    return {"error": "Something went wrong"}