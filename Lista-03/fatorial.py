# -*- coding: utf-8 -*-
#Fazer um algoritmo para ler um número inteiro e imprimir o FATORIAL desse número
#Ex: N= 4   Fat = 4*3*2*1 = 24

n = input("Digite um número: ")
fator = 1
while (n > 0):
	fator = (fator * n)
	n = n - 1
print fator

