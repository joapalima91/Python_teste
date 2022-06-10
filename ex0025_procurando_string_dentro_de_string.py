#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input("Digite seu nome completo: ")).strip()

print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
#joaga nome para minusculo pra fazer comparação com "silva" e depois procura se tem dentro do nome
