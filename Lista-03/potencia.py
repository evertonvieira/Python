# -*- coding: utf-8 -*-
#Questão 2
#Faça um programa que escreva os N primeiros termos de uma PA. O primeiro termo e a
#razão da PA devem ser lidos..

x = input("Digite o valro de x: ")
y = input("Digite o valro de y: ")

mult = 0
for i in range(1, y):
	mult += x*x

print mult