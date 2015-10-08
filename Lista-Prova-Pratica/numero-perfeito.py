# -*- coding: utf-8 -*-
# 7. Imprima os números perfeitos entre 0 e 1000. Um número é dito perfeito quando a soma dos seus divisores (tirando ele próprio) é igual a ele.
#Exemplo: 6 é perfeito pois, 1 + 2 + 3 = 6
soma = 0
somaPerfe = 0
n = input ("número: ")
for i in range(0, 1001):
	if i % 2 == 0:
		soma += i
		print soma
		if (soma == n):
			somaPerfe += soma

print "soma:", somaPerfe

