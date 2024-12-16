import typer
import json
from pathlib import Path

app = typer.Typer() 

caminho_do_arquivo = "/home/john/Trabalho/Storm/Projetos Back-end/Rastreador de tarefas/task.json"

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
    print("Formato do JSON corrigido com sucesso!")

#FUNÇÃO PARA ADICIONAR TAREFAS:
def adicionar(tarefa: str):
    if Path(caminho_do_arquivo).exists():
        try:
            with open(caminho_do_arquivo, "r") as doc:
                tarefas = json.load(doc)
        except json.JSONDecodeError:
            print("Erro: o arquivo JSON está corrompido. Criando um novo arquivo.")
    else:
        tarefas = []

    #Adicionar a nova tarefa no arquivo json
    tarefas.append(tarefa)

    #salvar as tarefas de volta no arquivo json
    with open(caminho_do_arquivo, "w") as doc:
        json.dump(tarefas, doc, indent=4)
    print(f"A tarefa '{tarefa}' foi adicionada com sucesso!")
    
    
#Função para listar as tarefas:
def listar():
    corrigir_formato_json()
    if Path(caminho_do_arquivo).exists():
        with open(caminho_do_arquivo, "r") as doc:
            tarefas = json.load(doc)
            print("Tarefas: ")
            for i, tarefa in enumerate(tarefas,1):
                print(f"{i}. {tarefa}")
    else:
        print("Nenhuma tarefa encontrada")


#Função para remover tarefas:
def remover(tarefa: str):
    corrigir_formato_json()
    if Path(caminho_do_arquivo).exists():
        try:
            with open(caminho_do_arquivo, "r") as doc:
                tarefas = json.load(doc)
        except json.JSONDecodeError:
            print("Erro: arquivo JSON corrompido. Criando um novo arquivo.")
    else: 
        tarefas = []
    try:
        tarefas.remove(tarefa)
        with open(caminho_do_arquivo, "w") as doc:
            json.dump(tarefas, doc, indent=4)
        print(f"A tarefa '{tarefa}' foi removida com sucesso!")
    except:
        print("Tarefa não encontrada, tente novamente.")


#Função para atualizar uma tarefa:
def atualizar(indice_da_tarefa:int, nova_tarefa:str):
    corrigir_formato_json()
    if Path(caminho_do_arquivo).exists():
        try:
            with open(caminho_do_arquivo, "r") as doc:
                tarefas = json.load(doc)
        except json.JSONDecodeError:
            print("Erro: arquivo JSON corrompido. Criando um novo arquivo.")
    else: 
        tarefas = []
    
    try:
        tarefas[indice_da_tarefa-1] = nova_tarefa
        with open(caminho_do_arquivo, 'w') as doc:
            json.dump(tarefas, doc, indent=4)
        print(f'A tarefa de {indice_da_tarefa} foi modificada com sucesso.')
        listar()
    except json.JSONDecodeError:
        print("A tarefa não foi modificada, tente novamente.")


#Função pra marcar a tarefa como concluída:
corrigir_formato_json()
def marcar_como_concluida(indice_da_tarefa:int, novo_status:str): 
    #Validar o status inserido
    status_validos = ["done", "in-progress", "not-started"]
    if novo_status not in status_validos:
        print("Erro. status inválido.")
        return
    #Parte que verifica se o caminho do arquivo é válido:
    if Path(caminho_do_arquivo).exists():
        try:
            with open(caminho_do_arquivo, "r") as doc:
                tarefas = json.load(doc)
        except json.JSONDecodeError:
            print("Erro: arquivo JSON corrompido. Criando novo arquivo.")
    else:
        tarefas = []
    
    #Atualizar o status da tarefa:
    try:
        tarefa = tarefas[indice_da_tarefa - 1]
        if isinstance(tarefa, dict):
            tarefa['status'] = novo_status
        else:
            print("Erro: estrutura de tarefa inválida. Atualização do formato JSON necessária.")
            return
        
        #Salvar de volta no arquivo:
        with open(caminho_do_arquivo, "w") as doc:
            json.dump(tarefas, doc, indent=4)
        print(f"Tarefa '{tarefa['tarefa']}' atualizada para status '{novo_status}'.")
    except IndexError:
        print("Erro: índice da tarefa inválido.")