import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):

    def test_empty_text(self):
        result = emotion_detector("")
        self.assertIn("error", result)

    def test_none_text(self):
        result = emotion_detector(None)
        self.assertIn("error", result)


if __name__ == "__main__":
    unittest.main()