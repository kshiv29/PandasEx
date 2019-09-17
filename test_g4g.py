import time
import webbrowser

a = 'geeks'
lst = list(a)
print(list(a))
print(a)

# Import the time module, it provides various time-related
# functions.


# Import the webbrowser module, it is used to
# display various HTML documents to the user.


# First Input: It is the time of the form
# 'Hours:Minutes:Seconds' that you'll
# use to set the alarm.
Set_Alarm = input("Set the website alarm as H:M:S:")

# Second Input: It is the URL that you want
# to open on the given time.
url = input("Enter the website you want to open:")

# This is the actual time that we will use to print.
Actual_Time = time.strftime("%I:%M:%S")
print("The time is " + Actual_Time)
print("The set time is " + Set_Alarm)
print(Actual_Time == Set_Alarm)
# This is the while loop that'll print the time
# until it's value will be equal to the alarm time
while (Actual_Time != Set_Alarm):
    print("The time is " + Actual_Time)
    Actual_Time = time.strftime("%I:%M:%S")
    time.sleep(1)
