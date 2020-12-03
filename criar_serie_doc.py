from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
import time
from colorama import init
from colorama import Fore, Back, Style
from selenium.webdriver.support.ui import WebDriverWait, Select
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
        time.sleep(5)
        clicar_na_base = navegador.find_element_by_css_selector(f"[data-id='{zetta_base}']").click()
        time.sleep(5)
        comercialModulo = navegador.find_element_by_css_selector(f"[data-id='3']").click()
        time.sleep(5)
    else:
        time.sleep(5)
        raw_base_clicar = navegador.find_element_by_id("zt-empresa").click()
        raw_base_digitar = navegador.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/input").send_keys(zetta_base)
        time.sleep(2)
        raw_base_procurar = navegador.find_element_by_css_selector(f"[data-id='{zetta_base}']").click()
except Exception as e:
    print(e)
    print("Algo deu errado ao logar.")
    time.sleep(3)
    navegador.close()
##### Criar serie de documento fiscal #####
try:
    time.sleep(5)
    chamarjanela(45)
    time.sleep(5)
    row = '0'
    validar_row = navegador.find_elements_by_xpath("//table[@class='ui-jqgrid-btable ui-common-table']/tbody/tr")
    validar_number_row = len(validar_row) # Padrão é 2
    time.sleep(4) 
    if validar_number_row == 2:
        row = "1"
    elif validar_number_row == 3:
        row = '2'
    elif validar_number_row == 4:
        row = '3'
    else:
        print("Não é possivel cadastrar a series. Tem certeza que a base é nova?")
        time.sleep(3)
        navegador.close()

    var_add_serie = "_confserMod"
    num_serie = "_confserNum"
    row_num_serie = row + num_serie
    row_var_add_serie = row+var_add_serie
    
    var_next_row_2 = str(int(row) +1)
    second_num_row = var_next_row_2 + num_serie
    second_row = var_next_row_2 + var_add_serie
    
    var_next_row_3 = str(int(var_next_row_2) +1)
    third_num_row = var_next_row_3 + num_serie
    third_row = var_next_row_3 + var_add_serie
    ###      Serie SAT 59   ###
    navegador.find_element_by_id("btAddSerieNf").click()
    time.sleep(2)
    navegador.find_element_by_id(f"{row_var_add_serie}").click()
    select_serie = Select(navegador.find_element_by_id(f"{row_var_add_serie}"))
    select_serie.select_by_value('59') # SAT
    navegador.find_element_by_css_selector("#edit_jqg1 > td:nth-child(2)").click()
    navegador.find_element_by_id(f"{row_num_serie}").send_keys("1")
    navegador.find_element_by_id(f"{row_num_serie}").send_keys(Keys.ENTER)
    ###      Serie NOTA AVULSA 01   ###
    navegador.find_element_by_id("btAddSerieNf").click()
    time.sleep(2)
    navegador.find_element_by_id(f"{second_row}").click()
    select_serie = Select(navegador.find_element_by_id(f"{second_row}"))
    select_serie.select_by_value('01')
    navegador.find_element_by_css_selector("#edit_jqg2 > td:nth-child(2)").click()
    navegador.find_element_by_id(f"{second_num_row}").send_keys("1")
    navegador.find_element_by_id(f"{second_num_row}").send_keys(Keys.ENTER)
    ###      Serie NF-E 55   ###
    navegador.find_element_by_id("btAddSerieNf").click()
    time.sleep(2)
    navegador.find_element_by_id(f"{third_row}").click()
    select_serie = Select(navegador.find_element_by_id(f"{third_row}"))
    select_serie.select_by_value('55')
    navegador.find_element_by_css_selector("#edit_jqg3 > td:nth-child(2)").click()
    navegador.find_element_by_id(f"{third_num_row }").send_keys("1")
    navegador.find_element_by_id(f"{third_num_row }").send_keys(Keys.ENTER)

    ## Clicando no checking box ## 
    navegador.find_element_by_css_selector("#edit_jqg1 > td:nth-child(4) > input:nth-child(1)").click()
    navegador.find_element_by_css_selector("#edit_jqg2 > td:nth-child(4) > input:nth-child(1)").click()
    navegador.find_element_by_css_selector("#edit_jqg3 > td:nth-child(4) > input:nth-child(1)").click()
    time.sleep(2)
    navegador.find_element_by_id("btPersist").click() # Verificar a possibilidade de colocar wait elemeent para evitar possiveis problema.




  ''' Nota: Lembrar de remover todas as entradas do GRID antes de executar o codigo
      Talvez: Seja necessario usar o contador de ROW para verificar quantas linhas já tem e com isso selecionar elas e ir removendo uma a uma e logo em seguida executar 
      o bloco de codigo com a series assim evita duplicidade e e exception. 

      Nota 2: Criar funções para asa ROW e SERIES afimde diminuir o code.
      '''

except Exception as e:
    print(e)
    print("Algo deu errado!")
    navegador.close()
