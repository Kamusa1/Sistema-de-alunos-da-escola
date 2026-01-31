import funcoes
import listas
from InquirerPy import inquirer
from time import sleep
def menu():
    while True:
        inicio = inquirer.select(
            message= "Sistema de alunos da escola:",
            choices= ["Adicionar alunos", "Listar todos os Alunos", "Buscar Alunos pelo nome", "Remover Aluno", "Mostrar Média geral dos Alunos", "Sair"]
        ).execute()

        match inicio:
            case "Adicionar alunos":
                funcoes.adicionar_aluno()
                decisao = inquirer.select(
                    message= "Deseja adicionar mais algum?",
                    choices= ["Sim", "Não"]
                ).execute()
                if decisao == "Sim":
                    funcoes.adicionar_aluno()
                elif decisao == "Não":
                    continue
            case "Listar todos os Alunos":
                if not listas.alunos_cadastrado:
                    print("A lista está vazia!")
                    sleep(4)
                    mensagem = inquirer.confirm(
                        message= "(aperte qualquer tecla para continuar)"
                    ).execute()
                else:
                    print(listas.alunos_cadastrado)
                    sleep(5)
                    mensagem = inquirer.confirm(
                        message="(aperte qualquer tecla para continuar)"
                    ).execute()
            case "Buscar Alunos pelo nome":
                funcoes.buscar_aluno()
                decisao = inquirer.select(
                    message= "Deseja voltar?",
                    choices=["Sim","Não"])
                if decisao == "Sim":
                    funcoes.buscar_aluno()
                elif decisao == "Não":
                    continue
                else:
                    print("Resposta invalida!")
            case "Remover Aluno":
                funcoes.remover_aluno()
                decisao = inquirer.select(
                    message="Deseja remover algum aluno?",
                    choices=["Sim", "Não"]
                )
                if decisao == "Sim":
                    funcoes.remover_aluno()
                elif decisao == "Não":
                    continue
                else:
                    print("Resposta invalida!")
            case "Mostrar Média geral dos Alunos":
                funcoes.media_geral()
            case "Sair":
                print("Fechando...")
                break
            case _:
                print("Resposta não indetificada.")
menu()