# -*- coding: utf-8 -*-
#Ler um vetor de números inteiros de 30 posições. Depois, ler um número inteiro X, imprimir quantas vezes o
#número X aparece no vetor.
n = input("Digite quantas posições possui o vetor: ")
soma = 0
vetor = [0]*n
for i in range(n):
	vetor[i] = input("Digite um número: ")

numero = input("Digite o número a ser pesquisado no vetor: ")

for i in range(n):
	if vetor[i] == numero:
		soma += 1
print vetor
print "Existe %2d vezes o número %2d no vetor." % (soma, numero)