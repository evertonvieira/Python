# -*- coding: utf-8 -*-
string = raw_input("Digite uma string: ")
nova = ""
j = len(string)
for i in range(0, len(string)):
	nova += string[j - i]
print nova
