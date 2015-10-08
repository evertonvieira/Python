# -*- coding: utf-8 -*-
#Faça um programa que leia uma string e crie uma outra string repetindo os caracteres
#Ex:  carro => ccaarrrroo
string = raw_input("Digite uma string: ")
newString = ""
for i in range(0 , len(string)):
	newString += string[i] * 2
print newString

