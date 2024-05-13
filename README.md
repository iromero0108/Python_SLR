***IMPORTANT***
Please make sure you are utilizing Python 3.9 or lower. Otherwise, the program will not work. This is because later versions of Python classify some of the types differently and kinda mess up the training program. 

GETTING THE PROGRAM SET UP
As stated above, please use a Python version lower than 3.10, otherwise the program will not work. 
In order to install the proper libraries, run the following command in the ai_project folder, in the terminal where you are running the program:

pip install -r requirements.txt

This will take the libraries listed in the requirements.txt file and allow them to be installed on your local machine

NOTES FOR UTILIZING THE PROGRAM
1. Make sure you are using some sort of machine that has a camera or webcam attached to it, so that the program can use  that for input
2. The main programs for the project are found in the project_ai folder
3. The programs should be executed in the following order:
	1. get_dataset_images
	2. create_dataset
	3. train_model (using either MLP or RF)
	4. test_classifier
4. The train_model program must run without any errors. If it comes up with some float error or some other error when processing the data, that means it ran into an issue trying to fit the data for each corresponding class, and you need to start over from the beginning (starting with get_dataset_images)
5. MUST BE RUN USING A PYTHON VERSION LOWER THAN PYTHON 10! THIS IS IMPORTANT OR THE PROGRAM WILL NOT RUN

