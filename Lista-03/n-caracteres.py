# -*- coding: utf-8 -*-
#1. leia um nome e imprima-o tantas vezes quantas for a quantidade de caracteres do seu nome.

alunos = input("Quantidades de alunos: ")

aprovados = 0
provaFinal = 0
reprovado = 0
mediaTurma = 0
totAlunos = 0

while alunos > 0:
	p1 = input("Digite 1 nota: ")
	p2 = input("Digite 2 nota: ")
	alunos -= 1
	media = (p1 + p2) / float(2)
	totAlunos += 1
 	mediaTurma += media

	if media >= 7:
		print "Aluno aprovado com média ", media
		aprovados += 1
	elif media >= 4:
		print "Prova final"
		provaFinal += 1
	else:
		reprovado += 1

print "Alunos aprovados:", aprovados
print "Alunos em prova final:", provaFinal
print "Alunos reprovado:", reprovado
print "A média da turma é:", mediaTurma/ float(totAlunos)






