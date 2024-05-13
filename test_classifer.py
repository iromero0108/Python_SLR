import cv2
import mediapipe as mp
import pickle
import numpy as np

# gets the model from the pickle file for random forest
#model_dict = pickle.load(open('./modelRF.p', 'rb'))
model_dict = pickle.load(open('./modelMLP.p', 'rb'))
model = model_dict['model']

# tells us which camera to use, in my case the only camera I have is set to 0 as it's the only camera
cap = cv2.VideoCapture(0)

# variable used to detect landmarks of the hand
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# model which represents the hand
hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

labels_dict = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}

font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1.3
color = (0, 0, 0)
thickness = 3

while True:
    data_tmp = []
    x_tmp = []
    y_tmp = []

    # starts the camera capture
    ret, frame = cap.read()
    
    height, width, _ = frame.shape

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # detects landmarks in the image and stores in variable
    results = hands.process(frame_rgb)
    # checks if there are hand landmarks present
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style()
            )

        # loops through each hand_landmark found
            for hand_landmarks in results.multi_hand_landmarks:
                # create an array of all landmarks that are detected
                for i in range(len(hand_landmarks.landmark)):
                    # this is the x, y, and z, coords of the detected landmarks
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_tmp.append(x)
                    data_tmp.append(y)
                    x_tmp.append(x)
                    y_tmp.append(y)

            # stores the x and y values
            x1 = int(min(x_tmp) * width) - 10
            y1 = int(min(y_tmp) * height) - 10

            x2 = int(max(x_tmp) * width) - 10
            y2 = int(max(x_tmp) * height) - 10
            # stores what the model thinks the handsign is
            prediction = model.predict([np.asarray(data_tmp)])
            predicted_character = labels_dict[int(prediction[0])]
            
            #cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 1)
            cv2.putText(frame, predicted_character, (x1, y1 - 10), font, fontScale, color, thickness, cv2.LINE_AA)


    cv2.imshow('frame', frame)
    # wait 1ms between each frame
    cv2.waitKey(1)

# releases the hardware/memory
cap.realease()
cv2.destroyAllWindows()