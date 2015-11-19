# -*- coding: utf-8 -*-
#3. Leia um vetor de 16 posições e troque as 8 primeiras posições pelas 8 últimas posições.
#Imprima o vetor original e o vetor trocado
n = input("Digite a quantidade de posições do vetor: ")
vetor = [0]*n
for i in range(0, n):
	vetor[i] = i
print "Vetor Original: ", vetor

for i in range((n/2)):
	aux	= vetor[i]
	vetor[i] = vetor[i+(n/2)]
	vetor[i+(n/2)] = aux
print "Vetor Trocado: ", vetor