from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from colorama import init
from colorama import Fore, Back, Style

url = 'https://sistema.zettabrasil.com.br/siggma'
zetta_login = str(input("Login: "))
zetta_senha = str(input("Senha: "))
zetta_base = str(input("Digite a base: "))
nome_do_usuario = str(input("Digite o nome do usuario: "))
email_padrao = "suporte1@setcomp.com.br"
login_padrao = nome_do_usuario + zetta_base
senha_padrao = "setcomp2020"
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
time.sleep(5)
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

                                      ##### Cadastrar usuario #######

time.sleep(4)
chamarjanela("6")
time.sleep(3)
botao_novo = navegador.find_element_by_id("btnNovo").click()
time.sleep(2)
cmp_nome = navegador.find_element_by_name("usUsrNom").send_keys(nome_do_usuario)
cmp_email = navegador.find_element_by_name("usUsrEml").send_keys(email_padrao)
cmp_login = navegador.find_element_by_name("usUsrLog").send_keys(login_padrao)
cmp_senha = navegador.find_element_by_name("usUsrPwd").send_keys(senha_padrao)
cmp_conf_senha = navegador.find_element_by_name("confPsw").send_keys(senha_padrao)
try:

    cmp_filial = navegador.find_element_by_name(
        "usempNumFil").send_keys("M")
    cmp_filial = navegador.find_element_by_name(
        "usempNumFil").send_keys(Keys.ENTER)
    cmp_perfil = navegador.find_element_by_id(
        "perfil").send_keys("P")
    cmp_perfil = navegador.find_element_by_id(
        "perfil").send_keys(Keys.ENTER)
    cmp_status = navegador.find_element_by_name(
        "usRegSta").send_keys("A")
    cmp_status = navegador.find_element_by_name(
        "usRegSta").send_keys(Keys.ENTER)
except Exception  as E:
    print(E)
btn_salvar = navegador.find_element_by_id("btnPersistir").click()
time.sleep(2)
btn_poup_ok = navegador.find_element_by_id("btnOk").click()
time.sleep(2)




# Verificações
try:
    verf_login = navegador.find_element_by_xpath(f"//td[@title='{login_padrao}']")
    print(f"Usuario:{login_padrao} ------------ [Pass]")
    print(f"Senha:{senha_padrao}   ------------ [Pass]")
except Exception as e:
    print("Houve um erro para validar o usuario.")
    print(e)
    navegador.close()

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
time.sleep(5)
navegador.close()
 