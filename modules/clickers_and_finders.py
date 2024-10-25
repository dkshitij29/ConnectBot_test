'''
Author:     Datta Lohith Gannavarapu
LinkedIn:   https://www.linkedin.com/in/datta-lohith/

Copyright (C) 2024 Datta Lohith Gannavarapu

License:    GNU Affero General Public License
            https://www.gnu.org/licenses/agpl-3.0.en.html
            
GitHub:     https://github.com/Datta-Lohith/Connect-Bot
'''


from yaml import safe_load
from modules.helpers import buffer, print_lg
from modules.open_chrome import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

config = safe_load(open("setup/config.yaml", "r"))

# Hard Click
def hard_click(actions, ele):
    if not ele: return False
    try:
        print(ele.text)
        actions.move_to_element(ele).click().perform()
        buffer(config["click_gap"])
        return True
    except: return False

# Click Functions
def wait_span_click(driver, x, time=5.0, click=True, scroll=True, scrollTop = False, actions = False):
    if x:
        try:
            button = WebDriverWait(driver,time).until(EC.presence_of_element_located((By.XPATH, '//span[normalize-space(.)="'+x+'"]')))
            if scroll:  scroll_to_view(driver, button, scrollTop)
            if click:
                try: button.click()
                except:
                    if actions: actions.move_to_element(button).click().perform()
                buffer(config["click_gap"])
            return button
        except Exception as e:
            print_lg("Click Failed! Didn't find '"+x+"'")
            # print_lg(e)
            return False

def multi_sel(driver, l, time=5.0):
    for x in l:
        try:
            button = WebDriverWait(driver,time).until(EC.presence_of_element_located((By.XPATH, '//span[normalize-space(.)="'+x+'"]')))
            scroll_to_view(driver, button)
            button.click()
            buffer(config["click_gap"])
        except Exception as e:
            print_lg("Click Failed! Didn't find '"+x+"'")
            # print_lg(e)

def multi_sel_noWait(driver, l, actions=False):
    for x in l:
        try:
            button = driver.find_element(By.XPATH, '//span[normalize-space(.)="'+x+'"]')
            scroll_to_view(driver, button)
            button.click()
            buffer(config["click_gap"])
        except Exception as e:
            if actions: company_search_click(driver,actions,x)
            else:   print_lg("Click Failed! Didn't find '"+x+"'")
            # print_lg(e)

def boolean_button_click(driver, actions, x):
    try:
        list_container = driver.find_element(By.XPATH, '//h3[normalize-space()="'+x+'"]/ancestor::fieldset')
        button = list_container.find_element(By.XPATH, './/input[@role="switch"]')
        scroll_to_view(driver, button)
        actions.move_to_element(button).click().perform()
        buffer(config["click_gap"])
    except Exception as e:
        print_lg("Click Failed! Didn't find '"+x+"'")
        # print_lg(e)

# Find functions
def find_by_class(driver, class_name, time=5.0):
    return WebDriverWait(driver, time).until(EC.presence_of_element_located((By.CLASS_NAME, class_name)))

# Scroll functions
def scroll_to_view(driver, element, top = False, smooth_scroll = config["smooth_scroll"]):
    if top: return driver.execute_script('arguments[0].scrollIntoView();', element)
    behavior = "smooth" if smooth_scroll else "instant"
    return driver.execute_script('arguments[0].scrollIntoView({block: "center", behavior: "'+behavior+'" });', element)

# Enter input text functions
def text_input_by_ID(driver, id, value, time=5.0):
    username_field = WebDriverWait(driver, time).until(EC.presence_of_element_located((By.ID, id)))
    username_field.send_keys(Keys.CONTROL + "a")
    return username_field.send_keys(value)

def try_xp(driver, xpath, click=True):
    try:
        if click:
            driver.find_element(By.XPATH, xpath)
            return True
        else:
            return driver.find_element(By.XPATH, xpath)
    except Exception as e:
        return False

def try_linkText(driver, linkText):
    try:    return driver.find_element(By.LINK_TEXT, linkText)
    except:  return False

def try_find_by_classes(driver, classes):
    for cla in classes:
        try:    return driver.find_element(By.CLASS_NAME, cla)
        except: pass
    raise Exception("Failed to find an element with given classes")
