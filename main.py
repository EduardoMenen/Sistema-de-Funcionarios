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
    def __init__(self, nome, idade, salario, Tempo_Estagio, Universidade):
        super().__init__(nome, idade, salario)
        self.tempo_estagio = Tempo_Estagio
        self.universidade = Universidade
    
    def trabalhar(self):
        return 'O Estagiário está está aprendendo e auxiliando'

class Vendedor(Funcionario):
    def __init__(self, nome, idade, salario, n_vendas, bonus):
        super().__init__(nome, idade, salario)
        self.n_vendas = n_vendas
        self.bonus = bonus
    
    def trabalhar(self):
        return 'O Vendedor está vendendo produtos'