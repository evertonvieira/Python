# -*- coding: utf-8 -*-
#Questão 5
#Faça um algoritmo que receba três notas de um aluno, calcule e mostre a média aritmética e a
#mensagem que segue a tabela abaixo. Para alunos de exame, calcule e mostre a nota que deverá
#ser tirada no exame para a aprovação, considerando que a média no exame é 6,0.  Nota no exame = (12 – media).
p1 = input("Digite a 1° nota do aluno: ")
p2 = input("Digite a 2° nota do aluno: ")
p3 = input("Digite a 3° nota do aluno: ")

mediaArit = (p1 + p2 + p3)/float(3)

print "A média do aluno é:", round(mediaArit, 2), "-",

if mediaArit < 2.9:
	print "REPROVADO"
elif mediaArit < 6.9:
	print "EXAME"
	print "Você deve tirar", round((6.9 - mediaArit), 2), "para ser aprovado"
else:
	print "APROVADO"


