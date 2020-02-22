import os
import time
import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def setup_logging():
    logging.basicConfig(filename='logs.log', level=logging.INFO)

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

def aguardar_conexao():
    WebDriverWait(driver, 30).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, '_18W8t'))
    )

def clicar_no_primeiro_contato():
    primeira_mensagem = driver.find_element_by_class_name('X7YrQ')
    primeira_mensagem.click()

def identificar_mensagens_existentes():
    messages = driver.find_elements_by_class_name('message-in')
    count = len(messages)
    return count

def verificar_novas_mensagens(quantidade_inicial):
    messages = driver.find_elements_by_class_name('message-in')
    quantidade_atual = len(messages)
    if quantidade_inicial != quantidade_atual:
        logging.info('chegou mensagens novas!')
        mensagens_para_exibir = messages[quantidade_atual-1:]
        return mensagens_para_exibir

def exibir_mensagens(mensagens=[]):
    for mensagem in mensagens:
        print(mensagem.text)

# -------------------------------------------------------------------------------------------
setup_logging()
dir_path = os.getcwd()
url = "https://web.whatsapp.com/"
driver = get_chromedriver()
# driver = get_geckodriver()
driver.get(url)
logging.info('-----------------SCRIPT INICIADO-----------------')

try:
    aguardar_conexao()
    logging.info('Zap conectado')
    clicar_no_primeiro_contato()
    logging.info('primeiro contato selecionado')

    messages_count_a = identificar_mensagens_existentes()
    messages_count_b = messages_count_a
    logging.info(f'{messages_count_a} mensagens identificadas')

    while True:
        # Notificações de mensagens novas tem span com class 'P6z4j'
        mensagens = verificar_novas_mensagens(messages_count_a)
        if mensagens:
            exibir_mensagens(mensagens)
            messages_count_a = len(mensagens)

finally:
    driver.quit()
