from psycopg2 import connect
import sys
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os
import time
import shutil

current_local = os.getcwd() 
db_name_limpo = "\\base_limpa.backup" 
checking_folder = os.path.exists("C:\\ZettaBrasil")
value_check = True
if checking_folder != value_check:
    print("Pasta ZettaBrasil Não existe")
    time.sleep(5)
else:
    shutil.copy(f"{current_local}"+f"{db_name_limpo}" , "C:\\ZettaBrasil") 

pasta = str(input("Defina o nome da pasta: "))
checking_folder = os.path.exists("C:\\ZettaBrasil\\ZettaNFCe")
checking_folder2 = os.path.exists("C:\\ZettaBrasil\\ZettaSAT")
if checking_folder is value_check:
    os.chdir("C:\\ZettaBrasil")
    shutil.copytree("C:\\ZettaBrasil\\ZettaNFCe",f"C:\ZettaBrasil\\{pasta}") 
    time.sleep(40)
elif checking_folder2 is value_check:
    os.chdir("C:\\ZettaBrasil")
    shutil.copytree("C:\\ZettaBrasil\\ZettaSAT",f"C:\ZettaBrasil\\{pasta}") 
    time.sleep(40)
else:
    print("Pasta do PDV não LOCALIZADA")
    time.sleep(5)

# Definir o .ini   
db_novo = str(input("Digite o nome do database: ")) 
db = open(f"C:\\ZettaBrasil\\{pasta}\\Config.ini","w+") 
for i in range(1):
	db.write(f"[Conexao]\nDriver=PG\nHost=127.0.0.1\nDatabase={db_novo}\nPorta=5434\nUsuario=postgres\nVersaoFB=30")

# Conexão com o banco
con = None 
con = connect(dbname='postgres',user='postgres', host = 'localhost', password='p057gre5',port=5434) 
con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) 
cur = con.cursor() 
cur.execute('CREATE DATABASE ' + db_novo) 
cur.close() 	
con.close() 
time.sleep(40)

novo_bat = open("C:\\ZettaBrasil\\PostgreSQL\\bin\\restore.bat","w")
novo_bat.write(f'pg_restore.exe -h localhost -p 5434 -U postgres -d {db_novo} -v "C:\\ZettaBrasil\\base_limpa.backup"') 
novo_bat.close()

print("SENHA DO BANCO: p057gre5")
time.sleep(5)
os.chdir("C:\\ZettaBrasil\\PostgreSQL\\bin")
os.startfile("restore.bat") 

print("Finalizou a importanção do banco de dados?")
print("Digite somente numero. E DIGITE NÃO SOMETNE SE HOUVE ERRO NO POSTGRE, COMO ERROU SENHA E NÃO EXIBIU RESTORE NA TELA. CASO CONTRARIO\nPRESSIONE 1 para SIM")
print("\n[1] ----- SIM")
print("[2] ----- NÃO")
try:
    resposta = int(input("Digite o codigo: "))
except Exception as e:
    print(e)
if resposta == 1:
    atalho = str(input("Define o nome do atalho: ")) 
    atalho_bat = open(f"C:\\ZettaBrasil\\{pasta}\\atalho.bat","w")
    atalho_bat.write(f'@echo off\n\nset SCRIPT="%TEMP%\\%RANDOM%-%RANDOM%-%RANDOM%-%RANDOM%.vbs"\n\necho Set oWS = WScript.CreateObject("WScript.Shell") >> %SCRIPT%\necho sLinkFile = "%USERPROFILE%\\Desktop\\{atalho}.lnk" >> %SCRIPT%\necho Set oLink = oWS.CreateShortcut(sLinkFile) >> %SCRIPT%\necho oLink.TargetPath = "C:\\ZettaBrasil\\{pasta}\\ZettaNFCe.exe" >> %SCRIPT%\necho oLink.Save >> %SCRIPT%\n\ncscript /nologo %SCRIPT%\ndel %SCRIPT%') 
    atalho_bat.close() 
    os.chdir(f"C:/ZettaBrasil/{pasta}") 
    os.startfile("atalho.bat") 

    os.chdir(f"C:/ZettaBrasil/{pasta}")
    os.startfile("AtualizadorBDZettaNFCe.exe") 
    time.sleep(20)
    os.chdir(f"C:/ZettaBrasil/{pasta}")
    os.startfile("AtualizadorBDZettaNFCe.exe")
elif resposta == 2:
    print("SENHA DO BANCO: p057gre5")
    time.sleep(5)
    os.chdir("C:\\ZettaBrasil\\PostgreSQL\\bin")
    os.startfile("restore.bat") 
    time.sleep(30)
    
    atalho = str(input("Define o nome do atalho: ")) 
    atalho_bat = open(f"C:\\ZettaBrasil\\{pasta}\\atalho.bat","w")
    atalho_bat.write(f'@echo off\n\nset SCRIPT="%TEMP%\\%RANDOM%-%RANDOM%-%RANDOM%-%RANDOM%.vbs"\n\necho Set oWS = WScript.CreateObject("WScript.Shell") >> %SCRIPT%\necho sLinkFile = "%USERPROFILE%\\Desktop\\{atalho}.lnk" >> %SCRIPT%\necho Set oLink = oWS.CreateShortcut(sLinkFile) >> %SCRIPT%\necho oLink.TargetPath = "C:\\ZettaBrasil\\{pasta}\\ZettaNFCe.exe" >> %SCRIPT%\necho oLink.Save >> %SCRIPT%\n\ncscript /nologo %SCRIPT%\ndel %SCRIPT%') 
    atalho_bat.close() 
    os.chdir(f"C:/ZettaBrasil/{pasta}") 
    os.startfile("atalho.bat") 
    time.sleep(10)

    os.chdir(f"C:/ZettaBrasil/{pasta}")
    os.startfile("AtualizadorBDZettaNFCe.exe") 
    time.sleep(10)
    os.chdir(f"C:/ZettaBrasil/{pasta}")
    os.startfile("AtualizadorBDZettaNFCe.exe")
else:
    print ("Comando inválido")
