import os
import cv2

# sets the path for where the date is stored
DATA_DIR = './data'
# if the data folder doesn't exist, make the folder
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# this is the number of letters we'll have and the number of images taken per letter
number_of_letters = 4
dataset_size = 200

# variables for cv2 putText() function
text = 'Press "Q" to start'
org = (100, 50)
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1.3
color = (0, 0, 0)
thickness = 3

# tells us which camera to use, in my case the only camera I have is set to 0 as it's the only camera
cap = cv2.VideoCapture(0)

for i in range(number_of_letters):
    # creates the directory for the letter
    if not os.path.exists(os.path.join(DATA_DIR, str(i))):
        os.makedirs(os.path.join(DATA_DIR, str(i)))

    # prints which number it is collecting data for
    print('Collecting data for class {}'.format(i))

    # basically acts as a menu until user presses the assigned button to begin
    while True:
        # starts the camera capture
        ret, frame = cap.read()
        # puts text on the video
        cv2.putText(frame, text, org, font, fontScale, color, thickness, cv2.LINE_AA)
        # opens the camera
        cv2.imshow('frame', frame)
        # if user enters q, go to next loop
        if cv2.waitKey(25) == ord('q'):
            break

    # initializes a counter for pic numbers
    counter = 0
    # loops until counter hits dataset_size
    while counter < dataset_size:
        # initalizes the camera
        ret, frame = cap.read()
        # opens the camera
        cv2.imshow('frame', frame)
        # wait 25 ms between each frame
        cv2.waitKey(25)
        # saves the image to corrosponding folder
        cv2.imwrite(os.path.join(DATA_DIR, str(i), '{}.jpg'.format(counter)), frame)
        # incrememnts the counter
        counter += 1

# releases the hardware/memory
cap.release()
cv2.destroyAllWindows()