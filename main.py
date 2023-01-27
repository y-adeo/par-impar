# Será que é par ou é ímpar?

while True:
    try:
        valor = int(input('Digite um número inteiro: '))
        if valor % 2 == 0:
            print('Esse é um número par!')
        else:
            print('Esse número é impar!')
    except:
        print('O-ou, isso não é um número inteiro...')
