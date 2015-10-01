# -*- coding: utf-8 -*-
#Questão 22
#João recebeu seu salário e precisa pagar duas contas atrasadas. Como as contas estão atrasadas,
#João deverá pagar uma multa de 2% sobre cada uma. Faça um algoritmo que leia o valor do salário de
#João e das contas que ele deve pagar, e que mostre quanto restará do seu salário após o pagamento das contas.
salario = input("Digite o seu salário: ")
conta = input("Digite o valor da conta a ser paga: ")
divida = 0
while conta > 0:
	divida  += conta + (conta*0.02)
	conta = input("Digite o valor da conta a ser paga: ")

salarioFinal = float(salario - divida)

print "Após o pagamento das dívidas, seu salário será: R$", salarioFinal
