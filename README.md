# Siggma
> Automatizando criação de logins nas novas base com python e selenium. --- Automatizador WEB

> Automatizando criação de bases novas para o PDV no postgreSQL --- Automatizando banco de dados

[![NPM Version][npm-image]][npm-url]
[![Build Status][travis-image]][travis-url]
[![Downloads Stats][npm-downloads]][npm-url]




## Instalção
WebDrivers(Linux):
Utilizado no script: Firefox
URL: <a>https://github.com/mozilla/geckodriver/releases</a>
Extrair para : ```/usr/local/bin```

Windows:
Extrair o arquivo banco_de_dados.rar e executar. Ele já contém todos os dados necessarios para rodar. 
```sh
https://chocolatey.org/install
choco install selenium-all-drivers
choco install selenium
```

Python:

```sh
pip install psycopg2  # Para o postgre_siggma
pip install selenium
```


## Utilização:
<p>-> Baixar a pasta automação web do repositorio</p>
<p>-> Baixar o Geecko WebDriver(Firefox). Caso utilize outro mudar na  siggma.py função entrar linha 16</p>
<p>-> Iniciar o terminal com python -i main_siggma.py </p>
<p>-> Com o terminal aberto para cadastrar usuario chamar .novousuario("nome do usuario")</p>
<p>...
<p>-> para fechar utilize .fechar_navegador()</p>




## Em Andamento

<p>Chamar tela no modo interativo</p>
<p>Definir usuario padrão</p>
<p>Criar tabela contabil padrão</p> 
<p>Criar plano de contas padrão generico</p>
<p>Teste de emissão NF-e</p>
<p>Teste servidor sefaz</p>
<p>Teste consultar busca de XML</p>
<p>Validador de informação.</p>



<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki
