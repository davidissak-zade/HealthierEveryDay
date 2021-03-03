# HealthierEveryDay

Back End: 
DB.json - file where the data about users is saved (internally in the project directory)
DailyCalories - is a file that has 2 functions inside that help the program calculate your DCI - daily calorie needs
algorithms.py - just has a function that helped me sort the data of the api
executor.py - is the main BACK_END working file, it imports all the information and runs the program
plotting.py - is the file that has only one function inside (which is imported to executor.py), it plots users progress so far by taking data from an internal json file


Front End (main.py, ui_functions.py)
INTERFACE.ui is an interface file that has not been connected to the back end yet : )
Interface.py is a python code that represents the GUI so that we could import the GUI to python Back-End working files
main.py - is a file that opens my GUI (Interface.py) and displays + animates it by importing the animation-oriented functions from ui_functions.py
ui_functions.py - is a file consisting of one function (currently) that enables user to toggle the Menubar
