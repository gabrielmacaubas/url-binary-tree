'''
Classe para instanciação de nós que vão ficar na memória
'''
class TreeException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class Node:
    def __init__(self,data:object):
        self.__data = data
        self.__leftChild = None
        self.__rightChild = None

    @property
    def data(self)->object:
        return self.__data

    @data.setter
    def data(self, newData:object):
        self.__data = newData

    @property
    def leftChild(self)->'Node':
        return self.__leftChild

    @leftChild.setter
    def leftChild(self, newLeftChild:object):
        self.__leftChild = newLeftChild

    @property
    def rightChild(self)->'Node':
        return self.__rightChild

    @rightChild.setter
    def rightChild(self, newRightChild:'Node'):
        self.__rightChild = newRightChild

    def insertLeft(self, data:object):
        if self.__leftChild == None:
            self.__leftChild = Node(data)	

    def insertRight(self,data:object):
        if self.__rightChild == None:
            self.__rightChild = Node(data)

    def __str__(self):
        return str(self.__data)

    def hasLeftChild(self)->bool:
        return self.__leftChild != None

    def hasRightChild(self)->bool:
        return self.__rightChild != None
        
	    
'''
Classe para a instanciação de Árvores Binárias
Autor: Alex Sandro
Data da última modificação: 11/05/2022
'''
class BinaryTree:
    # constructor that initializes an empty Tree 
    def __init__(self, data_root:object):
        self.__root = Node(data_root)
        self.string = ""

    def getRoot(self)->'Node':
        '''Obtem a referência para o nó "root"'''
        return self.__root

    def addLeft(self, target_key, data ):   
        if target_key.leftChild is None:
            target_key.leftChild = Node(data)

    def addRight(self, target_key, data ):
        if target_key.rightChild is None:
            target_key.rightChild = Node(data)
        
    def getNode(self, key ):
        root_str = self.getRoot().data.strip()
        if key == root_str:
            return self.getRoot()
        
        return self.__getNode(key, self.getRoot())

    def __getNode(self, key, node:Node)->Node:
        
        if (node == None):
            return None # Nao encontrou a chave

        if ( key == node.data):
            return node

        returnedNode = self.__getNode( key, node.leftChild)

        if ( returnedNode):
            return returnedNode
        else:
            return self.__getNode( key, node.rightChild)

    def search(self, chave:object )->bool:
        '''Realiza uma busca na árvore pelo nó cuja carga é igual à chave
           passada como argumento.
           Returns
           ---------
           True: caso a chave seja encontrada na árvore
           False: caso a chave não esteja na árvore
        '''
        return self.__searchData(chave, self.__root)
    
    def __searchData(self, chave, node):
        if (node == None):
            return False # Nao encontrou a chave
        if ( chave == node.data):
            return True
        elif ( self.__searchData( chave, node.leftChild)):
            return True
        else:
            return self.__searchData( chave, node.rightChild)

    def preorderTraversal(self):
        '''Exibe os nós da árvore com percurso em pré-ordem'''
        self.__preorder(self.__root)

    def inorderTraversal(self):
        '''Exibe os nós da árvore com percurso em in-ordem'''
        self.__inorder(self.__root)

    def postorderTraversal(self):
        '''Exibe os nós da árvore com percurso em pós-ordem'''
        self.__postorder(self.__root)
        
    def __preorder(self, node):
        if( node == None):
            return

        print(f'{node.data}')

        self.__preorder(node.leftChild)
        self.__preorder(node.rightChild)

    def __inorder(self, node):
        if( node == None):
            return
        self.__inorder(node.leftChild)
        print(f'{node.data} ',end='')
        self.__inorder(node.rightChild)

    def __postorder(self, node):
        if( node == None):
            return
        self.__postorder(node.leftChild)
        self.__postorder(node.rightChild)
        print(f'{node.data} ',end='')

    def viewtree(self):
        '''Método utilizado para exibir toda árvore carregando também os ancestrais de cada nó'''
        ancestrais = []
        
        self.__viewtree(self.__root, ancestrais)
    
    def __viewtree(self, node, ancestrais):
        if( node == None):
            return

        ancestrais.append(node.data)

        for i in ancestrais:
            print(f"{i}/", end="")

        print()

        self.__viewtree(node.leftChild, ancestrais)
        self.__viewtree(node.rightChild, ancestrais)

        ancestrais.pop()
    
    def match(self, url):
        '''Verificação para validar a existência de uma url na árvore'''
        try:
            return self.__match(self.__root, url)
        except IndexError:
            raise TreeException('URL inválida.')
    
    def __match(self, node, url):
        if node.data == url[0]:
            url.pop(0)
            if len(url) == 0:
                return node
            #verifica se o nó é igual ao filho esquerdo ou direito antes de entrar na recursividade
            if node.hasLeftChild():
                if node.leftChild.data == url[0]: 
                    return self.__match(node.leftChild, url)

            if node.hasRightChild():
                if node.rightChild.data == url[0]:
                    return self.__match(node.rightChild, url)
            
            else:
                return

        return

    def deleteTree(self):
        '''Elimina todos os nós da árvore'''
        # garbage collector fará o trabalho de eliminação dos nós
        # abandonados 
        self.__root = None

    def __deleteNode(self,root, key):

        if root is None: 
            return
        elif root.leftChild == None and root.rightChild == None:
            return
        
        if root.leftChild == None:
            if root.rightChild.data == key:
                root.rightChild = None
        elif root.rightChild == None:
            if root.leftChild.data == key:
                root.leftChild = None
