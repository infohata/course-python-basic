import PySimpleGUI as sg

layout = [
    [sg.Text("Koks tavo vardas?")],
    [sg.Input(key='-INPUT-')],
    [sg.Button("Pasisveikinti"), sg.Button("Išeiti")],
    [sg.Text(size=(40, 1), key='-OUTPUT-')]
]

window = sg.Window("Labas!", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Išeiti":
        break

    window['-OUTPUT-'].update(
        f"Labas {values['-INPUT-']}, geros dienos!",
        text_color='#ffeecc'
    )

window.close()
