import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


dir_path = os.getcwd()
path_geckodriver = os.path.join(dir_path, 'bin', 'geckodriver')

driver = webdriver.Firefox(executable_path=path_geckodriver)
url = "https://web.whatsapp.com/"
driver.get(url)

try:
    WebDriverWait(driver, 60).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, 'message-in'))
    )

    messages = driver.find_elements_by_class_name('message-in')
    messages_count_a = len(messages)
    messages_count_b = messages_count_a

    while True:
        messages = driver.find_elements_by_class_name('message-in')
        messages_count_b = len(messages)
        if messages_count_a != messages_count_b:
            message = messages[-1]
            print("Nova mensagem identificada!")
            print(message.text)
            messages_count_a = messages_count_b

finally:
    driver.quit()
