# -*- coding: utf-8 -*-
#Faça um programa que leia uma string e um caractere e diga quantas vezes o caractere aparece na string
string = raw_input("Digite uma string: ")
caracter = raw_input("Digite uma caracter a ser pesquisado: ")

new_string = string.lower()
new_caracter = caracter.lower()
print "Exite", new_string.count(new_caracter), "caracteres na string", string