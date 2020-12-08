import pytest
from selenium import webdriver
from selenium.webdriver import Firefox
import sys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
 
def test_lambdatest_todo_app():
    url = 'https://sistema.zettabrasil.com.br/siggma'
    navegador = Firefox()
    navegador.get(url)
    sleep(1)
    elemento = navegador.find_element_by_id("cpUser")
    elemento.click()
    elemento.clear()
    elemento.send_keys('zetta_login')
    senha_elemento = navegador.find_element_by_id("cpPwd")
    senha_elemento.click()
    senha_elemento.clear()
    senha_elemento.send_keys('zetta_senha')
    botao_elemento = navegador.find_element_by_id('btEnviar').click()
    sleep(5)
    assert navegador.find_element_by_id("notifyDiv")
    sleep(2)
    navegador.close()
