from typing import List
import csv

path = r'data\vendas.csv'

def ler_arquivo_csv(nome_arquivo: str) -> List[dict]:

    lista = []

    with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:

        leitor = csv.DictReader(arquivo)

        for linha in leitor:

            lista.append(linha) 

    return lista

def filtrar_eletronicos(lista: dict) -> list[dict]:

    lista_com_eletronicos = []

    for produto in lista:

        if produto.get('Categoria') == 'Electronics':

            lista_com_eletronicos.append(produto)

    return lista_com_eletronicos

def valor_dos_eletronicos(lista_com_eletronicos: list[dict]) -> int:

    valor_total = 0

    for produto in lista_com_eletronicos:

        valor_total += int(produto.get('Venda'))

    return valor_total

lista_produtos = ler_arquivo_csv(path)

eletronicos = filtrar_eletronicos(lista_produtos)

valor_total = valor_dos_eletronicos(eletronicos)

print(valor_total)