# Escreva um programa que leia uma determinada quantidade de minutos e
# informe essa quantidade convertida de para horas e minutos. Por exemplo
# , 220 minutos é equivalente 3 horas e 40 minutos.

min = int(input())

h = (min//60)
m = min%60

print (f'{h:.0f}:{m:.0f}')


