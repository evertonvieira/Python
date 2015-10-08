# -*- coding: utf-8 -*-
#Faça um programa que leia duas strings e imprima a interseção entre as strings
#Ex:   cabelo e pelo => e, l, o
string = raw_input("Digite a 1° string: ")
cadeia = raw_input("Digite a 2° string: ")
newString = " "
for i in range(0 , len(string)):
	for j in range(0 , len(cadeia)):
		if (string[i] == cadeia[j]):
			newString += ","
			newString += cadeia[j]
print newString