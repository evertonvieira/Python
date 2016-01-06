# -*- coding: utf-8 -*-
#Busca binárica
def criaVet(n):
	vet = [0] * n
	for i in range(n):
		vet[i] = input("Digite um valor: ")
	return vet

def ordenacao(vet):
	aux = 0
	for i in range(0, len(vet)):
		for j in range(0, len(vet)):
			if vet[i] < vet[j]:
				aux = vet[i]
				vet[i] = vet[j]
				vet[j] = aux

def busca (vet, s):
	inicio = 0
	final = len(vet)
	meio = 0
	achou = False
	posicao = -1
	while inicio <= final and not achou:
		meio = (inicio + final) // 2
		if vet[meio] == s:
			achou = True
			posicao = meio
		elif vet[meio] > s:
			final = meio - 1
		else:
			inicio = meio + 1
	return posicao


vet = criaVet(5)
print vet
ordenacao(vet)
print vet
s = input("digite o valor a ser pesquisado: ")
posicao = busca(vet, s)

if posicao != -1:
	print  "O Valor foi encontrado na posição:", posicao
else:
	print  "O Valor não foi encontrado"










