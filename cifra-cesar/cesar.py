# -*- coding: cp852 -*-
from string import ascii_lowercase
import os


def f(frase, chave):
    pos = [letras.index(frase[i]) + chave
                       for i in range(len(frase))
                       if frase[i] in letras]

    for i in pos:
        if i >= 26:
            pos[pos.index(i)] = i%26
		
    cifrada = ''.join([letras[i] for i in pos])
    return cifrada

def r_all(frase, chave):
    descifrada = ''.join([letras[letras.index(frase[i]) - chave]
                       for i in range(len(frase))
                       if frase[i] in letras])
    return descifrada

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
            for i in range(1, 26):
                print(r_all(palavra, i) + ' = ' + str(i))
        elif opcao == '0':
            palavra = raw_input('Insira uma palavra a ser cifrada: ').upper()
            chave = input('Insira uma chave para cifrar: ')
            print(f(palavra, chave))

if __name__ == '__main__':
    main()
