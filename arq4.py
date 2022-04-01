class Emprego:
    def __init__(self, nome, area, salario, bonus):
        self.cargo = nome
        self.area = area
        self.salario = salario
        self.bonus = bonus
        
class Pessoa:
    def __init__(self, nome, fone, email, emprego):
        self.nome = nome
        self.fone = fone
        self.email = email
        self.emprego = emprego
        self.dependentes = []

    def calcular_salario(self):
        porcentagem = len(self.dependentes) * self.emprego.bonus
        aumento = self.emprego.salario * porcentagem / 100
        return self.emprego.salario + aumento

emprego = Emprego("Programador", "TI", 1000, 5)
pessoa1 = Pessoa("Paulo", "11-99999999", "paulo@email.com", Emprego)

# dois dependentes (o dependente também é um objeto Pessoa)
dep1 = Pessoa("Maria", "", "", None)
dep2 = Pessoa("Joao", "", "", None)

# adiciona dependentes na lista de dependentes da pessoa1
pessoa1.dependentes.append(dep1)
pessoa1.dependentes.append(dep2)

print("Salario: ",pessoa1.calcular_salario()) 
