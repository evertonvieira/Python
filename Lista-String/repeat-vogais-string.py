# -*- coding: utf-8 -*-
#Faça um programa que leia uma string e crie uma outra string repetindo apenas as vogais
#Ex:  carro => caarroo
string = raw_input("Digite uma string: ")
newString = ""
for i in range(0 , len(string)):
	if string[i] == "a" or string[i] == "e" or string[i] == "i" or string[i] == "o" or string[i] == "u":
		newString += string[i]*2
	else:
		newString += string[i]
print newString