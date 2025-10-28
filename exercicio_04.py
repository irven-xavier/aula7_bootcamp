from typing import List

def calcular_desvio_padrao(valores: List[float]) -> float:
    media = sum(valores) / len(valores)
    variancia = sum((x - media) ** 2 for x in valores) / len(valores)
    return variancia ** 0.5

if __name__ == "__main__":

    lista_de_valores = [2.0, 3.7, 9.0, 3, 10]

    resultado = calcular_desvio_padrao(lista_de_valores)

    print(f'{resultado:.2f}')