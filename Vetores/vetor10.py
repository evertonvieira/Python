# -*- coding: utf-8 -*-
#Leia dois vetores de 15 posições cada, imprimir a soma dos elementos dos vetores e a
#diferença dos elementos dos vetores.
vet1 = [0]*15
vet2 = [0]*15
soma1 = 0
soma2 = 0
for i in range(15):
	vet1[i] = i*3+2
	vet2[i] = i*4+4

for i in range(15):
	soma1 += vet1[i]
	soma2 += vet2[i]
print vet1
print vet2

print "A soma dos elementos dos vetores é: ", soma1 + soma2
print "A diferença dos elementos dos vetores é: ", soma1 - soma2