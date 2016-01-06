# -*- coding: utf-8 -*-
#15. Leia uma matriz 5x5 e imprima o valor do mair elemento. Imprima também a linha e
#coluna desse elemento.

def CriaMat(n):
	#criando matriz quadrada
	mat = [0]*n
	for i in range(n):
		mat[i] = [0]*n

	#preenchendo a matriz
	for i in range(n):
		for j in range(n):
			mat[i][j] = input("Digite: ")
	return mat

mat = CriaMat(5)
maior = -1
linha = -1
coluna = -1
for i in range(5):
	for j in range(5):
		if mat[i][j] > maior:
			maior = mat[i][j]
			linha = i
			coluna = j
		print "%3d" % mat[i][j],
	print

print "o maior número é: ", maior, "está localizado na linha", linha, "coluna", coluna