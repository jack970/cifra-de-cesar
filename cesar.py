# -*- coding: cp852 -*-
from string import ascii_lowercase
import os


def encoder(frase, chave):
    return ''.join([letras[(letras.index(i) + chave) % 26]
                       for i in frase if i in letras])

def decoder(frase, chave):
    return ''.join([letras[letras.index(i) - chave]
                       for i in frase if i in letras])

def main():
    opcao = ''
    global letras
    letras = [i.upper() for i in ascii_lowercase]

    while opcao == '' or opcao not in '01':
        os.system('cls && color 0a')
        opcao = raw_input("""  CIFRA DE CêSAR 
        [0] Cifrar 
        [1] Descifrar

    Escolha uma opcao: """)

        if opcao == '1':
            palavra = raw_input('Insira uma palavra a ser descifrada: ').upper()
            print('\nFRASE | CHAVE\n--------------')
            for i in range(1, 26):
                print(decoder(palavra, i) + ' = ' + str(i))
        elif opcao == '0':
            palavra = raw_input('Insira uma palavra a ser cifrada: ').upper()
            chave = input('Insira uma chave para cifrar: ')
            print(encoder(palavra, chave))

if __name__ == '__main__':
    main()
