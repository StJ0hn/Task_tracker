import typer
import json
from pathlib import Path

app = typer.Typer() 

caminho_do_arquivo = "/home/john/Trabalho/Storm/Projetos Back-end/Rastreador de tarefas/task.json"

#FUNÇÃO PARA ADICIONAR TAREFAS:
def adicionar(tarefa: str):
    if Path(caminho_do_arquivo).exists():
        try:
            with open(caminho_do_arquivo, "r") as f:
                tarefas = json.load(f)
        except json.JSONDecodeError:
            print("Erro: o arquivo JSON está corrompido. Criando um novo arquivo.")
    else:
        tarefas = []

    #Adicionar a nova tarefa no arquivo json
    tarefas.append(tarefa)

    #salvar as tarefas de volta no arquivo json
    with open(caminho_do_arquivo, "w") as f:
        json.dump(tarefas, f, indent=4)
    
    print(f"A tarefa '{tarefa}' foi adicionada com sucesso!")




#Função para listar as tarefas:
def listar():
    if Path(caminho_do_arquivo).exists():
        with open(caminho_do_arquivo, "r") as f:
            tarefas = json.load(f)
            print("Tarefas: ")
            for i, tarefa in enumerate(tarefas,1):
                print(f"{i}. {tarefa}")
    else:
        print("Nenhuma tarefa encontrada")



