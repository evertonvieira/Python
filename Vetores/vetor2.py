# -*- coding: utf-8 -*-
vetor = [0]*3
print vetor

for i in range(0, 3):
	vetor[i] = [0]*3

print vetor
for i in range(0, 3):
	for j in range(0, 3):
		vetor[i][j] = input("Digite: ")

for i in range(0,3):
	for j in range(0,3):
		print "%3d" % vetor[i][j],
	print