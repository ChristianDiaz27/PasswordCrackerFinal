# Imports the Password Cracker class, a stopwatch module, and a GUI module
# THIS REQUIRES THE STOPWATCH.PY AND PYAUTOGUI PACKAGES INSTALLED
from PasswordClass import PasswordCracker
import stopwatch
import pyautogui

# Declaration of variables
password = ""
minutes = 0
seconds = 0.0


# Loops until the user enters a password that is only numbers and is ten characters or fewer
# Loop launches a GUI to take user input and another GUI if the user inputted an invalid password
while True:
    password = pyautogui.password("Please enter a password that is ten characters or less (only numbers):")
    # To allow for the user to enter letter and symbols replace the if statement with this one
    # Replace the corresponding line in the PasswordClass file so that the program can process other inputted passwords
    # if len(password) <= 10:
    if password.isdigit() and len(password) <= 10:
        break
    else:
        pyautogui.alert("\u26A0 Invalid password. Please try again. \u26A0")

# Declares an object of the PasswordCracker class using the password inputted by the user
# Starts a stopwatch and begins cracking the password
# Once the password is found the stopwatch is stopped and the password is outputted
target = PasswordCracker(password)
time = stopwatch.Stopwatch(2)
output = target.crackPassword()
time.stop()

# Outputs the time it took to crack the password
# Converts into minutes if needed
if time.duration > 60:
    minutes = int(time.duration / 60)
    seconds = round((time.duration % 60), 2)
    f = open("Results.txt", "w")
    f.write(output + "\nYour password took " + str(minutes) + " minute(s) and " + str(seconds) + " seconds to crack!")
    f.close()
    f = open("Results.txt", "r")
    print(f.read())
else:
    seconds = round(time.duration, 2)
    f = open("Results.txt", "w")
    f.write(output + "\nYour password took " + str(seconds) + " seconds to crack!")
    f.close()
    f = open("Results.txt", "r")
    print(f.read())