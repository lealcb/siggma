from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
import time
from colorama import init
from colorama import Fore, Back, Style
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

url = 'https://sistema.zettabrasil.com.br/siggma'
zetta_login = str(input("Login: "))
zetta_senha = str(input("Senha: "))
zetta_base = str(input("Digite a base: "))
init(autoreset=True)
navegador = Firefox()

def chamarjanela(codigojanela):
    cmd = navegador.find_element_by_xpath("/html/body")
    cmd.send_keys(Keys.CONTROL + Keys.ALT + "C")
    cmd_comando = navegador.find_element_by_id("tSystemCmd")
    cmd_comando.clear()
    cmd.send_keys(Keys.CONTROL + Keys.ALT + "C")
    cmd_comando.send_keys(f"{codigojanela}")
    cmd_comando.send_keys(Keys.ENTER)


def login(*args):
    user , userpwd  = args
    elemento = navegador.find_element_by_id("cpUser")
    elemento.click()
    elemento.clear()
    elemento.send_keys(f"{user}")
    senha_elemento = navegador.find_element_by_id("cpPwd")
    senha_elemento.click()
    senha_elemento.clear()
    senha_elemento.send_keys(f"{userpwd}")
try:
    navegador.get(url)
    time.sleep(1)
    login(zetta_login,zetta_senha)
    botao_elemento = navegador.find_element_by_id('btEnviar')
    botao_elemento.click()
    time.sleep(5)
except Exception as e:
    print(e)
    navegador.close()
verificar_url = navegador.current_url
try:
    if verificar_url == "https://sistema.zettabrasil.com.br/siggma/app/index/workbench":
        bloqueado_base_digitar = navegador.find_element_by_class_name("zt-info")
        bloqueado_base_digitar.click()
        bloqueado_digitar_base = navegador.find_element_by_xpath("/html/body/section[2]/div[1]/div[1]/div[2]/input")
        bloqueado_digitar_base.send_keys(zetta_base)
        time.sleep(2)
        clicar_na_base = navegador.find_element_by_css_selector(f"[data-id='{zetta_base}']").click()
        time.sleep(3)
        comercialModulo = navegador.find_element_by_css_selector(f"[data-id='3']").click()
        time.sleep(2)
    else:
        raw_base_clicar = navegador.find_element_by_id("zt-empresa").click()
        raw_base_digitar = navegador.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/input").send_keys(zetta_base)
        time.sleep(2)
        raw_base_procurar = navegador.find_element_by_css_selector(f"[data-id='{zetta_base}']").click()
except Exception as e:
    print(e)
    print("Algo deu errado ao logar.")
    navegador.close()
##### Criar serie de documento fiscal #####
try:
    time.sleep(5)
    chamarjanela(45)
    

except Exception as e:
    print(e)
    print("Algo deu errado ao definir o perfil padrão do colaborador")
    navegador.close()