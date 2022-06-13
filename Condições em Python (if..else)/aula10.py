
tempo = int(input('Quantos anos seu carro tem? '))
if tempo <=3:
    print('Carro novo!')
else:
    print("Carro velho")

nome = str(input('Qual é o seu nome? '))
if nome == 'João':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A sua média foi {:.1f}'.format(m))

print('Parabéns' if m >=6 else 'ESTUDE MAIS!') # if simplificado
if m >= 6.0:
    print('Sua média foi boa. Parabéns!!')
else:
    print('Sua média foi ruim. Estude mais!')
