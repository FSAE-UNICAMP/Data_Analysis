def tela_obter_valores():
    sg.theme('SystemDefaultForReal')
    layout = [
        [sg.Text("Wheelbase Value (meters): "), sg.Input(key="wheelbase")],
        [sg.Text("Steer ratio Value: "), sg.Input(key="steer_ratio")],
        [sg.Button("OK")]
    ]
    return sg.Window("Valores", layout=layout, finalize=True, icon="icone_pysimplegui.ico")
