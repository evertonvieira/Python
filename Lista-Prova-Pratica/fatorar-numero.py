# -*- coding: utf-8 -*-
# Leia um número N, caso ele seja > 0,  mostre a seguinte saída, caso contrário de uma mensagem de erro:
#Exemplo N= 9
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5
#1 2 3 4 5 6
#1 2 3 4 5 6 7
#1 2 3 4 5 6 7 8
#1 2 3 4 5 6 7 8 9

n = input("Digite um número: ")

for i in range(1,n+1):
	for j in range(1,i+1):
		print j,
	print '\t'
