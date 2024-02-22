def tela_cortes():
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
    return sg.Window("Análise", layout=layout, finalize=True, icon="icone_pysimplegui.ico")
