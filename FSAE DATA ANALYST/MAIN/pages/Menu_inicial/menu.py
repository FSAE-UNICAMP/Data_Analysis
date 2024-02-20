def tela_menu():
    sg.theme('SystemDefaultForReal')
    layout = [
        [sg.Button("Bibliografia")],
        [sg.Button("Acesso ao GitHub")],
        [sg.Button("Fazer Análise")]
    ]
    return sg.Window("Menu", layout=layout, finalize=True, icon="icone_pysimplegui.ico")
