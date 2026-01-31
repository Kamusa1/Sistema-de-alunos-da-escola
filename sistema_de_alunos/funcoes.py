import time
import sys
import uuid
from listas import alunos_cadastrado

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
    novos_alunos = {
        "id": uuid.uuid4(),
        "nome": nome,
        "idade": idade,
        "nota": nota
    }
    alunos_cadastrado.append(novos_alunos)
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
        posicao_inicio = alunos_cadastrado.index(input("Digite o nome do aluno que deseja remover: "))
        posicao_fim = posicao_inicio + 2
        del alunos_cadastrado[posicao_inicio:posicao_fim]
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
def media_geral():
    try:
        notas_alunos = [novos_alunos["nota"] for novos_alunos in alunos_cadastrado]
        soma = sum(notas_alunos)
        media = soma / len(notas_alunos)
        print(f"A media geral das notas é {media}")
        time.sleep(2.0)
        sair = int(input("Digite 0 para voltar a tela de menu."))
    except ZeroDivisionError:
        print("Erro. Lista está vazia!")
        time.sleep(1.5)