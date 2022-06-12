# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('Digite primeiro segmento: '))
r2 = float(input('Digite segundo segmento: '))
r3 = float(input('Digite terceiro segmento: '))

# anadlisar se dar pra formar um triangulo
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("os segmento PODEM FORMAR UMA TRIÂNGULO!")
else:
    print("Os segmenteo NÃO PODEM FORMAR UM TRIÂNGULO!!")
