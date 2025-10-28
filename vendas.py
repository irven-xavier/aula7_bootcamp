from typing import List
import pandas as pd

def ler_arquivo_csv():

    df = pd.read_csv('data\vendas.csv', sep=',', encoding='utf-8')