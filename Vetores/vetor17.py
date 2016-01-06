# -*- coding: utf-8 -*-
#12. Fazer um programa para ler dois vetores de 10 posições e colocar em um outro
#vetor de no máximo 20 posições a união dos elementos. Colocar em um vetor de 10 posições
#a intercecção dos dois vetores.
def CriarVet(n):
	vet = [0]*n
	for i in range(n):
		vet[i] = int(input("Digite um valor inteiro: "))
	return vet

def Union(v1, v2):
	vet = [0]*10
	for i in range(5):
		vet[i] = v1[i]
		vet[i+5] = v2[i]
	return vet

def Inter(v1, v2):
	vet = [0]*5
	k = 0
	for i in range(5):
		for j in range(5):
			if v1[i] == v2[j]:
				vet[k] = v1[i]
				k += 1
	return vet

vetor1 = CriarVet(5)
vetor2 = CriarVet(5)
vetUniao = Union(vetor1, vetor2)
interceccao = Inter(vetor1, vetor2)

print vetor1
print vetor2
print "União: ", vetUniao
print "Intersecção: ", interceccao