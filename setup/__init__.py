"""
setup/__init__.py - inicializacao do pacote de configuracao do projeto.

Aqui fazemos o Django usar o PyMySQL como driver do MySQL.

Por que PyMySQL e nao mysqlclient?
  - O mysqlclient e uma extensao escrita em C. No Windows, o comando
    "pip install mysqlclient" costuma FALHAR, porque exige um compilador C
    e o MySQL Connector/C instalados.
  - O PyMySQL e escrito 100% em Python: instala igual no Linux (Arch/Ubuntu),
    no Windows e no macOS, sem precisar de nenhuma ferramenta de compilacao.

O backend MySQL do Django procura por um modulo chamado "MySQLdb". O comando
abaixo registra o PyMySQL nesse nome, e assim o Django passa a usa-lo sem que
o mysqlclient precise estar instalado.
"""

import pymysql

pymysql.install_as_MySQLdb()
