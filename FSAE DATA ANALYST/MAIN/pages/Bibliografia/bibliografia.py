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
    return sg.Window("Bibliografia", layout=layout, finalize=True, icon="icone_pysimplegui.ico")
