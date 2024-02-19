import pandas as pd

def sincroniza_gps_ft(file_ft, log_gopro_gps, log_gopro_acelerometro):
# PEGANDO MAIOR VALOR DE ACELERAÇÃO DE TELEMETRIA FUELTECH
    file_ft = pd.read_csv(file_ft)
    valor_max_ft = file_ft["Força_G_aceleração"][:260].values.max()
    file_ft_sync = file_ft.loc[file_ft.index[file_ft["Força_G_aceleração"].astype(str).str.contains("{}".format(valor_max_ft))].tolist()[0]: ].reset_index().drop(columns=["index"])

# JUTANDO LOGS DE ACELERACAO E GPS DA GOPRO E TENTANDO IGUALAVAR VELOCIDADE DE LEITURA, SENDO DO ACELEROMETRO DE 4 E 5 E DO GPS DE 136:
    file_gopro = pd.read_csv(log_gopro_gps)
    file_gps = pd.read_csv(log_gopro_acelerometro)

# IGUALANDO A LEITURA DE 40MS DA FUELTECH
    vet = []
    for i in range(0, len(file_gopro.index)):
        if list(str(file_gopro["date"].loc[i]).split(".")[1])[:3][2] != "0":
            vet.append(i)
    file_gopro = file_gopro.drop(vet)

    file_gopro = file_gopro.reset_index().drop(columns=["index"])
    file_ft_sync = file_ft_sync[::3]
    file_gopro = file_gopro[::2]
    file_gps = file_gps.drop(columns=["cts","date"])
    file_gopro = file_gopro.join(file_gps, how="right").dropna().reset_index().drop(columns=["cts","index"])

# PEGANDO MAIOR VALOR DE ACELERAÇÃO DE TELEMETRIA GOPRO
    valor_max_gopro = file_gopro["Accelerometer (x) [m/s2]"][:850].values.max()
    file_gopro_sync = file_gopro[file_gopro.index[file_gopro["Accelerometer (x) [m/s2]"][:850].astype(str).str.contains("{}".format(valor_max_gopro))].tolist()[0]: ].reset_index()

# DEIXANDO CASAS DECIMAIS COM PRECISÃO DE 10MS DA GO PRO, PARA QUE FIQUE COM A MESMA PRECISÃO DA FT
    df_sincronizado = file_ft_sync.join(file_gopro_sync, how="right").dropna()
    return(df_sincronizado)

# POSSIVEL PROBLEMA NO PROGRAMA, O TEMPO DA FT ESTÁ VARIANDO DE 40 EM 40 MS E O DA GOPRO EU SETEI DE 70 EM 70
#ENTRETANTO, O DO GPS VARIA DE 136ms EM 136ms, PORTANTO AGORA O DA GOPRO IRA EM 140ms E O DA FT EM 120ms
#arquivo1 = r"C:/Users/Samsung/Desktop/TOFS/Scripts/dados.csv"
#arquivo2 = r"C:/Users/Samsung/Desktop/TOFS/GH010198.MP4_gps_csv"
#arquivo3 = r"C:/Users/Samsung/Desktop/TOFS/GH010198.MP4_acelerometro_csv"
#print(sincroniza_gps_ft(arquivo1, arquivo2, arquivo3))