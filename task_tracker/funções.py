import typer
import json
from pathlib import Path

app = typer.Typer() 

caminho_do_arquivo = "/home/john/Trabalho/Storm/Projetos Back-end/task_tracker/task.json"

def abertura_do_json():
    if Path(caminho_do_arquivo).exists():
        try:
            with open(caminho_do_arquivo, "r") as doc:
                tarefas = json.load(doc)
        except json.JSONDecodeError:
            print("Erro: o arquivo JSON está corrompido. Criando um novo arquivo.")
    else:
        tarefas = []
    return tarefas


def salvar_json(tarefas):
    with open(caminho_do_arquivo, "w") as doc:
            json.dump(tarefas, doc, indent=4)


#Correção do formato json:
def corrigir_formato_json():
    if Path(caminho_do_arquivo).exists():
        try:
            with open(caminho_do_arquivo, "r") as doc:
                tarefas = json.load(doc)
        except json.JSONDecodeError:
            print("Erro: arquivo JSON corrompido. Criando um novo arquivo.")
            tarefas = []
    else:
        print("Arquivo de tarefas não encontrado. Criando um novo arquivo.")
        tarefas = []

    # Verificar se as tarefas estão no formato antigo (strings simples)
    tarefas_corrigidas = []
    for tarefa in tarefas:
        if isinstance(tarefa, str):
            # Converter string simples para o novo formato
            tarefas_corrigidas.append({"tarefa": tarefa, "status": "not-started"})
        elif isinstance(tarefa, dict) and "tarefa" in tarefa and "status" in tarefa:
            # Já no formato correto
            tarefas_corrigidas.append(tarefa)
        else:
            print(f"Tarefa inválida encontrada no JSON: {tarefa}")

    # Salvar o JSON corrigido
    with open(caminho_do_arquivo, "w") as doc:
        json.dump(tarefas_corrigidas, doc, indent=4)



#FUNÇÃO PARA ADICIONAR TAREFAS:
def adicionar(tarefa: str):
    corrigir_formato_json()  # Corrige o formato antes de adicionar a tarefa
    tarefas = abertura_do_json()
    # Adicionar a nova tarefa no arquivo JSON
    tarefas.append({"tarefa": tarefa, "status": "not-started"})
    # Salvar as tarefas de volta no arquivo JSON
    salvar_json(tarefas)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")



#Função para listar as tarefas:
def listar():
    #Isso aqui é um bloco de código para abrir o documento json, mas é uma exceção.
    if Path(caminho_do_arquivo).exists():
        with open(caminho_do_arquivo, "r") as doc:
            tarefas = json.load(doc)
        print("Tarefas: ")
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa['tarefa']} - Status: {tarefa['status']}")
    else:
        print("Nenhuma tarefa encontrada")


#Função para remover tarefas:
def remover(tarefa: str):
    corrigir_formato_json()  # Corrige o formato antes de remover a tarefa
    tarefas = abertura_do_json()
    try:
        nova_lista = []
        for uma_tarefa in tarefas:
            if uma_tarefa['tarefa'] != tarefa:
                nova_lista.append(uma_tarefa) 
        salvar_json(nova_lista)
        print(f"A tarefa '{tarefa}' foi removida com sucesso!")
    except:
        print("Tarefa não encontrada, tente novamente.")



#Função para atualizar uma tarefa:
def atualizar(indice_da_tarefa: int, nova_tarefa: str):
    corrigir_formato_json()  # Corrige o formato antes de atualizar a tarefa
    tarefas = abertura_do_json()
    try:
        tarefa = tarefas[indice_da_tarefa - 1]
        tarefa["tarefa"] = nova_tarefa
        salvar_json(tarefas)
        print(f'A tarefa {indice_da_tarefa} foi modificada com sucesso.')
    except IndexError:
        print("Erro: índice da tarefa inválido.")


#Função pra marcar a tarefa como concluída:
def marcar_como_concluida(indice_da_tarefa:int, novo_status:str): 
    corrigir_formato_json()
    #Validar o status inserido
    status_validos = ["done", "in-progress", "not-started"]
    if novo_status not in status_validos:
        print("Erro. status inválido.")
        return
    #Parte que verifica se o caminho do arquivo é válido:
    tarefas = abertura_do_json()
    
    #Atualizar o status da tarefa:
    try:
        tarefa = tarefas[indice_da_tarefa - 1]
        if isinstance(tarefa, dict):
            tarefa['status'] = novo_status
        else:
            print("Erro: estrutura de tarefa inválida. Atualização do formato JSON necessária.")
            return
        
        #Salvar de volta no arquivo:
        salvar_json(tarefas)
        print(f"Tarefa '{tarefa['tarefa']}' atualizada para status '{novo_status}'.")
    except IndexError:
        print("Erro: índice da tarefa inválido.")


#Função para mostrar todos os status das tarefas:
def listar_por_status(status:str, mensagem:str):
    tarefas = abertura_do_json()
    lista_de_tarefas_filtradas =[]

    for tarefa in tarefas:
        if tarefa['status'] == status:
            lista_de_tarefas_filtradas.append(tarefa['tarefa'])
    if len(lista_de_tarefas_filtradas) > 0:
        print(mensagem)
        for tarefa in lista_de_tarefas_filtradas:
            print(tarefa)
    else:
        print(f"Nenhuma tarefa com o status '{status}' encontrada.")
        salvar_json(tarefas)