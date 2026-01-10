import funcoes
import listas_de_alunos
while True:
    opcao = int(input("Sistema de Alunos da Escola:\n1. Adicionar aluno\n2. Listar todos os alunos\n3. Buscar aluno Pelo nome\n4. Remover aluno\n5. Mostrar média geral das notas\n6. Sair\n:"))
    match opcao:
        case 1:
            funcoes.adicionar_aluno()
            decisao = input("Deseja adicionar mais algum aluno?\nY - Sim\nN - Não(retorna a tela de menu)\n:")
            if decisao == "y":
                funcoes.adicionar_aluno()
            elif decisao == "n":
                continue
            else:
                print("Resposta invalida!")
        case 2:
            if not listas_de_alunos.alunos_cadastrado:
                print("A lista está vazia!")
            else:
                print(listas_de_alunos.alunos_cadastrado)
        case 3:
            funcoes.buscar_aluno()
            decisao = input("Deseja voltar?\n Y - Sim\nN - Não(retorna a tela do menu)\n:")
            if decisao == "y":
                funcoes.buscar_aluno()
            elif decisao == "n":
                continue
            else:
                print("Resposta invalida!")
        case 4:
            funcoes.remover_aluno()
            decisao = input("Deseja remover mais algum aluno?\n Y - Sim\nN - Não(retorna a tela do menu)\n:")
            if decisao == "y":
                funcoes.remover_aluno()
            elif decisao == "n":
                continue
            else:
                print("Resposta invalida!")
        case 5: