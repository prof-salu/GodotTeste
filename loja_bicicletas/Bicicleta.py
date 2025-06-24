class Bicicleta:
    def __init__(self, modelo, fabricante, velocidade_maxima):
        self.modelo = modelo
        self.fabricante = fabricante
        self.marcha = 0
        self.velocidade = 0
        self.velocidade_maxima = velocidade_maxima

    def acelerar(self, valor):
        if valor > 0 :
            self.velocidade += valor

        if self.velocidade > self.velocidade_maxima:
            self.velocidade = self.velocidade_maxima


    def frear(self, valor):
        if valor > 0 :
            self.velocidade -= valor

        if self.velocidade < 0:
            self.velocidade = 0

    def imprimir_estados(self):
        print(f'Modelo: {self.modelo}')
        print(f'Fabricante: {self.fabricante}')
        print(f'Velocidade: {self.velocidade}')
        print(f'Marcha: {self.marcha}')
        print(f'Velocidade máxima: {self.velocidade_maxima}')
        print()



bike_01 = Bicicleta('Ranger', 'Monark', 30)

bike_01.imprimir_estados()

bike_01.acelerar(-45)

bike_01.imprimir_estados()

bike_01.acelerar(10)

bike_01.imprimir_estados()

bike_01.velocidade = -100

#bike_01.frear(-100)

bike_01.imprimir_estados()