'''
Author:     Datta Lohith Gannavarapu
LinkedIn:   https://www.linkedin.com/in/datta-lohith/

Copyright (C) 2024 Datta Lohith Gannavarapu

License:    GNU Affero General Public License
            https://www.gnu.org/licenses/agpl-3.0.en.html
            
GitHub:     https://github.com/Datta-Lohith/Connect-Bot
'''

from yaml import safe_load

config = safe_load(open("setup/config.yaml", "r"))
secrets = safe_load(open("setup/secrets.yaml", "r"))

def validate_TorF(var, var_name):
    if var == True or var == False: return True
    raise Exception(f'Invalid input for {var_name}. Expecting a Boolean input "True" or "False", not "{var}" and do NOT surround True or False in Quotes ("")!')

def validate_String(var, var_name, options=[]):
    if not isinstance(var, str): raise Exception(f'Invalid input for {var_name}. Expecting a String!')
    if len(options) > 0 and var not in options: raise Exception(f'Invalid input for {var_name}. Expecting a value from {options}, not {var}!')
    return True

def validate_Multi(var, var_name, options=[]):
    if not isinstance(var, list): raise Exception(f'Invalid input for {var_name}. Expecting a List!')
    for element in var:
        if not isinstance(element, str): raise Exception(f'Invalid input for {var_name}. All elements in the list must be strings!')
        if len(options) > 0 and element not in options: raise Exception(f'Invalid input for {var_name}. Expecting all elements to be values from {options}. This "{element}" is NOT in options!')
    return True


def validate_config():
    
    if not isinstance(config["click_gap"], int) and config["click_gap"] >= 0: raise Exception(f'Invalid input for click_gap. Expecting an int greater than or equal to 0, NOT "{config["click_gap"]}"!')

    validate_TorF(config["run_in_background"], "run_in_background")
    validate_TorF(config["smooth_scroll"], "smooth_scroll")

    validate_String(secrets["username"], "username")
    validate_String(secrets["password"], "password")

    validate_Multi(config["search_terms"], "search_terms")

    return True

