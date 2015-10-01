# -*- coding: utf-8 -*-
#Questão 7
#Elabore um algoritmo que implemente uma calculadora com as operações de soma, subtração,
#multiplicação e divisão. O algoritmo deve ler os operadores e a operação a ser realizada e
#mostrar o resultado. Seu algoritmo deve considerar o caso em que o usuário tente dividir um
#número por zero.
operacao = raw_input("Digite a operão desejada: ")
n1 = input("Digite o 1° número: ")
n2 = input("Digite o 2° número: ")

if operacao == "+":
	result = n1 + n2
elif operacao == "-":
	result = n1 - n2
elif operacao == "/":
	if n2 == 0:
		result = "OPERAÇÃO INVÁLIDA"
	else:
		result = n1 / float(n2)
elif operacao == "*":
	result = n1 * n2
print "O resultado da operação é:", result