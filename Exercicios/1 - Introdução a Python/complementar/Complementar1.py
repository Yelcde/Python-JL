# 1. A Companhia de Carros Usados João Honesto paga seus empregados um salário de R$ 1.000,00 por mês mais uma comissão de R$ 200,00 por cada carro vendido mais 5% do valor da venda.                             Escreva um programa que leia o nome, o número de carros vendidos e o valor total das vendas de um vendedor, e calcule e exiba o seu salário.

# nome = input('Qual seria o nome do funcionário? ')

# carro_vendido = int(input(f'Quantos carros {nome} vendeu? '))

# valor_venda = float(input('Qual o valor da venda de todos os carros vendido? '))

# salario_mensal = 1000 #Salário mensal do funcionário

# comissao_por_carro = 200 #Comissão por venda de carro

# porcentagem_valor_venda = 0.05*carro_vendido #5% do valor da venda total

# salario_total = salario_mensal + (carro_vendido*comissao_por_carro) *porcentagem_valor_venda

# print(f'o salário total de {nome} é de {salario_total:.2f} ')



# Exercicio Corrigido 

nome = input('Qual seria o nome do funcionário? ')

carro_vendido = int(input(f'Quantos carros {nome} vendeu? '))

valor_venda = float(input('Qual o valor da venda de todos os carros vendido? '))

salario_mensal = 1000 #Salário mensal do funcionário

comissao_por_carro = 200 #Comissão por venda de carro

porcentagem_valor_venda = valor_venda * 0.05  #5% do valor da venda total

''' O Erro estava nessa linha de código!! Colocando os valores carro_vendido = 1 e valor_venda = 1000 o resultado final deveria dar 1250 pois o valor da comissão fixa, nesse caso, seria 200 e 5 por cento de 1000 é 50, tudo isso somado ao salario que é 1000 daria 1250. 
    O seu código segue tudo certo, ele calcula de forma certa o valor comissão por carro e a porcentagem no total da venda, mas erra na hora de somar tudo isso para dar o valor total do quanto o funcionário vai receber.
    No nódigo que você escreveu salario_total = salario_mensal + (carro_vendido*comissao_por_carro) *porcentagem_valor_venda em vez de somar a porcentagem, voce multiplica, o que muda completamente o resultado da questão!!
'''
salario_total = salario_mensal + (carro_vendido*comissao_por_carro) + porcentagem_valor_venda

print(f'o salário total de {nome} é de {salario_total:.2f} ')