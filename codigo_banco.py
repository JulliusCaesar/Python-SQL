import pymysql

# Conecta com o banco
def conectar_banco(_host, _db, _user, _passwd):
    # Cria uma conexão com o banco
    conexao = pymysql.connect(host= _host, db= _db, user= _user, passwd= _passwd)
    return conexao

# Devolve um cursor valido
def recuperar_cursor(conexao):
    # Criar um cursor
    cursor = conexao.cursor()
    return cursor

# Executar um statment
def executar_statment(conexao, cursor, sql):
    #---- Execute o comando
    cursor.execute(sql)
    # Executar a transação (statements realizados)
    conexao.commit()

# Executa uma query
def executar_query(conexao, cursor, sql):
    # ---- Execute o comando
    cursor.execute(sql)
    # ---- Recuperar o valor da consulta
    retorno = cursor.fetchall()
    return retorno

# Defino as informações de conexão
host = 'localhost'
db = 'consulta_avancada'
user = 'root'
passwd = 'R8rh4*o%G&gxvc87RVY'

# Pego a conexão com o banco
conexao = conectar_banco(host, db, user, passwd)

# Prgo o cursor
cursor = recuperar_cursor(conexao)

# Defino as informações do filme
nome = 'Buu'
nota = 4
categoria = 5
nova_nota = 0

# C => Create
# Defino o comando
sql_c = f"INSERT INTO filme(nome, nota, categoria) VALUES('{nome}', {nota}, {categoria});"
# Executo o comando
executar_statment(conexao, cursor, sql_c)

# R => Read
# Defino o coomando
sql_r = "SELECT * FROM filme;"
# Executo o comando
retorno = executar_query(conexao, cursor, sql_r)

id_atual = -1
for registro in retorno:
    if registro[1] == nome:
        id_atual = registro[0]

# U - Update
# Defino o coomando
sql_u = f"UPDATE filme SET nota = {nova_nota} WHERE id = {id_atual};"
# Executo o comando
executar_statment(conexao, cursor, sql_u)

# D => Delete
# Defino o coomando
sql_d = f"DELETE FROM filme WHERE id = {id_atual};"
# Executo o comando
# executar_statment(conexao, cursor, sql_d)