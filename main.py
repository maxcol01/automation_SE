from selenium import webdriver
from get_chrome_driver import GetChromeDriver
from selenium.webdriver.common.by import By

# create a new driver object that will make the link with the browser of choice
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get(url="https://www.python.org/")
# implicit wait in order to wait for the user to login if required (e.g., type "I am not a robot")
driver.implicitly_wait(15)

events_list = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li')
events_list_as_list = [item.text.split("\n") for item in events_list]
events_list_as_dict = {item: {events_list_as_list[item][0]: events_list_as_list[item][1]}
                       for item in range(0, len(events_list_as_list))}

print(events_list_as_dict)

# quit the web page once we loaded
driver.quit()
