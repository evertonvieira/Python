# -*- coding: utf-8 -*-
# Leia um vetor de 40 posições contar quantos elementos pares se encontram no vetor.
n = input("Digite quantas posições possui o vetor: ")
soma = 0
vetor = [0]*n
for i in range(n):
	vetor[i] = input("Digite um número: ")

for i in range(n):
	if vetor[i] % 2 == 0:
		soma += 1
print "Vetor: ", vetor
print "Existe %2d números pares no vetor" % soma