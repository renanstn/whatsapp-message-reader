import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def get_geckodriver():
    path_geckodriver = os.path.join(dir_path, 'bin', 'geckodriver')
    driver = webdriver.Firefox(executable_path=path_geckodriver)
    return driver

def get_chromedriver():
    path_chromedriver = os.path.join(dir_path, 'bin', 'chromedriver')
    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=./User_Data')
    driver = webdriver.Chrome(executable_path=path_chromedriver, chrome_options=options)
    return driver


dir_path = os.getcwd()
url = "https://web.whatsapp.com/"
driver = get_chromedriver()
# driver = get_geckodriver()
driver.get(url)

try:
    # Aguardar a imagem de abertura do zap (class=_18W8t)
    WebDriverWait(driver, 30).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, '_18W8t'))
    )

    print('zap conectado')

    primeira_mensagem = driver.find_element_by_class_name('X7YrQ')
    primeira_mensagem.click()
    time.sleep(10)

    # messages = driver.find_elements_by_class_name('message-in')
    # messages_count_a = len(messages)
    # messages_count_b = messages_count_a

    # while True:
    #     # Notificações de mensagens novas tem span com class 'P6z4j'
    #     messages = driver.find_elements_by_class_name('message-in')
    #     messages_count_b = len(messages)
    #     if messages_count_a != messages_count_b:
    #         message = messages[-1]
    #         print("Nova mensagem identificada!")
    #         print(message.text)
    #         messages_count_a = messages_count_b

finally:
    driver.quit()
