class paciente:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

class medico:
    def __init__(self, nome, crm, especializacao):
        self.nome = nome
        self.crm = crm
        self.especializacao = especializacao

class Exame:
    def __init__(self, medico, paciente, descricao, resultado):
        self.medico = medico
        self.paciente = paciente
        self.descricao = descricao
        self.resultado = resultado
    
    def imprimir_exame(self):
        print("Informações do paciente:")
        print("Nome:" , self.paciente.nome)
        print("Cpf:" , self.paciente.cpf)
        print("Idade:" , self.paciente.idade)
        print("")
        print("Informações do médico:")
        print("Nome:" , self.medico.nome)
        print("Crm:" , self.medico.crm)
        print("Especialização:" , self.medico.especializacao)


paciente = paciente('Marcelo Silva', '033444555-22', 26)

medico = medico('Ana Beatriz', 333431, 'Clínico Geral')

exame01 = Exame(medico, paciente, 'COVID-19', 'Negativo')  

exame01.imprimir_exame()						

# Deve exibir relatório com os dados do exame (inclusive os do médico e do paciente)