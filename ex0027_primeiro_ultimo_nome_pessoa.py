#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: ')).strip()

seprado = nome.split()
print(seprado)
print('_'*40)
print("Muito prazer em te conhecer!!")
print("Seu primeiro nome é {}".format(seprado[0]))
print("Seu último nome é {}".format(seprado[len(seprado)-1]))