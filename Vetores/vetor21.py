# -*- coding: utf-8 -*-
#16. Leia uma matriz 7x7 e imprima a soma dos elementos da linha 6.
#Imprima tambem a soma dos elementos da coluna 2. Imprima também a soma dos elementos
#da diagonal principal. Imprima também o elemento da linha 3 e  coluna 4.
#Imprima também a soma de todos os elementos pares da matriz.

#método para criar a matriz
def create(l, c):
	mat = [0]*l
	for i in range(l):
		mat[i] = [0]*c

	for i in range(l):
		for j in range(c):
			mat[i][j] = int(input("Digite: "))

	return mat
mat = create(7,7)

soma1 = 0
soma2 = 0
soma3 = 0
soma4 = 0
soma5 = 0

print "------------"
for i in range(7):
	for j in range(7):
		print "%3d" % mat[i][j],
	print
print "------------"


for i in range(7):
	for j in range(7):
		if i == 5:
			soma1 += mat[i][j]
		if j == 1:
			soma2 += mat[i][j]
		if i == j:
			soma3 += mat[i][j]
		if i == 2 and j == 3:
			soma4 += mat[i][j]
		if mat[i][j] % 2 == 0:
			soma5 += mat[i][j]

print "A soma dos elementos da linha 6 é: ", soma1
print "A soma dos elementos da coluna 2 é: ", soma2
print "A soma dos elementos da diagonal principal é: ", soma3
print "A soma dos elementos da linha 3 e coluna 4 é: ", soma4
print "A soma dos elementos pares é: ", soma5
