# -*- coding: utf-8 -*-
#Questão 2
#Faça um programa que escreva os N primeiros termos de uma PA. O primeiro termo e a
#razão da PA devem ser lidos..

QtaTermo = input("Digite a quantidade de termos da PA: ")
a1 = input("Digite o primeiro termo da PA: ")
r = input("Digite a razão da PA: ")
#Formula: an = a1 + (n -1)* r

for i in range(1, (QtaTermo + 1)):
	print a1 + (i - 1) *r ,