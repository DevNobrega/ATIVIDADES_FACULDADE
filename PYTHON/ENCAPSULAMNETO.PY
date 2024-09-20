
class Empregado:
    def __init__(self, nome:str, salario_base:float):
        self.nome = nome
        self.salario_base = salario_base

    def valores(self):
        ...

class Gerente(Empregado):
    def valores(self):
        return f'{self.nome} recebe: {self.salario_base + (self.salario_base*0.10)}'
    
class Vendedor(Empregado):
    def valores(self):
        return f'{self.nome} recebe: {self.salario_base + (self.salario_base*0.02)}'

barto = Gerente('Bartolomeu Nagano', 300)
print(barto.valores())
cj = Vendedor('Christopher Jonny', 1500)
print(cj.valores())