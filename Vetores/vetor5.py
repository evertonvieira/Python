# -*- coding: utf-8 -*-
#Fazer um programa para ler os dados para uma matriz 3x3 e somar os elementos PARES da matriz.

n = input("Digite a dimensão da matriz: ")
soma = 0
mat = [0]*n
for i in range(n):
	mat[i] = [0]*n
print mat

for i in range(n):
	for j in range(n):
		mat[i][j] = input("Digite: ")

for i in range(n):
	for j in range(n):
		print "%3d" % mat[i][j],
		if mat[i][j] % 2 == 0:
			soma += mat[i][j]
	print
print "A soma dos elementos pares é: %3d" % soma