frase = 'Curso em Vídeo Python'

print(frase)
print("Tamando da frase é: ",len(frase))

print(frase[9]) #pimprime dígito 9 na frase

print(frase[9:21]) #imprime os dígitos de 9 ao 20

print(frase[9:21:2]) #começa no 9, para no 21, pulando de 2 em 2

print(frase[:5]) #comça antes do 2pontos(caracter 0) e termina no 5

print(frase[15:]) # começa no 15 e vai até o final

print(frase[9::3]) #começa no 9 e vai até final, pulando de 3 em 3

len(frase) # conta tamanho da string

print(frase.find('deo')) #imprime localição 'deo', a posição que começa

print(frase.find('Android')) #retorna -1 pra valor não encontrado

print('Curso' in frase) # retorna se existe 'Curso" na frase

print(frase.count('o')) #imprime a quantidade da letra "o" na frase

print("-"*20)

frase2 = frase.split() #separa todas a palavras da frase

print(frase2[0])


