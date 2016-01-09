# -*- coding: utf-8 -*-
#17. Crie uma matriz 5x5 com 1 na diagonal principal e 0 nas outras posições. Imprima a matriz.

#método para criar a matriz
def create(l, c):
	mat = [0]*l
	for i in range(l):
		mat[i] = [0]*c

	for i in range(l):
		mat[i][l-1-i] = 1
		mat[i][i] = 1
	return mat
mat = create(5,5)


for i in range(5):
	for j in range(5):
		print "%3d" % mat[i][j],
	print