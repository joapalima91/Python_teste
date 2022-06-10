nome = str(input('Digite seu nome completo: '))

print("Seu nome é: {}".format(nome))

print('-'*50)

print("Seu nome com todas letras maiúsculas é: {}".format(nome.upper()))
print("Seu nome em letras minusculas é {}".format(nome.lower()))
print('A qunatidade de letras no seu nome é: {}' .format(len(nome)- nome.count(" ")))
print("seu primeiro nome tem {} letras".format(nome.find(" ")))

print('\n','-'*50)
nome2 = nome.split()
print(nome2)
print('Seu primeiro nome tem {} letras'.format(len(nome2[0])))