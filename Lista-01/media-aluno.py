# -*- coding: utf-8 -*-
#Questão 05
#Elabore um algoritmo que calcule e imprima a média de um aluno em uma disciplina com as
#seguintes características: Duas provas (P1 e P2), um trabalho (T) e 5 listas de exercícios (L1..L5).
#A média será dada por: média = 0,3xP1 + 0,4xP2 + 0,2x(média das listas) + 0,1xT.
p1 = input("Digite a nota da P1: ")
p2 = input("Digite a nota da P2: ")
t = input("Digite a nota do trabalho: ")
l1 = input("Digite a nota da lista 1: ")
l2 = input("Digite a nota da lista 2: ")
l3 = input("Digite a nota da lista 3: ")
l4 = input("Digite a nota da lista 4: ")
l5 = input("Digite a nota da lista 5: ")

media =  (0.3*p1) + (0.4*p2) + 0.2*((l1+l2+l3+l4+l5)/5) + 0.1*t

print "A média do aluno é: ", media

