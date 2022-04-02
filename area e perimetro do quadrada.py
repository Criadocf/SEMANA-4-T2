# Escreva um programa que ler o valor do lado de um quadrado. Calcule e
# mostre a área e o perímetro desse quadrado. OBS: Mostre o resultado com 4
# casas decimais alinhado à direta com 10 espaços na tela.


la = float(input())
ar = (la)**2
pe = 4 * la

print(f'{ar:>10.4f}\n{pe:>10.4f}')
