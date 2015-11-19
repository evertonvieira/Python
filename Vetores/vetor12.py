# -*- coding: utf-8 -*-
#10. Leia uma frase e imprima o total de vogais, o total de brancos e o total do resto.
s = raw_input("Digite uma frase: ")
vogais = "aeiouAEIOUÁÉÍÓÚÂãÃÊêôÔõÕú"
totV = 0
totB = 0
totR = 0
for i in range(len(s)):
	if s[i] in vogais:
		totV += 1
	elif s[i] == " ":
		totB += 1
	else:
		totR += 1
print "Total de Vogais:", totV
print "Total de Brancos:", totB
print "Restante das letras", totR