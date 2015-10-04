# -*- coding: utf-8 -*-
#Fazer um algoritmo para imprimir os N primeiros termos da série de Fibonacci. Se N for menor ou igual a zero imprimir uma mensagem de erro.
#Série de Fibonacci: 0 – 1 – 1 – 2 – 3 – 5 – 8 – 13 …
#Os elementos da série de fibonnacci iniciam com 0 e 1 e depois são formados
#pela soma dos dois elementos anteriores

n = input ("Digite um número: ")
if n <= 0:
	print "Erro"
elif n == 1:
	print "0"
elif n == 2:
	print "0 – 1"
else:
	a = 0
	b = 1
	while a < n:
		print "–", a,
		c = a + b
		a = b
		b = c