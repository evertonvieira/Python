# -*- coding: utf-8 -*-
#Questão 11
#Faça um algoritmo que converta um comprimento dado em polegadas para centímetros.
#O programa deve utilizar o diálogo Comprimento em polegadas: e escrever o resultado em um
#linha da tela com a forma xxxpol = yyycm. (1 pol = 2,54 cm)

pol = input("Digite o comprimento em polegadas a ser convertido: ")
cm = float(pol * 2.54)
print pol, "pol =", cm, "cm"