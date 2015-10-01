# -*- coding: utf-8 -*-
#Questão 6
#Elabore um algoritmo que leia 3 números do usuário e imprima-os em ordem crescente.
a = input("Digite o 1° número: ")
b = input("Digite o 2° número: ")
c = input("Digite o 3° número: ")

# a > b e  b > c logo a > c --> a, b, c
if (a > b) and (a > c):
	if c > b:
		print "A ordem é:", a, ",", c, "e", b
	else:
		print "A ordem é:", a, ",", b, "e", c
elif (b > a) and (b > c):
	if c > a:
		print "A ordem é:", b, ",", c, "e", a
	else:
		print "A ordem é:", b, ",", a, "e", c
elif (c > b) and (c > a):
	if b > a:
		print "A ordem é:", c, ",", b, "e", a
	else:
		print "A ordem é:", c, ",", a, "e", b
