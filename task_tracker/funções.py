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


#FUNÇÃO PARA ADICIONAR TAREFAS:
def adicionar(tarefa: str):
    corrigir_formato_json()  # Corrige o formato antes de adicionar a tarefa

    if Path(caminho_do_arquivo).exists():
        try:
            with open(caminho_do_arquivo, "r") as doc:
                tarefas = json.load(doc)
        except json.JSONDecodeError:
            print("Erro: o arquivo JSON está corrompido. Criando um novo arquivo.")
    else:
        tarefas = []

    # Adicionar a nova tarefa no arquivo JSON
    tarefas.append({"tarefa": tarefa, "status": "not-started"})

    # Salvar as tarefas de volta no arquivo JSON
    with open(caminho_do_arquivo, "w") as doc:
        json.dump(tarefas, doc, indent=4)
    print(f"A tarefa '{tarefa}' foi adicionada com sucesso!")

    
    
#Função para listar as tarefas:
def listar():
    corrigir_formato_json()  # Corrige o formato antes de listar as tarefas

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

    if Path(caminho_do_arquivo).exists():
        try:
            with open(caminho_do_arquivo, "r") as doc:
                tarefas = json.load(doc)
        except json.JSONDecodeError:
            print("Erro: arquivo JSON corrompido. Criando um novo arquivo.")
    else:
        tarefas = []

    try:
        tarefas = [t for t in tarefas if t["tarefa"] != tarefa]
        with open(caminho_do_arquivo, "w") as doc:
            json.dump(tarefas, doc, indent=4)
        print(f"A tarefa '{tarefa}' foi removida com sucesso!")
    except:
        print("Tarefa não encontrada, tente novamente.")



#Função para atualizar uma tarefa:
def atualizar(indice_da_tarefa: int, nova_tarefa: str):
    corrigir_formato_json()  # Corrige o formato antes de atualizar a tarefa

    if Path(caminho_do_arquivo).exists():
        try:
            with open(caminho_do_arquivo, "r") as doc:
                tarefas = json.load(doc)
        except json.JSONDecodeError:
            print("Erro: arquivo JSON corrompido. Criando um novo arquivo.")
    else:
        tarefas = []

    try:
        tarefa = tarefas[indice_da_tarefa - 1]
        tarefa["tarefa"] = nova_tarefa
        with open(caminho_do_arquivo, 'w') as doc:
            json.dump(tarefas, doc, indent=4)
        print(f'A tarefa {indice_da_tarefa} foi modificada com sucesso.')
    except IndexError:
        print("Erro: índice da tarefa inválido.")



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

#Função para mostrar uma lista com as tarefas completas

def mostrar_tasks_concluidas():
    lista_das_tarefas_completas = []
    if Path(caminho_do_arquivo).exists():
        try:
            with open(caminho_do_arquivo, "r") as doc:
                tarefas = json.load(doc)
        except json.JSONDecodeError:
            print("Erro: arquivo JSON corrompido. Criando novo arquivo.")
    else:
        tarefas = []
#Checar quais tarefas estão marcadas como completas.
    for tarefa in tarefas:
        if tarefa['status'] == 'done':
            print("Tasks completeds: ")
            lista_das_tarefas_completas.append(tarefa['tarefa'])
            for i in lista_das_tarefas_completas:
                print(i)
    #salvando documento JSON:
    with open(caminho_do_arquivo, "w") as doc:
        json.dump(tarefas, doc, indent=4)


#Função para mostrar as tarefas em progresso
def mostrar_tasks_em_progresso():
    lista_de_tarefas_em_andamento = []
    if Path(caminho_do_arquivo).exists():
        try:
            with open(caminho_do_arquivo, 'r') as doc:
                tarefas = json.load(doc)
        except json.JSONDecodeError():
            print("Erro: arquivo JSON corrompido. Criando novo arquivo.")
    else:
        tarefas = []

    for tarefa in tarefas:
        if tarefa['status'] == 'in-progress':
            print('Tasks in-progress:')
            lista_de_tarefas_em_andamento.append(tarefa['tarefa'])
            for i in lista_de_tarefas_em_andamento:
                print(i)
    with open(caminho_do_arquivo, "w") as doc:
        json.dump(tarefas, doc, indent=4)

#Função para mostrar as tarefas não iniciadas:
def mostrar_tasks_nao_iniciadas():
    lista_de_tarefas_nao_iniciadas = []
    if Path(caminho_do_arquivo).exists():
        try:
            with open(caminho_do_arquivo, 'r') as doc:
                tarefas = json.load(doc)
        except json.JSONDecodeError():
            print("Erro: arquivo JSON corrompido. Criando novo arquivo.")
    else:
        tarefas = []

    for tarefa in tarefas:
        if tarefa['status'] == 'not-started':
            print('Tasks in-progress:')
            lista_de_tarefas_nao_iniciadas.append(tarefa['tarefa'])
            for i in lista_de_tarefas_nao_iniciadas:
                print(i)
    with open(caminho_do_arquivo, "w") as doc:
        json.dump(tarefas, doc, indent=4)