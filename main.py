from contato import Contato
from arquivo_services import *

print("-" * 30)
print(("-" * 3) + " Agenda de contatos TW " + ("-" * 3))
print("-" * 30)

opcao_menu = 1

while opcao_menu != 0:
    print("1. Listar contatos")
    print("2. Cadastrar contato")
    print("3. Remover contato")
    print("4. Buscar contato")
    print("0. Sair")
    opcao_menu = int(input("Digite a opção desejada: "))

    if opcao_menu == 1:
        contatos = listar_contatos()
        for contato_novo in contatos:
            print(f"Nome: {contato_novo.nome} / Email: {contato_novo.email} / Telefone: {contato_novo.telefone}")

    elif opcao_menu == 2:
        nome_contato = input("Digite o nome do contato: ")
        email_contato = input("Digite o email do contato: ")
        telefone_contato = input('Digite o telefone do contato: ')
        contato_novo = Contato(nome_contato, email_contato, telefone_contato)
        cadastrar_contato(contato_novo)

    elif opcao_menu == 3:
        contato_remover = input("Digite o email do contato que deseja remover: ")
        contato_encontrado = False
        with open("contatos.txt", "r") as arquivo:
            lista_contatos = arquivo.readlines()
            contatos = list()
            for i in lista_contatos:
                dados = (i.split("-"))
                if dados[1][1:-1] != contato_remover:
                    contatos.append(f"{dados[0]}-{dados[1]}-{dados[2]}")
                else:
                    contato_encontrado = True
            with open("contatos.txt", "w") as arquivo:
                arquivo.writelines(contatos)
            if not contato_encontrado:
                print("Contato não encontrado")

    elif opcao_menu == 4:
        contato_buscar = input("Digite o email do contato que deseja buscar: ")
        contato_encontrado = buscar_contato_email(contato_buscar)
        if contato_encontrado:
            print(f"Nome: {contato_encontrado.nome} / Email: {contato_encontrado.email} / Telefone: {contato_encontrado.telefone}")
        else:
            print("Contato não encontrado")

    elif opcao_menu == 0:
        print("Até breve!")
        break
    else:
        print("opcao invalida")
else:
    print("Obrigado por usar a agenda de contatos TW")
