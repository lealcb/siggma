# Siggma
> Automatizando criação de logins nas novas base com python e selenium.
> Automatizando definição de perfil como vendedor em base nova
> Automatizando criação de bases novas para o PDV no postgreSQL

[![NPM Version][npm-image]][npm-url]
[![Build Status][travis-image]][travis-url]
[![Downloads Stats][npm-downloads]][npm-url]

1º Script É so colocar o codigo da base(junto do usuario e senha) que o mesmo já cadastrar um novo login.
2º Script é só definir a base que ele vai automaticamente definir o id colaborador 1 como perfil vendeedor
3º Script/EXE é so seguir as instruçoes do terminal que o mesmo irá criar o banco de dados novo. Utilizar o EXE quando for o windows. 



## Instalção
WebDrivers(Linux):
Utilizado no script: Firefox
URL: <a>https://github.com/mozilla/geckodriver/releases</a>
Extrair para : ```/usr/local/bin```

Windows:
Extrair o arquivo banco_de_dados.rar e executar. Ele já contém todos os dados necessarios para rodar. 
```sh
choco install selenium-all-drivers
choco install selenium
```

Python:

```sh
pip install psycopg2  # Para o postgre_siggma
pip install selenium
```


## Utilização:
-> Baixar o arquivo siggma.py e main_siggma.py
-> Baixar o Geecko WebDriver(Firefox). Caso utilize outro mudar na  siggma.py função entrar linha 16
-> Iniciar o terminal com python -i main_siggma.py 
-> Com o terminal aberto para cadastrar usuario chamar .novousuario("nome do usuario")
...
-> para fechar utilize .fechar_navegador()




## Em Andamento

Chamar tela no modo interativo
Definir usuario padrão
Criar tabela contabil padrão 
Criar plano de contas padrão generico
Teste de emissão NF-e
Teste servidor sefaz
Teste consultar busca de XML
Validador de informação.



<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki
