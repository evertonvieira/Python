# -*- coding: utf-8 -*-
# 7. Leia dois vetores de 10 posições cada. Armazene em um vetor de 20 posições os elementos do vetor 1 depois
#os elementos do vetor 2. No final imprima os três vetores.
vet1 = [0]*10
vet2 = [0]*10
vetSoma = [0]*20
for i in range(10):
	vet1[i] = i*2+2
	vet2[i] = i*2+3

for i in range(10):
	vetSoma[i] = vet1[i]
	vetSoma[i+10] = vet2[i]

print "Vetor1:", vet1
print "Vetor2:", vet2
print "Vetor Soma:", vetSoma