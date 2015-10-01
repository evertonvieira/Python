# -*- coding: utf-8 -*-
#Questão 24
#Faça um algoritmo que leia o salário de um funcionário e o salário mínimo vigente.
#Calcular e escrever quantos salários mínimos ganha o funcionário.
salario = input("Digite seu salário: ")
salarioMinimo = input("Digite o salaŕio mínimo vigente: ")
qta = round((salario/salarioMinimo), 0)

if qta > 1:
	print "Você recebe", int(qta) , "salários mínimos."
else:
	print "Você recebe 1 salário mínimo."
