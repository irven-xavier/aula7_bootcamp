from typing import List

def encontrar_valores_ausentes(sequencia: List[int]) -> List[int]:
    
    completo = set(range(min(sequencia), max(sequencia) + 1))
    
    return list(completo - set(sequencia))

if __name__ == "__main__":

    lista_de_valores = [1, 3, 4, 5, 6, 7, 8, 9, 10]

    resultado = encontrar_valores_ausentes(lista_de_valores)

    print(resultado)