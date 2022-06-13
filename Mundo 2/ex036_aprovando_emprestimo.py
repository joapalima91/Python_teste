'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''

casa = float(input('Qual valor da casa R$'))
salario = float(input('Qual seu salário R$'))
anos = int(input('Quer pagar a casa em quantos anos? '))

prestação = casa / (anos * 12)
minino = salario * 30/100

print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(casa, anos, prestação))
if prestação <= minino:
    print("Empréstimo pode ser concedido!")
else:
    print("Empréstimo NEGADO")