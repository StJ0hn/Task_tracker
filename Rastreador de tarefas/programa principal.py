import typer
from funções import *


app = typer.Typer()

@app.command()
def add(tarefa:str):
    adicionar(tarefa)


@app.command()
def list():
    listar()

@app.command()
def remove(tarefa:str):
    remover(tarefa)    

@app.command()
def update(indice_da_tarefa:int, nova_tarefa:str):
    atualizar(indice_da_tarefa, nova_tarefa)

@app.command()
def mark(indice_da_tarefa:int, status:str):
    marcar_como_concluida(indice_da_tarefa, status)

if __name__ == '__main__':
    app()