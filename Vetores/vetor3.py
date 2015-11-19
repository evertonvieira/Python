# -*- coding: utf-8 -*-
#2. Ler um vetor de 12 posições inteiras e depois ler dois números X e Y de 1 a 12.
#Imprimir  soma das posições X e Y do vetor.

n = input("Digite a quantidade de posições do vetor: ")
vetor = [0]*n
soma = 0
x = input("Digite um número de %2d: " % n)
y = input("Digite outro número de %2d: " % n)
for i in range(0, len(vetor)):
	vetor[i] = i
soma = vetor[x] + vetor[y]
print "A soma dos números das posições ",x, "+", y, "=", soma