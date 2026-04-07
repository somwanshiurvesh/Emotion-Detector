# pylint: disable=missing-module-docstring,missing-function-docstring

from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    return "Emotion Detection App"


@app.route("/emotionDetector")
def emotion_detector_route():
    text_to_analyse = request.args.get('textToAnalyze')

    if text_to_analyse is None or text_to_analyse.strip() == "":
        return "Invalid input! Please try again."

    result = emotion_detector(text_to_analyse)

    if result is None:
        return "Invalid input! Please try again."

    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
