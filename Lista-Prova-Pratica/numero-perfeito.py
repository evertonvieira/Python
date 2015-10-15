# -*- coding: utf-8 -*-
#Imprima os números perfeitos entre 0 e 1000. Um número é dito perfeito quando a
#soma dos seus divisores (tirando ele próprio) é igual a ele.
#Exemplo: 6 é perfeito pois, 1 + 2 + 3 = 6

#n = 1000
soma = 0
for i in range(1, 1000):
	n = i
	soma = 0
	for j in range(1, n):
		if n % j == 0:
			soma += j
	if soma == n:
		print n,
