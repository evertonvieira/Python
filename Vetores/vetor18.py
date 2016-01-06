# -*- coding: utf-8 -*-
#14. Leia uma string e imprima se ela é um palindromo. Um palindromo é uma cadeia que pode ser
#lida de frente para trás e de trás para frente.  Ex: ‘SOMOS’    ‘1234321’

string = raw_input("Digite uma string: ")
new = ""
for i in range(len(string)):
	new += string[len(string)-i -1]

if string == new:
	print "A palavra", string, "é palidrome!"
else:
	print "A palavra", string, "não é palidrome!"

soma = 0
for i in range(64):
	soma += i
print soma


soma = 0
for i in range(5, 11):
 soma += 2**i
print soma