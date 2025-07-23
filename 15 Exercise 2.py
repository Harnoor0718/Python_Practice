#Q:
# Write a Python program that prints a greeting message based on the current system time. The program should display the current time in HH:MM:SS format and greet the user as follows:

# Good Morning if the time is between 5:00 AM and 11:59 AM

# Good Afternoon if the time is between 12:00 PM and 4:59 PM

# Good Evening if the time is between 5:00 PM and 8:59 PM

# Good Night for any other time
import time

# Get current hour using strftime
timestamp = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))

print("Current Time:", timestamp)

# Time-based greeting logic
if 5 <= hour < 12:
    print("Good Morning!")
elif 12 <= hour < 17:
    print("Good Afternoon!")
elif 17 <= hour < 21:
    print("Good Evening!")
else:
    print("Good Night!")
