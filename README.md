# python-server
simple python back-end

# Pré-requisitos do projeto
*Execute na linha de comando*
1. Tenha python3
2. Tenha node 8+<br />
***Execute:***
* git clone git@github.com:lavesan/python-server.git
* npm i

# Rodando o projeto
Digite na linha de comando de algum terminal
> npm run start

Esse projeto usa nodemon, então é só salvar o arquivo que ele atualiza
# Instalando python3
* No próprio site
  * https://www.python.org/downloads/
* Com chocolatey **(windows)**
  * Abra o terminal do windows como administrador
  * Rode:
  ```bash
    @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
    ```
  * execute: choco install python3
