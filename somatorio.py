import math
x = input ("Digite o valor de X: ")
y = input ("Digite o valor de Y: ")
e = 0
for i in range(1, 51):
	e = e + (x + (math.sqrt(y + 2)))/3 + (i**2)-(y**5)
print e

