def tela_corte_tempo():
    sg.theme('SystemDefaultForReal')
    layout = [
        [sg.Text("Entre com início do tempo"), sg.Input(key="inicio_tempo")],
        [sg.Text("Entre com o fim do tempo"), sg.Input(key="fim_tempo")],
        [sg.Button("Próximo Passo"), sg.Button("Voltar")]
    ]
    return sg.Window("Corte por Tempo", layout=layout, finalize=True, icon="icone_pysimplegui.ico")
