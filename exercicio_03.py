from typing import List

def celsius_para_fahrenheit(temperaturas_celsius: List[float]) -> List[float]:
    
    return [(9/5) * temp + 32 for temp in temperaturas_celsius]

if __name__ == "__main__":

    temps_em_celsius = [0, 30.1, 25.9, 10, -10]

    temps_em_fahrenheit = celsius_para_fahrenheit(temps_em_celsius)

    print(temps_em_fahrenheit)