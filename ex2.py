from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Veterinario:
    def examinar(self, animal): 
        animal.emitir_som()
 

class Cachorro(Animal):
    def emitir_som(self):
        print("au au")

class Gato(Animal):
    def emitir_som(self):
        print("miau miau")

class Cavalo(Animal):
    def emitir_som(self):
        print("cavalo")

dog = Cachorro("Rex", 3)
horse = Cavalo("Horse", 6)
cat = Gato("Tina", 1)

dog.emitir_som()          # exibe o som do cachorro
horse.emitir_som()        # exibe o som do cavalo
cat.emitir_som()          # exibe o som do gato

vet = Veterinario()
vet.examinar(dog)         # exibe o som do cachorro 
vet.examinar(horse)       # exibe o som do cavalo 
vet.examinar(cat)         # exibe o som do gato
