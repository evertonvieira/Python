# -*- coding: utf-8 -*-

#método para criar um vetor
def create(n):
	vet = [0]*n
	for i in range(n):
		vet[i] = int(input("Digite o valor para a posição %i: " % i))
	return vet

#método para order o vetor em ordem crescente
def order(vet):
	aux = 0
	for i in range(len(vet)):
		for j in range(len(vet)):
			if vet[i] < vet[j]:
				aux = vet[i]
				vet[i] = vet[j]
				vet[j] = aux
	return vet

def search(vet):
	s = input ("Digite o número a ser pesquisado no vetor: ")
	inicio = 0
	fim = len(vet)
	achou = False
	posicao = -1
	while inicio <= fim and not achou:
		meio = (inicio + fim)//2
		if vet[meio] == s:
			achou = True
			posicao = meio
		elif vet[meio] > s:
			fim = meio - 1
		else:
			inicio = meio + 1
	return posicao

vet = create(5)
print vet

vetOrdenado = order(vet)
print vetOrdenado

s = search(vetOrdenado)

if s != -1:
	print "O número pesquisado foi encontrado na posição: ", s
else:
	print "A pesquisa retornou vazia!"



