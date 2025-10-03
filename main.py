from abc import ABC, abstractmethod
class Funcionario(ABC):
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario

    @abstractmethod
    def trabalhar(self):
        pass

class Gerente(Funcionario):
    def __init__(self, nome, idade, salario, departamento, equipe):
        super().__init__(nome,idade,salario)
        self.departamento = departamento
        self.equipe = equipe
    
    def trabalhar(self):
        return 'O Gerente está coordenando sua equipe'

class Estagiario(Funcionario):
    def __init__(self, nome, idade, salario, ano_de_estagio, universidade):
        super().__init__(nome, idade, salario)
        self.ano_de_estagio = ano_de_estagio
        self.universidade = universidade
    
    def trabalhar(self):
        return 'O Estagiário está aprendendo e auxiliando'

class Vendedor(Funcionario):
    def __init__(self, nome, idade, salario, n_vendas):
        super().__init__(nome, idade, salario)
        self.n_vendas = n_vendas
        self.percentual_comissao = 0.10
    
    def trabalhar(self):
        return 'O Vendedor está vendendo produtos'

    def comissao(self):
        return self.n_vendas * (self.salario * self.percentual_comissao)

gerente = Gerente("Eduardo Menegazzo", 20, 8000, 'Vendas', ["Ana", "João", "Bernardo"])
estagiario = Estagiario("Lucas Pereira", 18, 1200, 2, "Atitus")
vendedor = Vendedor("Gabriel Silva", 34, 3000, 10)

print(gerente.trabalhar())
print(estagiario.trabalhar())
print(vendedor.trabalhar())