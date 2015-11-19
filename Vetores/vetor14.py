# -*- coding: utf-8 -*-
#12.Fazer um programa para ler dois vetores de 10 posições e colocar em um outro vetor de no máximo
#20 posições a união dos elementos. Colocar em um vetor de 10 posições a intercecção dos dois vetores.

def CriaVetor(name, tamanho):
	name = [0]*tamanho
	for i in range(tamanho):
		name[i] = input("Digite valores para o vetor: ")
	print name

Union = [0]*10

def Union(vet1, vet2):
	k = 0
	maior = vet1
	menor = vet2
	if maior < vet2:
		maior = vet2
		menor = vet1
	for i in range(maior):
		for j in range(menor):
			if maior[i] == menor[j]:
				Union[k] = maior[i]
				k += 1
	print Union

CriaVetor('vet1', 10)
CriaVetor('vet2', 10)

Union('vet1', 'vet2')