import pandas as pd

def calcular_correlacao(df):
    """
    Calcula a matriz de correlação entre as variáveis.

    Parameters:
        df (DataFrame): Conjunto de dados.

    Returns:
        DataFrame: Matriz de correlação.
    """
    colunas = ['idade', 'colesterol', 'pressao', 'risco']
    return df[colunas].corr()
