import pandas as pd

def filtrar_por_tempo(arquivo, tempo_inicial, tempo_final):
    df = pd.read_csv(arquivo, encoding="utf-8")
    df_filtrado = (df[(df['TIME'] >= tempo_inicial) & (df['TIME'] <= tempo_final)])
    return df_filtrado

#teste da função
#filtrar_por_tempo("teste.csv", int(823.261), int(853.301))