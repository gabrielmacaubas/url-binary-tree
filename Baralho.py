# Baralho = coleçao de cartas (lista de cartas)
from Carta import Carta
from PilhaEncadeada import Pilha
from random import sample


class BaralhoException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class Baralho:
    def __init__(self):
        self.baralho = list()
        self.__novo_baralho = None

        naipe = ["Ouro",    "Espada","Paus","Copas"]
        numeracao = ["As","2","3","4","5","6","7","8","9","10","valete","dama","rei"]


        for idx in range(len(naipe)):
            for id in numeracao:
                self.baralho.append(Carta(id, naipe[idx]))

    def __len__(self):
        return self.__novo_baralho.tamanho()

    def temCarta(self):
        if not self.__novo_baralho.estaVazia():
            return True

        return False
    
    def retirarCarta(self)->Carta:
        return self.__novo_baralho.desempilha()

    def embaralhar(self):
        baralho_embaralhado = sample(self.baralho, 52)

        self.__novo_baralho = Pilha()
        self.__novo_baralho.empilhaSerie(baralho_embaralhado)

    def imprime(self):
        print(self.__novo_baralho)


if __name__ == "__main__":
    b = Baralho()
    b.embaralhar()
    b.imprime()
    print("tem carta?", b.temCarta())
    for i in range(48):
        print(f'{b.retirarCarta()} foi desempilhado!')
    print("tem carta?", b.temCarta())
    b.imprime()
