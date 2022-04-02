# Escreva um programa que leia um preço e um valor
# percentual. Informe o preço acrescido do percentual e o
# preço com o desconto percentual. Por exemplo, se for lido
# um preço de 100.00 e um valor percentual de 5.00 o
# programa deve mostrar que o preço com aumento é 105.00
# e o preço com desconto é 95.00.
# OBS: Mostre sempre duas casas decimais.

pre = float(input())
por = float(input())
aum = (pre+(pre*por/100))
des = (pre-(pre*por/100))

print(f'{aum:.2f}\n{des:.2f}')
            