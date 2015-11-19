# -*- coding: utf-8 -*-
#9. Leia uma frase e imprima as suas palavras.
f = raw_input("Digite uma frase: ")
vet = f.split()
print vet
for i in range(len(vet)):
	print vet[i]
