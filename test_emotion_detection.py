import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_emotion_detector_output_keys(self):
        result = emotion_detector("I am happy")

        self.assertIsInstance(result, dict)

        self.assertIn('anger', result)
        self.assertIn('disgust', result)
        self.assertIn('fear', result)
        self.assertIn('joy', result)
        self.assertIn('sadness', result)
        self.assertIn('dominant_emotion', result)

    def test_dominant_emotion(self):
        result = emotion_detector("I am very happy")

        self.assertIn(result['dominant_emotion'], ['anger', 'disgust', 'fear', 'joy', 'sadness'])


if __name__ == "__main__":
    unittest.main()
