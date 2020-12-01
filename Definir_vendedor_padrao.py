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


def nomeusuario(user):
    elemento = navegador.find_element_by_id("cpUser")
    elemento.click()
    elemento.clear()
    elemento.send_keys(f"{user}")


def senhausuario(userpwd):
    senha_elemento = navegador.find_element_by_id("cpPwd")
    senha_elemento.click()
    senha_elemento.clear()
    senha_elemento.send_keys(f"{userpwd}")

try:
    navegador.get(url)
    time.sleep(1)
    nomeusuario(zetta_login)
    senhausuario(zetta_senha)
    botao_elemento = navegador.find_element_by_id('btEnviar')
    botao_elemento.click()
    time.sleep(5)
except Exception as e:
    print(e)
    navegador.close()
verificar_url = navegador.current_url
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

# Definir vendedor padrão 
time.sleep(5)
chamarjanela(52)
time.sleep(5)
btn_pesquisar = navegador.find_element_by_id("btnPesquisar").click()
time.sleep(2)
user_id_valid = navegador.find_element_by_xpath(f"//td[@title='1']").click() # Nao esquecer de mudar para 1
time.sleep(5)
btn_alterar = navegador.find_element_by_id("btnAlterar").click()
time.sleep(2)
vend_padrao = navegador.find_element_by_css_selector("#tabs-1 > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(7) > td:nth-child(2) > span:nth-child(2) > span:nth-child(1) > span:nth-child(1)").click()
vend_padrao_text = navegador.find_element_by_xpath("//li[text()='VENDEDOR']").click()
time.sleep(2)
btn_salvar = navegador.find_element_by_id("btnPersistir").click()

# # Verificações


verf_vendedor = navegador.find_element_by_xpath(f"//td[@title='VENDEDOR']").text
assert (verf_vendedor == "VENDEDOR"), f"O status atual é {verf_vendedor} e não VENDEDOR. Necessario verificar"
print(Fore.GREEN + f"O codigo de colaborador 1 está definido como perfil {verf_vendedor}")

nome_da_base = navegador.find_element_by_xpath("/html/body/div[2]/div[3]/div[3]/span[2]").text
numero_da_base= navegador.find_element_by_xpath("/html/body/div[2]/div[3]/div[3]/span[2]/b").text
print(Fore.GREEN + f"Você está na base: {numero_da_base}")
print(f"Nome da Empresa:   {nome_da_base}")

validar_base = navegador.find_element_by_id("zt-empresa").text.split(" ")
if validar_base[0] == zetta_base:
    print("TESTE DE BASE ---------------------" + Fore.GREEN + "[Pass]")
else:
    print("TESTE DE BASE ---------------------" + Fore.RED + "[Fail]")
time.sleep(5)

navegador.close()

