import PySimpleGUI as sg
import webbrowser
import cortar_log, bibliotecas, undesteer_caio
import os

# Funções de janelas
def tela_apresentacao():
    sg.theme('SystemDefaultForReal')
    layout = [
        [sg.Text("Seja bem vindo ao software de análise de dados da FSAE Unicamp")],
        [sg.Button("Clique para entrar")]
    ]
    return sg.Window("Apresentação", layout=layout, finalize=True)

def tela_menu():
    sg.theme('SystemDefaultForReal')
    layout = [
        [sg.Button("Bibliografia")],
        [sg.Button("Acesso ao GitHub")],
        [sg.Button("Fazer Análise")]
    ]
    return sg.Window("Menu", layout=layout, finalize=True)

def tela_bibliografia():
    sg.theme('SystemDefaultForReal')
    layout = [
        [sg.Text("Selecione o diretório para salvar a bibliografia")],
        [sg.Input(key="pasta_bibliografia"), sg.FolderBrowse()],
        [sg.Button("Segers")],
        [sg.Button("Biblioteca 2")],
        [sg.Button("Biblioteca 3")],
        [sg.Button("Voltar")]
    ]
    return sg.Window("Bibliografia", layout=layout, finalize=True)

def tela_github():
    webbrowser.open("https://github.com/Rafael-Tobias/FSAE")
    return

def tela_analise():
    sg.theme('SystemDefaultForReal')
    layout = [
        [sg.Text("Entre com o arquivo .csv")],
        [sg.Input(key="arquivo"), sg.FileBrowse()],
        [sg.Checkbox("Corte por tempo", key="tempo"),
         sg.Checkbox("Corte por botão do 2 step(Arrancada)", key="botao"),
         sg.Checkbox("Corte por distância", key="distancia"),
         sg.Checkbox("Sem corte", key="sem_corte")],
        [sg.Button("Iniciar Análise"), sg.Button("Voltar")]
    ]
    return sg.Window("Análise", layout=layout, finalize=True)

def tela_corte_tempo():
    sg.theme('SystemDefaultForReal')
    layout = [
        [sg.Text("Entre com início do tempo"), sg.Input(key="inicio_tempo")],
        [sg.Text("Entre com o fim do tempo"), sg.Input(key="fim_tempo")],
        [sg.Button("Próximo Passo"), sg.Button("Voltar")]
    ]
    return sg.Window("Corte por Tempo", layout=layout, finalize=True)

def tela_obter_valores():
    sg.theme('SystemDefaultForReal')
    layout = [
        [sg.Text("Wheelbase Value (meters): "), sg.Input(key="wheelbase")],
        [sg.Text("Steer ratio Value: "), sg.Input(key="steer_ratio")],
        [sg.Button("OK")]
    ]
    return sg.Window("Valores", layout=layout, finalize=True)

def tela_habilitar_gps_ao_log():
    sg.theme('SystemDefaultForReal')
    layout = [
        [sg.Text("Por favor, adicione o local do arquivo de log: ")],
        [sg.Input(key="arquivo_log"), sg.FileBrowse()],
        [sg.Text("Por favor, adicione o local do arquivo de gps: ")],
        [sg.Input(key="arquivo_gps"), sg.FileBrowse()],
        [sg.Text("Por favor, adicione o log de acelerometro: ")],
        [sg.Input(key="arquivo_acelerometro"), sg.FileBrowse()],
        [sg.Button("OK")]
    ]
    return sg.Window("Habilitar GPS ao Log", layout=layout, finalize=True)

def tela_final():
    sg.theme('SystemDefaultForReal')
    layout = [
        [sg.Button("Undesteer Angle")],
        [sg.Button("Average Combined G")],
        [sg.Button("Habilitar GPS ao Log")],
        [sg.Button("Voltar")]
    ]
    return sg.Window("Tela Final", layout=layout, finalize=True)

# Programa principal
janelas = [tela_apresentacao, tela_menu, tela_bibliografia, tela_analise, tela_corte_tempo, tela_final]
indice_janela_atual = 0
pasta_bibliografia = None

while True:
    janela_atual = janelas[indice_janela_atual]()
    event, values = janela_atual.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "Clique para entrar":
        indice_janela_atual = 1

    elif event == "Bibliografia":
        indice_janela_atual = 2
    
    elif event == "Segers":
        local_destino_download_bibliografia = (r"{}".format(values["pasta_bibliografia"]))
        bibliotecas.baixar_arquivo(local_destino_download_bibliografia)

    elif event == "Acesso ao GitHub":
        tela_github()

    elif event == "Fazer Análise":
        indice_janela_atual = 3

    elif event == "Iniciar Análise":
        local_log = (r"{}".format(values["arquivo"]))
        if values["tempo"]:
            indice_janela_atual = 4
        else:
            indice_janela_atual = 5  

    # Página depois de selecionar os tempos para cortar
    elif event == "Próximo Passo":
        tempo_inicial = float(values["inicio_tempo"])
        tempo_final = float(values["fim_tempo"])
        df_filtrado = cortar_log.filtrar_por_tempo(local_log, tempo_inicial, tempo_final)
        print(df_filtrado)
        indice_janela_atual = 5

    # Primeira função
    elif event == "Undesteer Angle":
        # Abrir janela para obter valores de "Wheelbase" e "Steer ratio"
        valores_window = tela_obter_valores()
        event, valores = valores_window.read()
        valores_window.close()

        if event == "OK":
            wheelbase = float(valores["wheelbase"])
            steer_ratio = float(valores["steer_ratio"])
            print(steer_ratio)
            undesteer_caio.caio_analises1(df_filtrado, wheelbase, steer_ratio)

    elif event == "Habilitar GPS ao Log":
        habilitar_gps_window = tela_habilitar_gps_ao_log()
        event, valores = habilitar_gps_window.read()
        habilitar_gps_window.close()

        if event == "OK":
            arquivo_log = valores["arquivo_log"]
            arquivo_gps = valores["arquivo_gps"]
            arquivo_acelerometro = valores["arquivo_acelerometro"]
            # Faça algo com os arquivos selecionados, por exemplo, processar ou armazenar

    elif event == "Voltar":
        if indice_janela_atual > 0:
            indice_janela_atual -= 1

    janela_atual.close()

# Fechando todas as janelas ao sair do loop
sg.WIN_CLOSED
