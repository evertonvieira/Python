# -*- coding: utf-8 -*-
#Questão 12
#Faça um algoritmo que responda a área de um círculo dado o raio, fornecido pelo usuário.
#Use o valor 3,14159 como uma aproximação de π. (S  = πr2
# foi usado a função round() para o arredondamento do cálculo
print "Digite o raio em cm!!"
raio = input("Digite o raio da circunferência: ")
area = round(3.14159 * raio**2, 2)
print "A área da circunferência é:", area, "cm²"