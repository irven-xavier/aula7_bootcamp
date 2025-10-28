from typing import List

def contar_valores_unicos(lista: List[int]) -> int:
    return len(set(lista))

if __name__ == "__main__":

    lista_valores = [1, 2, 3, 4, 4, 4, 5, 6, 44, 6]

    valores_unicos = contar_valores_unicos(lista_valores)

    print(valores_unicos)