import typer
import json
from pathlib import Path

caminho_do_arquivo = "task.json"
#função para adicionar tarefas:
def adicao_de_tarefas(tarefa: str):
    if Path(caminho_do_arquivo).exists():
        with open(caminho_do_arquivo, "r") as f:
            tarefas = json.load(f)
    else:
        tarefas = []

    #Adicionar a nova tarefa no arquivo json
    tarefas.append(tarefa)

    #salvar as tarefas de volta no arquivo json
    with open(caminho_do_arquivo, "w") as f:
        json.dump(tarefas, f, indent=4)
    
    print(f"A tarefa '{tarefa}' foi adicionada com sucesso!")

#Criando a interface de linha de comando
if __name__ == "__main__":
    typer.run(adicao_de_tarefas)