# -*- coding: utf-8 -*-
#1. Faça um programa para ler as notas de 100 alunos e imprimir quantos alunos
#tiraram nota abaixo da media da turma e quantos tiraram acima ou igual a media.

notas = [0.0]*5
soma = 0
maior = 0
menor = 0
for i in range(0, 5):
	nota = float(input("Digite a nota: "))
	notas[i] = nota
	soma += nota
media = (soma/5)
print "Notas: ", notas
print "Média: ", media

for i in range(0, 5):
	if notas[i] >= media:
		maior += 1
	else:
		menor += 1
print "Alunos acima da média:", maior
print "Alunos abaixo da média:", menor