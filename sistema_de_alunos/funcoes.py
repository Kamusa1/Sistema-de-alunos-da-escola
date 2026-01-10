import time
import sys
from listas_de_alunos import alunos_cadastrado

def adicionar_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    while True:
        try:
            nota = float(input("Digite a nota do aluno(0 a 10): "))
            if nota >= 0 and nota <= 10:
                break
            else:
                print("Erro!: Valor deve ser escrito entre 0 e 10.")
        except ValueError:
            print("Erro!: Valor digitado invalido.")
    alunos_cadastrado.append(nome)
    alunos_cadastrado.append(idade)
    alunos_cadastrado.append(nota)
    segundos = 0
    while True:
        sys.stdout.write('\rCarregando.')
        sys.stdout.flush()
        time.sleep(0.4)
        sys.stdout.write('\rCarregando..')
        sys.stdout.flush()
        time.sleep(0.4)
        sys.stdout.write('\rCarregando...')
        sys.stdout.flush()
        time.sleep(0.4)
        segundos += 1
        if segundos == 3:
            break
    sys.stdout.write('\rPronto. Aluno Cadastrado Com Sucesso!\n')
    sys.stdout.flush()

def buscar_aluno():
    try:
        posicao_nome = alunos_cadastrado.index(input("Digite o nome do aluno que deseja buscar: "))
        posicao_idade = posicao_nome + 1
        posicao_nota = posicao_idade + 1 

        print(f"Aluno encontrado!: Nome: {alunos_cadastrado[posicao_nome]} Idade: {alunos_cadastrado[posicao_idade]} Nota: {alunos_cadastrado[posicao_nota]}")
    except ValueError:
        print("Aluno não encontrado. Nome digitado errado ou Aluno não cadastrado.")

def remover_aluno():
    try:
        posicao_nome = alunos_cadastrado.index(input("Digite o nome do aluno que deseja remover: "))
        posicao_idade = posicao_nome + 1
        posicao_nota = posicao_idade + 1
        del alunos_cadastrado[posicao_nome]
        del alunos_cadastrado[posicao_idade]
        del alunos_cadastrado[posicao_nota] 
        segundos = 0
        while True:
            sys.stdout.write('\rCarregando.')
            sys.stdout.flush()
            time.sleep(0.4)
            sys.stdout.write('\rCarregando..')
            sys.stdout.flush()
            time.sleep(0.4)
            sys.stdout.write('\rCarregando...')
            sys.stdout.flush()
            time.sleep(0.4)
            segundos += 1
            if segundos == 3:
                break
        sys.stdout.write('\rPronto. Aluno Removido Com Sucesso!\n')
        sys.stdout.flush()
    except ValueError:
        print("Erro. Aluno Não encontrado!")
    
