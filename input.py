'''
Author: Muhammad Mobeen
Reg No: 200901097
BS-CS-01 (B)
Lab Task [11 Jan 202]
Submitted to Mam Reeda Saeed

GitHub Repo URL: https://github.com/muhammad-mobeen/Inter-Process-Communication
'''
import getpass  # Utilities to get a password and/or the current user name.
import datetime

username = getpass.getuser()    # Get the username from the environment or password database.
now = datetime.datetime.now()   # Construct a datetime from time.time() and optional time zone info.

print("Welcome, {}!".format(username))
print("Current date and time: " + now.strftime("%d-%m-%Y %H:%M:%S"))
