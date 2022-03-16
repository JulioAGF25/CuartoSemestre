#!/usr/bin/python3
#-*-coding: utf-8 -*-
#
# Metodo para validar una tarjeta de debito, empleando el
# algoritmo de construccion de los numeros pseudoaleatorios.
#
# Kiovahn Leon
# Mar/15/22
# al20760618.at.ite.dot.edu.dot.mx
#

import math

def CambiarDigitos(digitos):
    decimales=[10,11,12,13,14,15]
    hexadecimal=['A','B','C','D','E','F']
    for c in range(7):
        if digitos==decimales[c-1]:
            digitos=hexadecimal[c-1]
    return(digitos)


def DecimalAHexadecimal(decimal):
    hexadecimal=''
    while decimal!=0:
        rem=CambiarDigitos(decimal%16)
        hexadecimal=str(rem)+hexadecimal
        decimal=int(decimal/16)
    return(hexadecimal)

def aleatorio(a,b,m,semilla,longitud):
    rnd=[]
    rnds=[]
    rnd.append(semilla)
    for j in range(longitud+1):
        valor=(a*rnd[j]+b)%m
        rnd.append(valor)
        if j>0:
            rnds.append(valor/m)
    return (rnds)


def main():
    cadena="Casi casi"
    a=1921
    b=888
    modulo=333
    semilla=0
    for i in range(len(cadena)):
        caracter=cadena[i]
        asci=ord(caracter)
        semilla+=asci
    aleatorios=aleatorio(a,b,modulo,semilla,len(cadena))
    texto=''

    for i in range(len(cadena)):
        caracter=cadena[i]
        asci=ord(caracter)
        termino=DecimalAHexadecimal(math.ceil(asci*aleatorios[i]))
        texto+=termino
    print("La contraseña es {}".format(texto))

if __name__ == '__main__':
    main()
