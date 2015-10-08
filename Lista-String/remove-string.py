# -*- coding: utf-8 -*-
#Faça um programa que leia uma string e um caractere e crie uma outra string sem o caractere lido.
string = raw_input("Digite uma string: ")
caracter = raw_input("Digite uma caracter a ser removida: ")

new_string = string.lower()
new_caracter = caracter.lower()

print "String antiga:", string
print "A nova string é: ", new_string.replace(new_caracter, "")