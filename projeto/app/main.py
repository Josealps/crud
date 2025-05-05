from database import conecta, encerrar_session
import uuid


def main():
    
    connection = conecta()
    cursor = connection.cursor()

    def insert_usuarios(nome, idade, email, numero):
        cmd_insert = "INSERT INTO crud (nome, idade, email, numero) VALUES (%s,%s,%s,%s ); "
        id = uuid.uuid4()
        values = id,nome, idade, email, numero
        cursor.execute(cmd_insert, values)
        connection.commit()
        print("Os dados Foram Inseridos Com Sucesso!")

    def select(id = None):
        if id:
            cmd_select = "SELECT nome, idade, email, numero FROM crud WHERE id = '{id}'; "
        else:
             cmd_select = "SELECT nome, idade, email, numero FROM crud;"
        cursor.execute(cmd_select)
        cruds = cursor.fetchall()
        for crud in cruds:
            print (crud)
        return cruds
    
    def update(novo_nome,nova_idade,novo_email,novo_numero, id):
        cmd_update = f"UPDATE crud SET nome = '{novo_nome}', idade = '{nova_idade}', email = '{novo_email}', numero = '{novo_numero}' WHERE id = {id}"
        cursor.execute(cmd_update)
        connection.commit()

    
    def delet(id):
        cmd_delete = f"DELETE FROM crud WHERE id= {id} "
        cursor.execute(cmd_delete)
        connection.commit()
        print("Dados Deletados com Sucesso!!")

    while True:
        print("Escolha uma Opção: ")
        print("1. Inserir Usuário")
        print("2. Selecionar Usuário")
        print("3. Atualizar Usuário")
        print("4. Deletar Usuário")
        print("5. Sair")
        opcao = input("Digite um número da opções: ")
         
        if opcao == "1":
            nome = str(input("Insira o Nome do Usuário: "))
            idade = int(input("insira a Idade do Usuário: "))
            email = input("insira o Email do Usuário: ")
            numero = int(input("Insira o Numero do Usuário"))
            insert_usuarios(nome, idade, email, numero)

        elif opcao == "2":
            id = input("Digite o Id do Usuário que deseja conferir: ")
            select(id)

        elif opcao == "3":
            id = input("insira o ID do cliente que deseja atualizar: ")
            novo_nome = str(input("Insira o Novo Nome do Usuário: "))
            nova_idade = int(input("insira a  Nova Idade do Usuário: "))
            novo_email = input("insira o  Novo Email do Usuário: ")
            novo_numero = int(input("Insira o Novo Numero do Usuário"))
            update(novo_nome,nova_idade,novo_email,novo_numero)

        elif opcao == "4":
            id = input("insira o ID do Usuário que deseja Deletar: ")
            delet(id)
        elif opcao == "5":
            print("Saindo...Adeus")
            break
        else:
            print("Opção Invalida, Por favor tente novamente!")
        


