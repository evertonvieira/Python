# -*- coding: utf-8 -*-
#9.leia  uma frase e exiba quantas vogais aparecem na frase. Além disso, imprima a palavra "OK" se o primeiro,
#último e caractere do meio forem vogais, e a palavra "PROBLEMA", caso contrário.

string = raw_input ("Digite uma palabra: ")
soma = 0
new = string.lower();
print new

for i in range(0, len(new)):
	if new[i] == 'a' or new[i] == 'e' or new[i] == 'i' or new[i] == 'o' or new[i] == 'u':
		soma += 1
		if string[-1]:


print soma

