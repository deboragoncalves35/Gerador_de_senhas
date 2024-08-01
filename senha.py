import random


print('Ola, irei te ajudar a gerar uma senha.')

caracter = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*-_=+'
    

quant = int(input('Quantas senhas você deseja gerar? '))
tamanho = int(input('Qual tamanho da sua senha? '))

for c in range(quant):
    senha = ''
    for a in range(tamanho):
        senha += random.choice(caracter)
    print (senha)


