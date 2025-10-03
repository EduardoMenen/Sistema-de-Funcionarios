# Mini Projeto 1 - Sistema de Funcionários

## Descrição
Este projeto é um exemplo prático de Programação Orientada a Objetos em Python. 
Ele utiliza **classes abstratas**, **herança** e **polimorfismo** para representar diferentes tipos de funcionários: Gerente, Estagiário e Vendedor.

## Estrutura do Código
- **Classe abstrata `Funcionario`**: define os atributos universais (`nome`, `idade`, `salario`) e o método abstrato `trabalhar()`.
- **Classe `Gerente`**: herda `Funcionario`, adiciona `departamento` e `equipe`, sobrescrevendo `trabalhar()`.
- **Classe `Estagiario`**: herda `Funcionario`, adiciona `ano_de_estagio` e `universidade`, sobrescrevendo `trabalhar()`.
- **Classe `Vendedor`**: herda `Funcionario`, adiciona `n_vendas` e `percentual_comissao`, sobrescrevendo `trabalhar()` e implementando método `comissao()`.

## Funcionamento
O projeto cria instâncias de cada tipo de funcionário e armazena em uma lista. 
Um loop percorre a lista e chama o método `trabalhar()` de cada funcionário:

# Tecnologias

- *Python 3.x*

# Conceitos de POO: 
- abstração 
- herança 
- polimorfismo
- encapsulamento

# Como rodar

- Clone o repositório

- Execute o script Python:

python nome_do_arquivo.py
