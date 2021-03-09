import cv2
import numpy as np


def detect(face_cascade, gray):
    # faces = face_cascade.detectMultiScale(gray, 1.3, 3)
    print(gray)
    faces = face_cascade.detectMultiScale(gray)
    print(faces)
    return faces


def draw_faces(faces, image):
    image_to_draw = image.copy()
    for (x, y, w, h) in faces:
        cv2.rectangle(image_to_draw, (x, y), ((x + w), (y + h)), (255, 0, 0), 2)
    return image_to_draw


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

# video_fn = 'guedes.mp4'
CAMERA_NUM = 0
cap = cv2.VideoCapture(CAMERA_NUM)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # print(type(gray))
    # print(gray)
    # # Detect function
    # # num_smiles, image = cv2.cvtColor(frame, gray.copy())
    faces = detect(gray)
    image_to_show = draw_faces(faces, frame)
    # # print(num_smiles)

    cv2.imshow('Video', image_to_show)

    k = cv2.waitKey(1)
    if k & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
