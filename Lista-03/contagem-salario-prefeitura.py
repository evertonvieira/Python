# -*- coding: utf-8 -*-
#Questão 1
#A prefeitura de uma cidade resolveu fazer uma pesquisa entre os seus trabalhadores.
#Para isso ela coletou alguns dados como idade, sexo (M ou F) e salário. Faça um programa que
#leia estes dados e que escreva ao final:
#a média salarial dos homens,   a média salarial das mulheres
#o maior salário encontrado entre as pessoas abaixo de 30 anos.
#Obs: O final da leitura de dados é marcado por uma idade negativa.

idade = input("Digite a idade: ")
TotMan = 0
TotFem = 0
TotSalaMan = 0
TotSalaFem = 0

while idade > 0:
	salario = input("Digite o salário: ")
	sexo = raw_input("Digite o sexo (M ou F): ")
	if sexo == "F":
		TotFem += 1
		TotSalaFem += salario
	else:
		TotMan += 1
		TotSalaMan += salario

	if idade < 30:
		BigSalario = salario
	else:
		BigSalario = "NÃO EXISTE"

	idade = input("Digite a idade: ")

	if TotMan == 0:
		MediaMan = "NÃO EXISTE HOMENS NESTA EMPRESA"
	else:
		MediaMan = TotSalaMan/ TotMan

	if TotFem == 0:
		MediaFem = "NÃO EXISTE MULHER NESTA EMPRESA"
	else:
		MediaFem = TotSalaFem/ TotFem

print "Média salarial dos homens é:", MediaMan
print "Média salarial das mulheres é:", MediaFem
print "O maior salário entre as pessoas a baixo de 30 anos é:", BigSalario
