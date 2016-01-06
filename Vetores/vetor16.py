# -*- coding: utf-8 -*-
def CriaMat(l, c):
	mat = [0] * l
	for i in range(l):
		mat[i] = [0]*c
	for i in range(l):
		for j in range(c):
			mat[i][j] = int(input("Digite um valor: "))
	return mat

#mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
def MontaMat(mat, l, c):
	for i in range(0, l):
		for j in range(0, c):
			print "%3d" % mat[i][j],
	return mat

mat = MontaMat(CriaMat(2,2), 2, 2)

print mat