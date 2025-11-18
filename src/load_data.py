import pandas as pd

def carregar_csv(path="data/risco_cardiaco.csv"):
    """
    Carrega o arquivo CSV com os dados de risco cardíaco.

    Parameters:
        path (str): Caminho do arquivo CSV.

    Returns:
        DataFrame: Dados carregados em um Pandas DataFrame.
    """
    try:
        df = pd.read_csv(path)
        return df
    except:
        raise FileNotFoundError(f"Arquivo não encontrado no caminho: {path}")
