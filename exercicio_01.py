from typing import List

def filtrar_acima_de(valores: List[float], limite: float) -> List[float]:
    
    resultado = []
    
    for valor in valores:
        if valor > limite:
            resultado.append(valor)

    return resultado

if __name__ == "__main__":

    lista_de_valores = [10, 10.2, 1000, 1908, 178.02]

    resultados = filtrar_acima_de(valores=lista_de_valores, limite=999)

    print(resultados)