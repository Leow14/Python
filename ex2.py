# #EX 1
# class Pessoa:
#     def __init__(self, identificador, nome):
#         self.identificador = identificador
#         self.nome = nome


# class PessoaJuridica(Pessoa):
#     def __init__(self, cnpj, nome, identificador):
#         super().__init__(identificador, nome)
#         self.cnpj = cnpj


# class PessoaFisica(Pessoa):
#     def __init__(self, rg, cpf, nome, identificador):
#         super().__init__(identificador, nome)
#         self.rg = rg
#         self.cpf = cpf

# EX 2

class Animal:
    def __init__(self, nome, cor, numero_patas):
        self.nome = nome
        self.cor = cor
        self.numero_patas = numero_patas

    def exibir_dados(self):
        print('Nome:', self.nome)
        print('cor', self.cor)
        print('numero_patas', self.numero_patas)


class Cachorro(Animal):
    def __init__(self, raca, nome, cor, numero_patas):
        super().__init__(nome, cor, numero_patas)
        self.raca = raca

    def exibir_dados(self):
        super().exibir_dados()
        print('raca', self.raca)


animal = Animal("Passarinho", "Azul", 2)
animal.exibir_dados()       # exibe os atributos do animal

dog = Cachorro("Rex", "Marrom", 4, "Vira lata")
dog.exibir_dados()          # exibe os atributos do cachorro
