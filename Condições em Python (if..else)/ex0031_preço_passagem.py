#Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

dist = int(input("Digite a distância da viagem em KM: "))
# if dist <= 200:
#     print("O preço da sua passagem é RS{:.2f}".format(dist * 0.50))
# else:
#     print("O preço da sua passagem é RS{:.2f}".format(dist * 0.45))
'''if dist<=200:
    preço = dist * 0.50
else:
    preço = dist * 0.45
print("O preço da sua passagem é RS{:.2f}".format(preço))'''
preço = dist *0.50 if dist <= 200 else dist * 0.50
print("O preço da sua passagem é RS{:.2f}".format(preço))
print("Tenha uma boa viagem!!")