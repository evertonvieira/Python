# -*- coding: utf-8 -*-
#Questão 23
#Faça um algoritmo que leia três notas de um aluno com os seus respectivos pesos e que calcule e
#escreva a média ponderada dessas notas.
n1 = input("Digite a 1° nota: ")
p1 = input("Digite o peso da 1° nota: ")
n2 = input("Digite a 2° nota: ")
p2 = input("Digite o peso da 2° nota: ")
n3 = input("Digite a 3° nota: ")
p3 = input("Digite o peso da 3° nota: ")
soma = (n1*p1) + (n2*p2) + (n3*p3)
ponderada = float(p1+p2+p3)
media = ((n1*p1) + (n2*p2) + (n3*p3)) / float(p1+p2+p3)
print "A média final do aluno é:", round(media, 2)
