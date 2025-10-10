'''
    Orientação a Objetos:
        É um paradigma de programação (estilo/forma) de programar, utilizando
    determinadas estruturas, tipos de dados e funcinalidades. Python é uma
    linguagem multiparadigma(estruturado, funcional e orientado a objetos).

    Conceitos de classes e objetos:
        As classes são modelos abstratos que vao representar itens do mundo
    real dentro de um software. E os objetos são as ocorrencias dessas classes
    carregadas na memoria efetivamente existindo pra valer.

'''

# ENCAPSULAMENTO:

# Exemplo:


class Veiculo:
    def movimentar(self):
        print("Sou um veiculo e me desloco.")

    def __init__(self, fabricante, modelo):
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__num_registro = None

# Setter
    def set_numero_registro(self, registro):
        self.__num_registro = registro

# Getter
    def get_fabricante_modelo(self):
        print(f"{self.__fabricante} - {self.__modelo}")

    def get_numero_registro(self):
        return self.__num_registro


# HERANÇA e POLIMORFISMO:
class Carro(Veiculo):
    # O metodo __init__ não será herdado.
    def movimentar(self):
        print("Sou um carro e ando pelas ruas!")


class Motocicleta(Veiculo):
    def movimentar(self):
        print("Corro muito!")


class Aviao(Veiculo):
    def __init__(self, fabricante, modelo, categoria):
        self.__cat = categoria
        super().__init__(fabricante, modelo)

    def get_categoria(self):
        return self.__cat

    def movimentar(self):
        print("Eu voo alto!")


if __name__ == '__main__':
    meu_veiculo = Veiculo('GM', 'Cadillac Escalade')
    meu_veiculo.movimentar()
    meu_veiculo.get_fabricante_modelo()
    meu_veiculo.set_numero_registro('490321-1')
    print(f"Registro: {meu_veiculo.get_numero_registro()}\n")

    meu_carro = Carro("Volkwagen", "Polo")
    meu_carro.movimentar()
    meu_carro.get_fabricante_modelo()
    print()
    seu_carro = Carro("Audi", "A5 SportBack")
    seu_carro.movimentar()
    seu_carro.get_fabricante_modelo()
    print()
    moto = Motocicleta("Harley-Davidson", "Nighster Special")
    moto.movimentar()
    moto.get_fabricante_modelo()
    print()
    meu_aviao = Aviao("Boing", "747", "Comercial")
    meu_aviao.movimentar()
    meu_aviao.get_fabricante_modelo()
    print(f"Categoria: {meu_aviao.get_categoria()}\n")
