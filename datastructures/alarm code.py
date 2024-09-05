# pip install opencv-python pygame
import cv2
import pygame
import time

def play_alarm():
    pygame.mixer.init()
    pygame.mixer.music.load("alarm_sound.mp3")  # replace with the path to your alarm sound file
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play(-1)  # -1 means play indefinitely

def stop_alarm():
    pygame.mixer.music.stop()

def detect_human():
    # Load the pre-trained Haar Cascade face detector
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Open the laptop's camera
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        # Convert the frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        if len(faces) > 0:
            stop_alarm()
            break

        cv2.imshow('Alarm Clock', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the OpenCV window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    play_alarm()
    detect_human()
