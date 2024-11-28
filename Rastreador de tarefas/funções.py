import typer


lista_de_tarefas = []
#função para adicionar tarefas:
def adicao_de_tarefas(tarefa: str):
    lista_de_tarefas.append(tarefa)
    print(f"A tarefa: {tarefa} foi adicionada com sucesso!")

#Criando a interface de linha de comando
if __name__ == "__main__":
    typer.run(adicao_de_tarefas)