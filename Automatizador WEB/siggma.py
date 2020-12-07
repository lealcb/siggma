from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Siggma:
    def __init__(self, zetta_login,zetta_senha,zetta_base):
        self.zetta_login = zetta_login 
        self.zetta_senha = zetta_senha
        self.zetta_base = zetta_base
        
    def entrar(self):
        url = 'https://sistema.zettabrasil.com.br/siggma'
        self.navegador = Firefox()
        self.navegador.get(url)
        time.sleep(1)
        elemento = self.navegador.find_element_by_id("cpUser")
        elemento.click()
        elemento.clear()
        elemento.send_keys(self.zetta_login)
        senha_elemento = self.navegador.find_element_by_id("cpPwd")
        senha_elemento.click()
        senha_elemento.clear()
        senha_elemento.send_keys(self.zetta_senha)
        botao_elemento = self.navegador.find_element_by_id('btEnviar')
        botao_elemento.click()
        time.sleep(5)
        verificar_url = self.navegador.current_url
        try:
            if verificar_url == "https://sistema.zettabrasil.com.br/siggma/app/index/workbench":
                bloqueado_base_digitar = self.navegador.find_element_by_class_name("zt-info")
                bloqueado_base_digitar.click()
                bloqueado_digitar_base = self.navegador.find_element_by_xpath("/html/body/section[2]/div[1]/div[1]/div[2]/input")
                bloqueado_digitar_base.send_keys(self.zetta_base)
                time.sleep(2)
                clicar_na_base = self.navegador.find_element_by_css_selector(f"[data-id='{self.zetta_base}']").click()
                time.sleep(3)
                comercialModulo = self.navegador.find_element_by_css_selector(f"[data-id='3']").click()
                time.sleep(2)
            else:
                raw_base_clicar = self.navegador.find_element_by_id("zt-empresa").click()
                raw_base_digitar = self.navegador.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/input").send_keys(self.zetta_base)
                time.sleep(2)
                raw_base_procurar = self.navegador.find_element_by_css_selector(f"[data-id='{self.zetta_base}']").click()
        except Exception as e:
            print(e)
            print("Algo deu errado ao logar.")
            self.navegador.close()
    def vendedor_padrao(self):
        try:
            time.sleep(5)
            cmd = self.navegador.find_element_by_xpath("/html/body")
            cmd.send_keys(Keys.CONTROL + Keys.ALT + "C")
            cmd_comando = self.navegador.find_element_by_id("tSystemCmd")
            cmd_comando.clear()
            cmd.send_keys(Keys.CONTROL + Keys.ALT + "C")
            cmd_comando.send_keys("52")
            cmd_comando.send_keys(Keys.ENTER)
            time.sleep(5)
            btn_pesquisar = self.navegador.find_element_by_id("btnPesquisar").click()
            time.sleep(2)
            user_id_valid = self.navegador.find_element_by_xpath(f"//td[@title='1']").click() # Nao esquecer de mudar para 1
            time.sleep(5)
            btn_alterar = self.navegador.find_element_by_id("btnAlterar").click()
            time.sleep(2)
            vend_padrao = self.navegador.find_element_by_css_selector("#tabs-1 > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(7) > td:nth-child(2) > span:nth-child(2) > span:nth-child(1) > span:nth-child(1)").click()
            vend_padrao_text = self.navegador.find_element_by_xpath("//li[text()='VENDEDOR']").click()
            time.sleep(2)
            btn_salvar = self.navegador.find_element_by_id("btnPersistir").click()
        except Exception as e:
            print(e)
            print("Algo deu errado ao definir o perfil padrão do colaborador")
            self.navegador.close()
    def chamarjanela(self,codigojanela):
        cmd = self.navegador.find_element_by_xpath("/html/body")
        cmd.send_keys(Keys.CONTROL + Keys.ALT + "C")
        cmd_comando = self.navegador.find_element_by_id("tSystemCmd")
        cmd_comando.clear()
        cmd.send_keys(Keys.CONTROL + Keys.ALT + "C")
        cmd_comando.send_keys(f"{codigojanela}")
        cmd_comando.send_keys(Keys.ENTER)
    def trocarbase(self,base):
        verificar_url = self.navegador.current_url
        try:
            if verificar_url == "https://sistema.zettabrasil.com.br/siggma/app/index/workbench":
                bloqueado_base_digitar = self.navegador.find_element_by_class_name("zt-info")
                bloqueado_base_digitar.click()
                bloqueado_digitar_base = self.navegador.find_element_by_xpath("/html/body/section[2]/div[1]/div[1]/div[2]/input")
                bloqueado_digitar_base.send_keys(base)
                time.sleep(2)
                clicar_na_base = self.navegador.find_element_by_css_selector(f"[data-id='{base}']").click()
                time.sleep(3)
                comercialModulo = self.navegador.find_element_by_css_selector(f"[data-id='3']").click()
                time.sleep(2)
            else:
                raw_base_clicar = self.navegador.find_element_by_id("zt-empresa").click()
                raw_base_digitar = self.navegador.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/input").send_keys(base)
                time.sleep(2)
                raw_base_procurar = self.navegador.find_element_by_css_selector(f"[data-id='{base}']").click()
        except Exception as e:
            print(e)
            print("Algo deu errado ao logar.")
            self.navegador.close()
    def novousuario(self,nome_usuario):
            email_padrao = "suporte1@setcomp.com.br"
            login_padrao = nome_usuario + self.zetta_base
            senha_padrao = "setcomp2020"
            time.sleep(4)
            cmd = self.navegador.find_element_by_xpath("/html/body")
            cmd.send_keys(Keys.CONTROL + Keys.ALT + "C")
            cmd_comando = self.navegador.find_element_by_id("tSystemCmd")
            cmd_comando.clear()
            cmd.send_keys(Keys.CONTROL + Keys.ALT + "C")
            cmd_comando.send_keys("6")
            cmd_comando.send_keys(Keys.ENTER)
            time.sleep(3)
            botao_novo = self.navegador.find_element_by_id("btnNovo").click()
            time.sleep(2)
            cmp_nome = self.navegador.find_element_by_name("usUsrNom").send_keys(nome_usuario)
            cmp_email = self.navegador.find_element_by_name("usUsrEml").send_keys(email_padrao)
            cmp_login = self.navegador.find_element_by_name("usUsrLog").send_keys(login_padrao)
            cmp_senha = self.navegador.find_element_by_name("usUsrPwd").send_keys(senha_padrao)
            cmp_conf_senha = self.navegador.find_element_by_name("confPsw").send_keys(senha_padrao)
            try:

                cmp_filial = self.navegador.find_element_by_name(
                    "usempNumFil").send_keys("M")
                cmp_filial = self.navegador.find_element_by_name(
                    "usempNumFil").send_keys(Keys.ENTER)
                cmp_perfil = self.navegador.find_element_by_id(
                    "perfil").send_keys("P")
                cmp_perfil = self.navegador.find_element_by_id(
                    "perfil").send_keys(Keys.ENTER)
                cmp_status = self.navegador.find_element_by_name(
                    "usRegSta").send_keys("A")
                cmp_status = self.navegador.find_element_by_name(
                    "usRegSta").send_keys(Keys.ENTER)
            except Exception  as E:
                print(E)
            btn_salvar = self.navegador.find_element_by_id("btnPersistir").click()
            time.sleep(2)
            btn_poup_ok = self.navegador.find_element_by_id("btnOk").click()
            time.sleep(2)
    def fechar_navegador(self):
        self.navegador.close()