# -*- coding: utf-8 -*-
#Faça um programa que leia uma string e crie uma outra string invertendo as posições de dois em dois
#Ex:  mexico => emixoc
string1 = raw_input("Digite uma string: ")
string2 = raw_input("Digite uma string: ")

string1  = string1[::-1]
print string1
print string2
maior = len(string1)
saida = ""
if len(string2) > maior:
	maior = len(string2)
for i in range(maior):

	if i < len(string1):
		saida += string1[i]

	if i < len(string2):
		saida += string2[i]

print saida