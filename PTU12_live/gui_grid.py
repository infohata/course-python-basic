import PySimpleGUI as sg

layout = [
    [sg.Text("Vardas", size=20), sg.Input(key="vardas", size=20)],
    [sg.Text("Pavardė", size=20), sg.Input(key="pavardė", size=20)],
    [
        sg.Text("Gimimo data", size=20),
        sg.Input(key="metai", size=5),
        sg.Input(key="mėnuo", size=3), 
        sg.Input(key="diena", size=3), 
    ],
    [sg.Button("Patvirtinti")],
    [sg.Text(key="confirmation")],
]

window = sg.Window("Pavyzdys", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    window['confirmation'].update(
        f"{values['vardas']} {values['pavardė']} gimė " + \
        f"{values['metai']}-{values['mėnuo']}-{values['diena']}"
    )

window.close()
