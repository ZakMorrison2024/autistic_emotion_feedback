
# Emotion Recognition and Social Script App

## Overview

This is a temporary prototype project for an **Emotion Recognition and Social Script App** aimed at young autistic adults. The app recognizes emotions from facial expressions using a webcam and provides predefined social scripts for various social scenarios to help users navigate social interactions.

The app uses the **FER** library for facial emotion recognition and **OpenCV** for capturing the webcam feed. Social scripts are predefined responses to situations like greetings, small talk, and thank yous.

This project is a starting point for further development and future work to improve emotion detection, social interaction guidance, and overall user experience.

## Features

- **Emotion Detection**: Using a webcam to detect emotions like happiness, sadness, anger, fear, and surprise.
- **Social Scripts**: Provides predefined responses for common social situations such as greetings and small talk.
- **Feedback**: Real-time feedback based on the detected emotion, offering possible responses or calming statements.

## Installation

To run this app, you need Python installed along with the required libraries. You can install the required libraries using the following commands:

```bash
pip install opencv-python fer
```

## Usage

1. Clone or download the repository.
2. Run the `emotion_script_app.py` file.
3. You will be prompted to either:
   - Detect emotions using your webcam.
   - View a social script for a chosen scenario (e.g., greeting, small talk, thank you).
4. For emotion detection, the webcam will open, and the app will display the recognized emotion along with feedback. To exit, press 'q'.
5. For social scripts, choose a number corresponding to the scenario, and the app will print the corresponding script.

## Sample Social Scripts:

- **Greeting**: "Hi there! How are you today? It's nice to see you!"
- **Small Talk**: "How was your day? Did you do anything interesting?"
- **Thank You**: "You're welcome! I'm glad I could help."
- **Goodbye**: "Goodbye! Take care and see you soon!"

## Future Work

This app is a prototype for future development. The following improvements and additions are planned:

- **Voice Integration**: Add text-to-speech capabilities for real-time vocal responses.
- **Advanced Emotion Recognition**: Expand emotion recognition to include voice tone and other emotional cues.
- **Mobile App Development**: Transition this functionality to a mobile app for easier accessibility.
- **User Feedback**: Gather feedback from real users to refine the app’s accuracy and usefulness.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

If you have questions or suggestions, feel free to reach out!

