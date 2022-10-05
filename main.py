import pdb
from turtle import pd

#pdb.set_trace()

def es_primo(n):
    if n % 2 == 0:
        num_f = n/2
    else:
        num_f = int(n/2) + 1
    
    num_f = int(num_f)

    res = True
    for numero in range(num_f):
        numero_1 = numero + 1
        if numero_1 > 1:
            if n % numero_1 == 0:
                res = False
    return res

def main():
    # PARTE 1
    # Definiendo la lista 
    lista = [[2, 4, 1,7], [1,2,56,7,11,8], [102,224,43,121]]

    # Utilizando la funcion max definimos el valor maximo de cada lista contenida
    # en la lista inicial
    arr_max = [max(elemento) for elemento in lista]

    # Imprimimos el resultado final
    print(arr_max)


    # PARTE 2
    lista_1 = [3, 4, 8, 5, 5, 22, 13]
    arr_primo = list(filter(es_primo,lista_1))

    print(arr_primo)

    return 0

if __name__ == '__main__':
    main()
    