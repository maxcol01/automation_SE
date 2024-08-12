from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "http://orteil.dashnet.org/experiments/cookie/"

# Options for Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option(name="detach", value=True)

# Driver
driver = webdriver.Chrome(options=options)
driver.get(url=URL)
time_intervals = time.time() + 5
total_time = time.time() + 5 * 60
cookie_button = driver.find_element(By.ID, "cookie")

while True:
    # Button cookie to click
    cookie_button.click()
    max_possible = []
    # click every 5 seconds
    if time.time() > time_intervals:
        # get the number of cookies to compare to the other buttons
        score_money = driver.find_element(By.ID, "money")

        # get the buttons information: value and name
        elements_id = driver.find_elements(By.CSS_SELECTOR, "div#store b")
        # Store everything in a list format:
        list_test = [elements_id[item].text.split(" - ") for item in range(0, len(elements_id) - 1)]
        # get the element which are available for buying, i.e., <= score_money:
        max_possible = [[item[0], item[1].replace(",", "")]
                        for item in list_test if int(item[1].replace(",", ""))
                        <= int(score_money.text.replace(",", ""))]
        # check if there are elements available for buying:
        if len(max_possible) != 0:
            max_possible_final = max(max_possible, key=lambda x: int(x[1]))
            id_to_click = max_possible_final[0]
            button_to_click = driver.find_element(By.ID, f"buy{id_to_click}")
            button_to_click.click()
        # Update the time so we can check again after 5 seconds.
        time_intervals = time.time() + 5

    if time.time() >= total_time:
        break
# Display the final score:
cps = driver.find_element(By.ID, "cps")
print(f"Your score is {cps.text}")
