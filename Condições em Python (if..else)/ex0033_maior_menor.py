#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('Digite primeiro valor: '))
b = int(input('Digite segundo valor: '))
c = int(input('Digite terceiro valor: '))
#verificando menor valor
menor = a
if b<a and b<c:
    menor=b
if c<a and c<b:
    menor=c

#verfificando maior
maior =a
if b>a and b>c:
    maior=b
if c>a and c>b:
    maior=c
print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))