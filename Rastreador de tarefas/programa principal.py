import typer
from funções import *


app = typer.Typer()

@app.command()
def add(tarefa:str):
    adicionar(tarefa)


@app.command()
def list():
    listar()


if __name__ == '__main__':
    app()