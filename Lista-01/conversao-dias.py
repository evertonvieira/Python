import math
# -*- coding: utf-8 -*-
#Questão 17
#Faça um algoritmo que leia os valores de anos, meses e dias e imprima tudo em dias.
ano = input("Digite o ano: ")
mes = input("Digite o mês: ")
dia = input("Digite o dia: ")
tempo = (ano * 365) + (mes * 30) + dia
print tempo, "dias"