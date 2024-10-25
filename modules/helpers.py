'''
Author:     Datta Lohith Gannavarapu
LinkedIn:   https://www.linkedin.com/in/datta-lohith/

Copyright (C) 2024 Datta Lohith Gannavarapu

License:    GNU Affero General Public License
            https://www.gnu.org/licenses/agpl-3.0.en.html
            
GitHub:     https://github.com/Datta-Lohith/Connect-Bot
'''

import os
from time import sleep
from random import randint
from datetime import datetime, timedelta
import yaml

logs_folder_path = yaml.safe_load(open("setup/config.yaml", "r"))["logs_folder_path"]


#### Common functions ####

#< Directories related
# Function to create missing directories
def make_directories(paths):
    for path in paths:  
        path = path.replace("//","/")
        if '/' in path and '.' in path: path = path[:path.rfind('/')]
        if not os.path.exists(path):   os.makedirs(path)

# Function to search for Chrome Profiles
def find_default_profile_directory():
    # List of default profile directory locations to search
    default_locations = [
        r"%LOCALAPPDATA%\Google\Chrome\User Data",
        r"%USERPROFILE%\AppData\Local\Google\Chrome\User Data",
        r"%USERPROFILE%\Local Settings\Application Data\Google\Chrome\User Data"
    ]
    for location in default_locations:
        profile_dir = os.path.expandvars(location)
        if os.path.exists(profile_dir):
            return profile_dir
    return None
#>


#< Logging related
# Function to log critical errors
def critical_error_log(possible_reason, stack_trace):
    print_lg(possible_reason, stack_trace, datetime.now())
    pass

# Function to log and print
def print_lg(*msgs):
    try:
        message = "\n".join(str(msg) for msg in msgs)
        path = logs_folder_path+"/log.txt"
        with open(path.replace("//","/"), 'a+', encoding="utf-8") as file:
            file.write(message + '\n')
        print(message)
    except Exception as e:
        critical_error_log("Log.txt is open or is occupied by another program!", e)
#>


# Function to wait within a period of selected random range
def buffer(speed=0):
    if speed<=0:
        return
    elif speed <= 1 and speed < 2:
        return sleep(randint(6,10)*0.1)
    elif speed <= 2 and speed < 3:
        return sleep(randint(10,18)*0.1)
    else:
        return sleep(randint(18,round(speed)*10)*0.1)
    

# Function to ask and validate manual login
def manual_login_retry(is_logged_in, limit = 2):
    count = 0
    while not is_logged_in():
        from pyautogui import alert
        print_lg("Seems like you're not logged in!")
        button = "Confirm Login"
        message = 'After you successfully Log In, please click "{}" button below.'.format(button)
        if count > limit:
            button = "Skip Confirmation"
            message = 'If you\'re seeing this message even after you logged in, Click "{}". Seems like auto login confirmation failed!'.format(button)
        count += 1
        if alert(message, "Login Required", button) and count > limit: return










