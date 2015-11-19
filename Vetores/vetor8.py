# -*- coding: utf-8 -*-
# 7. Leia dois vetores de 10 posições cada. Armazene em um vetor de 20 posições os elementos do vetor 1 depois
#os elementos do vetor 2. No final imprima os três vetores.
#n = int(input("Digite a quantidades de posições do vetor: "))

#vetor1 = [0]*n
#vetor2 = [0]*n
#for i in range(n):
	#vetor1[i] = input("Digite os valores do vetor 1: ")
	#vetor2[i] = input("Digite os valores do vetor 2: ")
#print "Vetor1: ", vetor1
#print "Vetor2: ", vetor2

#print "Vetor Soma:", vetor1 + vetor2

#ou

n = int(input("Digite a quantidades de posições do vetor: "))

vetor1 = [0]*n
vetor2 = [0]*n
vetorSoma = [0]*n*2
for i in range(n):
	vetor1[i] = input("Digite os valores do vetor 1: ")
	vetor2[i] = input("Digite os valores do vetor 2: ")

for i in range((n)):
	vetorSoma[i] = vetor1[i]

for i in range(n):
	vetorSoma[n+i] = vetor2[i]

print "Vetor1: ", vetor1
print "Vetor2: ", vetor2
print "Vetor Soma: ", vetorSoma