import pyautogui
pyautogui.FAILSAFE = False
from random import choice, shuffle, randint
from modules.open_chrome import *
from yaml import safe_load
from modules.helpers import *
from modules.clickers_and_finders import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, NoSuchWindowException

# Load configuration
config = safe_load(open("setup/config.yaml", "r"))

# Replace placeholders in search terms with the company name
if "company_name" in config:
    company_name = config["company_name"]
    config["search_terms"] = [term.replace("{{company_name}}", company_name) for term in config["search_terms"]]

secrets = safe_load(open("setup/secrets.yaml", "r"))

# Function to check if user is logged-in in LinkedIn
def is_logged_in_LN():
    if driver.current_url == "https://www.linkedin.com/feed/": 
        return True
    if try_linkText(driver, "Sign in"): 
        return False
    if try_xp(driver, '//button[@type="submit" and contains(text(), "Sign in")]'):  
        return False
    if try_linkText(driver, "Join now"): 
        return False
    print_lg("Didn't find Sign in link, so assuming user is logged in!")
    return True

# Function to login to LinkedIn
def login_LN():
    driver.get("https://www.linkedin.com/login")
    try:
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Forgot password?")))
        try:
            text_input_by_ID(driver, "username", secrets["username"], 1)
        except Exception as e:
            print_lg("Couldn't find username field.")
        try:
            text_input_by_ID(driver, "password", secrets["password"], 1)
        except Exception as e:
            print_lg("Couldn't find password field.")
        driver.find_element(By.XPATH, '//button[@type="submit" and contains(text(), "Sign in")]').click()
    except Exception as e1:
        try:
            profile_button = find_by_class(driver, "profile__details")
            profile_button.click()
        except Exception as e2:
            print_lg("Couldn't Login!")
    try:
        wait.until(EC.url_to_be("https://www.linkedin.com/feed/"))
        print_lg("Login successful!")
    except Exception as e:
        print_lg("Login attempt failed! Try logging in manually!")
        manual_login_retry(is_logged_in_LN, 2)

# Function to get pagination element and current page number
def get_page_info():
    try:
        pagination_element = try_xp(driver, ".//div[contains(@class,'artdeco-pagination--has-controls')]", False)
        if not pagination_element:
            pagination_element = try_find_by_classes(driver, ["artdeco-pagination", "artdeco-pagination__pages", "artdeco-pagination__pages--number"])
        scroll_to_view(driver, pagination_element)
        current_page = int(pagination_element.find_element(By.XPATH, "//li[contains(@class, 'active')]").text)
    except Exception as e:
        print_lg("Failed to find pagination element!")
        pagination_element = None
        current_page = None
    return pagination_element, current_page

# Function to send connection request
def connect_with_person(profile_url, window, person_name, searchTerm):
    try:
        driver.switch_to.window(window)
        driver.get(profile_url)
        sleep(3)
        
        if try_xp(driver, "(//span[@class='artdeco-button__text'][normalize-space()='Pending'])[2]", False):
            print_lg(f"Connection request already pending for: {person_name}")
            return False

        connect_button = (
            hard_click(actions, try_xp(driver, "(//button[contains(@class, 'artdeco-button--primary') and .//span[text()='Connect']])[2]", False)) or
            hard_click(actions, try_xp(driver, "(//button[contains(@class, 'artdeco-button--secondary') and .//span[text()='Connect']])[2]", False))
        )

        if not connect_button:
            more_actions = try_xp(driver, "//button[@aria-label='More actions']", False)
            if more_actions:
                hard_click(actions, more_actions)
                sleep(1)
                connect_button = hard_click(actions, try_xp(driver, "(//span[@class='display-flex t-normal flex-1'][normalize-space()='Connect'])[2]", False))
        
        if not connect_button:
            print_lg(f"Couldn't find Connect button for: {person_name}. Skipping this profile.")
            return False
        
    except Exception as e:
        print_lg(f"Error while attempting to connect with {person_name}: {str(e)}")
        return False

    if config["add_note"]:
        add_note_and_send(person_name, searchTerm)
    else:
        hard_click(actions, try_xp(driver, "//button[@aria-label='Send without a note']", False))

    print_lg(f"Connection request sent to {person_name}.")
    return True

# Function to add note and send connection request
def add_note_and_send(person_name, searchTerm):
    try:
        hard_click(actions, try_xp(driver, "//button[@aria-label='Add a note']", False))
        
        # Custom connection message
        if person_name == "Unknown":
            person_name = "there"  # Fallback to generic greeting
        
        note_key = (
            f"Hi {person_name},\n\n"
            f"I’m add_your_name, a graduate student in CIS at the University_name. I’m exploring internship opportunities at {searchTerm} and noticed your impressive experience there. "
            f"I’d love to connect and hear your insights if you have a moment for a quick chat.\n\n"
            f"Thank you!"
        )
        
        # Input the custom message
        text_input_by_ID(driver, "custom-message", note_key)
        hard_click(actions, try_xp(driver, "//button[@aria-label='Send invitation']", False))
        print_lg(f"Note added and connection request sent to {person_name}.")
    except Exception as e:
        print_lg(f"Failed to add note for {person_name}: {str(e)}")

# Main function
def main():
    try:
        alert_title = "Error Occurred. Closing Browser!"
        driver.get("https://www.linkedin.com/login")
        if not is_logged_in_LN(): 
            login_LN()

        linkedIn_tab = driver.current_window_handle

        for searchTerm in config["search_terms"]:
            current_request = 0

            if current_request >= config["max_connections_per_search"]:
                break

            driver.get(f"https://www.linkedin.com/search/results/people/?keywords={searchTerm}")
            print_lg(f"\n>>>> Now searching for '{searchTerm}' <<<<\n")
            buffer(2)

            while current_request < config["max_connections_per_search"]:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(1)
                pagination_element, current_page = get_page_info()
                driver.execute_script("window.scrollTo(0, 0);")

                people = driver.find_elements(By.XPATH, '//div[@data-view-name="search-entity-result-universal-template"]')  

                driver.switch_to.new_window('window')
                connections_tab = driver.current_window_handle

                for person in people:
                    if config["keep_screen_awake"]:
                        pyautogui.press('shiftright')
                    
                    print_lg("\n-@-\n")
                    driver.switch_to.window(linkedIn_tab)

                    link_element = person.find_element(By.TAG_NAME, 'a')
                    profile_url = link_element.get_attribute('href')
                    person_name = "Unknown"
                    try:
                        title_element = WebDriverWait(person, 5).until(
                            EC.presence_of_element_located((By.CLASS_NAME, "entity-result__title-line"))
                        )
                        person_name = title_element.text.split("\n")[0]
                        if "1st" in title_element.text.lower():
                            print_lg(f'Skipping "{person_name}", Profile URL: {profile_url}. Already a connection.')
                            continue
                    except Exception as e:
                        print_lg(f"Failed to fetch name for profile {profile_url}: {str(e)}")
                        print(f"HTML snapshot of the failed element: {person.get_attribute('outerHTML')}")

                    if person_name == "Unknown":
                        print_lg(f"Name not found for profile {profile_url}. Using a generic fallback message.")

                    print_lg(f'Sending connection request to "{person_name}", Profile URL: {profile_url}')
                    
                    if connect_with_person(profile_url, connections_tab, person_name, searchTerm):
                        current_request += 1
                    else:
                        print_lg(f"Skipped, a previous connection request is pending with '{person_name}'")
                    
                    if current_request >= config["max_connections_per_search"]:
                        break
                
                driver.switch_to.window(connections_tab)
                driver.close()
                driver.switch_to.window(linkedIn_tab)

                if current_request < config["max_connections_per_search"]:
                    if pagination_element is None:
                        print_lg("End of results. No pagination element found!")
                        break
                    try:
                        pagination_element.find_element(By.XPATH, f"//button[@aria-label='Page {current_page+1}']").click()
                        print_lg(f"Moved to Page {current_page+1}.")
                    except NoSuchElementException:
                        print_lg("End of results. No more pages!")
                        break

    except Exception as e:
        critical_error_log("In Connector Main", e)
        pyautogui.alert(e, alert_title)
    finally:
        try:
            driver.quit()
        except Exception as e:
            critical_error_log("Error while quitting browser", e)

main()
