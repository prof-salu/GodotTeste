class Aluno:
    def __init__(self, nome, turma, n1, n2):
        self.__nome = nome
        self.__turma = turma
        self.__n1 = n1
        self.__n2 = n2
        self.__media = 0

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_turma(self):
        return self.__turma

    def set_turma(self, turma):
        if turma not in (701, 702, 703):
            print('Turma invalida')
        else:
            self.__turma = turma

    def set_n1(self, n1):
        self.__n1 = n1

    def set_n2(self, n2):
        self.__n2 = n2


    def calcula_media(self):
        self.__media = (self.__n1 + self.__n2) / 2

    def imprime_dados(self):
        print(f'Nome: {self.__nome}')
        print(f'Turma: {self.__turma}')
        print(f'N1: {self.__n1}')
        print(f'N2: {self.__n2}')
        print(f'Média: {self.__media}')
        print()

a1 = Aluno('Pedro', 701, 7, 6)

a1.imprime_dados()

a1.calcula_media()

a1.imprime_dados()

a1.imprime_dados()

print(a1.get_nome())

a1.set_nome('Pedro Albuquerque')

a1.imprime_dados()

print(a1.get_turma())

a1.set_n1(10)
a1.set_n2(7)

#print(a1.__n1)

a1.set_turma(800)

a1.imprime_dados()