'''
Nessa aula, vamos aprender como criar estruturas condicionais aninhadas, usando os comandos if.. elif.. else em programas Python.
'''

nome = str(input('Qual é o seu nome? '))
if nome == 'João':
    print('Que nome lindo você tem!')
elif nome == 'Pedro' or nome == 'maria' or nome =='Paulo':
    print("Seu nome é bem popular no BRasil.")
elif nome in 'Ana Cláudia Jessica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))