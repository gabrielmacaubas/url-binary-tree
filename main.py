from BinaryTree import BinaryTree
from pathlib import Path
from BinaryTree import TreeException

path = Path(__file__).parent.resolve()
arvores = {}

def add(url):
    '''Método para adicionar uma nova árvore ou um novo nó em uma árvore existente'''
    domain = url[0]

    #observa se já existe um domínio na árvore
    if domain not in arvores:
        arvores[domain] = BinaryTree(url[0])

    else:
        target = url[:-1] 
        new_data = url[-1]
        current_node = arvores[domain].match(target)
        match = arvores[domain].match(url)

        #verifica se há nós filhos disponíveis para alocar o novo nó
        if current_node and not match:
            if current_node.hasLeftChild() and current_node.hasRightChild():
                return False
            
            else:
                #verifica se o nó tem filho esquerdo ou direito para adicionar 
                if current_node.hasLeftChild():
                    arvores[domain].addRight(current_node, new_data)
                else:
                    arvores[domain].addLeft(current_node, new_data)

                return True
        else:
            print("Esta URL já existe.")

# CARGA INICIAL
with open(str(path)+'/db.txt', 'r', encoding='utf-8') as arquivo: 
    db = arquivo.readlines()
    
    for line in db:
        url = line.strip("\n").rsplit('/')
        add(url)

print("""Bem-vindo ao navegador MSG!

COMANDOS :

    add -> adiciona uma nova URL
    viewtree -> exibe a árvore selecionada
    match -> verifica se a URL digitada existe
    sair -> encerra o programa""")

#tratamento dos métodos em comandos
while True:
    tokens = input("\n>>>").lower().split()
    print()
    command = tokens[0]

    if command == "sair":
        break
    
    try:
        url = tokens[1].rsplit('/')
        domain = url[0]
    except IndexError:
        print("Digite uma URL válida.")
    
    if command == "add":
        try:
            addition = add(url)
            if addition:

                print(f"""A URL: {tokens[1]}
foi adicionado com sucesso!""")
            else:
                print("Não há mais espaço para adição nesta subárvore.")
        except TreeException as te:
            print(te)

    elif command == "viewtree":
        arvores[domain].viewtree()
    
    elif command == "match":
        if domain not in arvores:
            print(f"{domain} não é um endereço na árvore.")
            
        else: 
            match = arvores[domain].match(url)

            if match:
                print("\033[32m200 OK - Requisição bem-sucedida!\033[m")
            else:
                print("\033[31m400 Bad Request - Servidor não atendeu a requisição.\033[m")
    else:
        print("Digite um comando válido.")

print("\n---Encerramento do programa---")    
