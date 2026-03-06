# Emotion Detector

This project implements an Emotion Detection application using the Watson NLP library.

## Project Description

The Emotion Detector analyzes a given text and identifies the emotional tone present in the sentence.  
The application returns the following emotions:

- anger
- disgust
- fear
- joy
- sadness

It also determines the **dominant emotion** among these values.

## Technologies Used

- Python
- Flask
- Watson NLP API
- Requests library
- Pylint for static code analysis
- Unit testing with unittest

## Project Structure
emotion-detector/  
│
├── EmotionDetection/  
│ ├── init.py  
│ └── emotion_detection.py  
│
├── templates/  
│ └── index.html  
│
├── server.py  
├── test_emotion_detection.py  
└── README.md  

## How to Run the Application

1. Navigate to the project directory:


cd emotion-detector


2. Run the Flask server:


python server.py


3. Open your browser and go to:


http://127.0.0.1:5000


4. Enter a sentence and click **Analyze Emotion** to see the detected emotions.

## Author

Soukaina Elbaz


