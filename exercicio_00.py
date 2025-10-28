from typing import List

def calcular_media(valores: List[float]) -> float:
    return sum(valores) / len(valores)

if __name__ == "__main__":
    resultado = calcular_media(valores=[9,3])

    print(resultado)