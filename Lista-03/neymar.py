# -*- coding: utf-8 -*-
#Fazer um algoritmo para ler o nome a idade e o salário de vários funcionários até que seja digitado o
#nome NEYMAR , que faz parte da lista. Imprimir o nome da pessoa com a MENOR idade e salário maior que 1000,00.

soma = 0
for i in range(1,6):
	fat = 1
	for j in range(1, i+1):
		fat = fat*j
	print 'fat de', j, "é", fat
	soma += fat
print 'soma:', soma



