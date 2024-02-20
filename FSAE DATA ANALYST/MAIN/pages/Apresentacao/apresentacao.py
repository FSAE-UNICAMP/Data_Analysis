import PySimpleGUI as sg

def tela_apresentacao():
    sg.theme('SystemDefaultForReal')
    layout = [
        [sg.Text("Seja bem vindo ao software de análise de dados da FSAE Unicamp")],
        [sg.Button("Clique para entrar")]
    ]
    return sg.Window("Apresentação", layout=layout, finalize=True, icon="icone_pysimplegui.ico")
