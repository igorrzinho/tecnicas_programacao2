# -*- coding: utf-8 -*-
"""folha.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GBVpJwJlHZfgeEdRZDpRDbfKUOCOkB_Z
"""

def calcularsal():
    print("Folha de pagamentos")
    sal = float(input("Digite a quantidade de salarios que recebe: (ref: 1518)"))
    sal *= 1518
    if (sal >= 1850):
        sal *= 0.89
        print("O seu salario apos o desconto de 11% de INSS ficara {}".format(sal))
    else:
        print("O seu salario e isento de INSS e continuara sendo {}".format(sal))

while True:
    calcularsal()
    confirma=input("novo calculo? [S/N]: ")
    if confirma.lower() == 'n':
        break