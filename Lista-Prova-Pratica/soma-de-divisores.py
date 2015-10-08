# -*- coding: utf-8 -*-
#que gere  números de 1000 a N (sendo N maior que 1000) e imprima a soma daqueles que divididos por 11
#dão resto igual a 5 MENOS a soma dos múltiplos de 17.
M11 = 0
M17 = 0
for i in range(1000, 2000):
	if i % 11 == 5:
		M11 += i
	elif i % 17 == 0:
		M17 += i
print "A soma dos números são:", M11 + M17