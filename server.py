from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector_route():
    text = request.args.get('textToAnalyze')

    if not text:
        return "Invalid input! Try again."

    result = emotion_detector(text)

    if result is None:
        return "Invalid input! Try again."

    return str(result)

if __name__ == "__main__":
    app.run(debug=True)
