# -*- coding: utf-8 -*-
#21. Leia uma matriz 3x3 e imprima a soma dos elementos da diagonal principal e a
#soma dos elementos da diagonal secundária.

#método para criar a matriz
def create(l, c):
	mat = [0]*l
	for i in range(l):
		mat[i] = [0]*c

	for i in range(l):
		for j in range(c):
			mat[i][j] = input("Digite: ")
	return mat

mat = create(3,3)

soma1 = 0
soma2 = 0

for i in range(3):
	soma1 += mat[i][i]
	soma2 += mat[i][3-1-i]

for i in range(3):
	for j in range(3):
		print "%3d" % mat[i][j],
	print

print "A soma da diagonal principal é: ", soma1
print "A soma da diagonal secundária é: ", soma2