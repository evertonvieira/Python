import math
# -*- coding: utf-8 -*-
#Questão 16
#Faça um algoritmo que leia os valores de horas, minutos e segundos e transforme tudo para segundo.
#EX: 3 horas 2 minutos 7 segundos	= 10927 segundos
hora = input("Digite a hora: ")
minuto = input("Digite os minutos: ")
segundo = input("Digite os segundos: ")
tempo = (hora * 3600) + (minuto * 60) + segundo
print tempo, "segundos"