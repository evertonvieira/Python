binario = raw_input ("binarios: ");
vetor = [0]*len(binario);

for i in range(len(binario)):
	vetor[i] =  int(binario[i]);

atual = vetor[0];
c = 2*atual + vetor[1];

for i in range(1, len(binario)-1):
	c = 2*c + vetor[i+1];
print (c);

#11111110
#1101000101101010101000101010111110