# -*- coding: utf-8 -*-
#Questão 13
#Faça um programa que, dados pelo usuário dois números inteiros m e n, com m > n,
#escreve os valores de uma tripla Pitagórica (lado1, lado2 e hipotenusa) gerada a partir de m e n,
#através das 3 fórmulas:
#Lado1 = m2 – n2                 Lado2 = 2mn                      Hipotenusa = m2 + n2
m = input("Digite um número inteiro: ")
n = input("Digite outro número inteiro: ")

if m <= n :
	while m <= n:
		print "Digite um valor menor que ", m
		n = input("Digite um número inteiro: ")

lado1 = (m**2) - (n**2)
lado2 = 2*m*n
hipo = (m**2) + (n**2)

print "os lados são", lado1, lado2, "e", hipo