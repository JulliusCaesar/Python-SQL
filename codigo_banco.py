import pymysql

# Inicia a conexão
conexao = pymysql.connect(host= 'localhost',db='consulta_avancada', user='root', passwd="R8rh4*o%G&gxvc87RVY")

# Criar um cursor
cursor = conexao.cursor()

# C => Create
# ---- Defino o filme
nome = 'Buuuu'
nota = 2
categoria = 5

#Definindo o Statment
sql = f"INSERT INTO filme(nome, nota, categoria) VALUES('{nome}', {nota}, {categoria});"
#---- Execute o comando
cursor.execute(sql)

# Executar a transação (statements realizados)
conexao.commit()

# R => Read

# ---- Definir minha Query
sql = "SELECT * FROM filme;"

# ---- Execute o comando
cursor.execute(sql)

# ---- Recuperar o valor da consulta
retorno = cursor.fetchall()
id_atual = -1
for registro in retorno:
    if registro[1] == nome:
        id_atual = registro[0]

if id_atual != -1:
    # U => Update
    # ---- Atualizo um dado
    nota = 0

    # ---- Definindo o Statment
    sql = f"UPDATE filme SET nota = {nota} WHERE id = {id_atual};"

    # ---- Execute o comando
    cursor.execute(sql)

    # Executar a transação (statements realizados)
    conexao.commit()

    # D => Delete
    # ---- Deletando um dado

    # ---- Definindo o Statment
    print(id_atual)
    sql = f"DELETE FROM filme WHERE id = {id_atual};"

    # ---- Execute o comando
    cursor.execute(sql)
    
    # Executar a transação (statements realizados)
    conexao.commit()

    # finalizar a conexão
    conexao.close()