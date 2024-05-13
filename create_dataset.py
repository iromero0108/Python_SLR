import os

import pickle
import mediapipe as mp
import cv2
import matplotlib.pyplot as plt

# variable used to detect landmarks of the hand
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# model which represents the hand
hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

# contant of where images are located
DATA_DIR = './data'

# these arrays will contain the data and labels of the images
data = []
labels = []
# loops through each directory in listed folder
for dir_ in os.listdir(DATA_DIR):
    # loops through each image within each folder located in the orignal given folder
    for img_path in os.listdir(os.path.join(DATA_DIR, dir_)):
        # will store the x and y coords
        data_tmp = []
        # stores the current image
        img = cv2.imread(os.path.join(DATA_DIR, dir_, img_path))
        # coverts the image from bgr into rgb
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # detects landmarks in the image and stores in variable
        results = hands.process(img_rgb)

        # checks if there are hand landmarks present
        if results.multi_hand_landmarks:
            # loops through each hand_landmark found
            for hand_landmarks in results.multi_hand_landmarks:
                # create an array of all landmarks that are detected
                for i in range(len(hand_landmarks.landmark)):
                    # this is the x, y, and z, coords of the detected landmarks
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_tmp.append(x)
                    data_tmp.append(y)

        # appends x and y coords
        data.append(data_tmp)
        # appends the category or directory number
        labels.append(dir_)

# stores all the data into a file
open_file_wb = open('data.pickle', 'wb')
pickle.dump({'data': data, 'labels': labels}, open_file_wb)
open_file_wb.close()