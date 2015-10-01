# -*- coding: utf-8 -*-
#Questão 21
#Um funcionário recebe um salário fixo mais 4% de comissão sobre as suas vendas.
#Faça um algoritmo que receba o valor do salário fixo do funcionário, o valor das suas vendas e
#que calcule e mostre o salário final do funcionário.
salario = input("Digite o salário: ")
venda = input("Digite o valor da venda: ")
comissao = 0

while venda > 0:
	comissao += (venda*0.04)
	venda = input("Digite o valor da venda: ")

salarioFinal = salario + comissao

print "O salário final é: R$", salarioFinal
