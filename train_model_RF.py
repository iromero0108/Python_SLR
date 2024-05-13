# Jamie's part
import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

# gets the data from the pickle file
data_dict = pickle.load(open('./data.pickle', 'rb'))

# seperates the data, or coords, and labels, or directory number
data = np.asarray(data_dict['data'])
labels = np.asarray(data_dict['labels'])

# this is splitting all the data into two sets, the x being the coord and y being the directory numbers
# test size is the size of the test set .2 being 20% of the data
# shuffle stands for shuffling the data and we're setting that to true, which can be very important
# stratify stands for we'll keep the same proportion in each set
# for example, 1/3 of the set will be the letter 'A' if you have the letters, 'A', 'B', and 'C' in the data set
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=.3, shuffle=True, stratify=labels)

# initializes the model with the random forest classifier
model = RandomForestClassifier()

# this line trains the classifier
model.fit(x_train, y_train)

# this like trains the predictions
y_predict = model.predict(x_test)

# this gets the score for the accuracy test
score = accuracy_score(y_predict, y_test)

print('{}% of samples were classified correctly'.format(score * 100))

# stores the model a file
open_file_wb = open('modelRF.p', 'wb')
pickle.dump({'model': model}, open_file_wb)
open_file_wb.close()