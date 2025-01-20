import cv2
from fer import FER
import time

# Initialize the emotion detector
detector = FER()

# Sample social script for different scenarios
social_scripts = {
    "greeting": "Hi there! How are you today? It's nice to see you!",
    "small_talk": "How was your day? Did you do anything interesting?",
    "thank_you": "You're welcome! I'm glad I could help.",
    "goodbye": "Goodbye! Take care and see you soon!"
}

# Basic emotion-based response function
def get_emotion_response(emotion):
    if emotion == "happy":
        return "You look happy! That's great!"
    elif emotion == "sad":
        return "It seems like you're feeling down. Would you like to talk about it?"
    elif emotion == "angry":
        return "It seems like you're frustrated. Try to take a deep breath and relax."
    elif emotion == "surprise":
        return "You seem surprised! What happened?"
    elif emotion == "fear":
        return "It seems like you're scared. It's okay, take a moment to calm down."
    elif emotion == "disgust":
        return "It seems like you're feeling disgusted. Is there something bothering you?"
    else:
        return "I couldn't detect your emotion, but I'm here if you need to talk!"

# Function to capture the video feed from the webcam
def capture_emotion():
    # Open the webcam
    cap = cv2.VideoCapture(0)
    
    while True:
        # Read the frame from the webcam
        ret, frame = cap.read()

        if not ret:
            print("Failed to capture image")
            break
        
        # Detect emotions in the frame
        emotion, score = detector.top_emotion(frame)
        
        # Display the frame and the detected emotion
        cv2.putText(frame, f"Emotion: {emotion}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Emotion Detection", frame)

        # Give feedback based on detected emotion
        if emotion:
            print(get_emotion_response(emotion))
        
        # Wait for a key press to break the loop
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    # Release the webcam and close the window
    cap.release()
    cv2.destroyAllWindows()

# Function to display social scripts based on user input
def display_social_script():
    print("\nSocial Scripts:")
    print("1. Greeting")
    print("2. Small Talk")
    print("3. Thank You")
    print("4. Goodbye")

    choice = input("\nChoose a scenario by number: ")
    
    if choice == "1":
        print(social_scripts["greeting"])
    elif choice == "2":
        print(social_scripts["small_talk"])
    elif choice == "3":
        print(social_scripts["thank_you"])
    elif choice == "4":
        print(social_scripts["goodbye"])
    else:
        print("Invalid choice, please try again.")

# Main function
def main():
    print("Welcome to the Emotion Recognition and Social Script App!")
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Detect emotion using webcam")
        print("2. View a social script")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            capture_emotion()
        elif choice == "2":
            display_social_script()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
