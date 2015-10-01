import math
# -*- coding: utf-8 -*-
#Questão 14
#Faça um programa que, dados pelo usuário os três coeficientes a, b e c de uma equação do 2º grau,
#escreve os valores das raízes dessa equação.
a = input("Digite o coeficientes A da equação: ")
b = input("Digite o coeficientes B da equação: ")
c = input("Digite o coeficientes C da equação: ")

#Delta = B * B - (4 * A * C)
#Delta < 0, não possue raizes reais
#Delta = 0, possui apenas uam raiz (x1 = x2)

delta = b * b - (4 * a * c)


if delta < 0:
	print "A equação não possue raizes reais."
elif delta == 0:
	x1 = (-1 * b) + math.sqrt(delta) / (2 * a)
	print "A equação não possue a seguinte raiz:", x1
else:
	raiz1 = (-1 * b + math.sqrt(delta)) / (2 * a)
	raiz2 = (-1 * b - math.sqrt(delta)) / (2 * a)
print "As raizes são", raiz1, raiz2
