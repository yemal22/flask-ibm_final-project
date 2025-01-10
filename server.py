"""
This module provides a Flask-based web application
for detecting emotions from text using an emotion detector.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

# Create the Flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    """
    Detect the dominant emotion from the provided text.
    """
    text_to_analyse = request.args.get("textToAnalyze")
    emotion = emotion_detector(text_to_analyse)

    if emotion["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    return emotion

@app.route("/")
def render_index_page():
    """
    Render the main index page.
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
