# -*- coding: utf-8 -*-
# Calcule o MDC entre dois números lidos.
x = input("Número 1:")
y = input("Número 2:")
mdc = 1
if x > y:
	maior = x
else:
	maior = y
for i in range(1, maior):
	if  x % i == 0 and y % i == 0:
		mdc = i
print "O MDC é: ", mdc


