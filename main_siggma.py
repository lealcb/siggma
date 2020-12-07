from siggma import Siggma
import time
zetta_login = str(input("Login: "))
zetta_senha = str(input("Senha: "))
zetta_base = str(input("Digite a base: "))
siggma = Siggma(zetta_login,zetta_senha,zetta_base)
siggma.entrar()
