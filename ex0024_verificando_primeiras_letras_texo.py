#rie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input("Qual sua cidade de nascimento: ")).strip()  #strip elimina os aspaços

print(cidade[:5].upper() == 'SANTO')
#joaga nome da cidade para maiúscula pra fazer comparação com "SANTO"

