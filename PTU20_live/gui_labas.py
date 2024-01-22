import PySimpleGUI as sg

layout = [
    [sg.Text("Koks tavo vardas?", font="Verdana 15")],
    [sg.Input(key="-NAME-", font="Terminal 15")],
    [
        sg.Button("Pasisveikinti", key="-HELLO-"), 
        sg.Button("Atsisveikinti", key="-BYE-"),
    ],
    [sg.Text(size=(40, 1), key="-OUTPUT-", font="Verdana 15")],
]

window = sg.Window("LABAS", layout)
sg.DEFAULT_FONT

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    if event == "-HELLO-":
        window["-OUTPUT-"].update(
            f"Sveiki {values['-NAME-']}",
            text_color="#99ff99"
        )
    elif event == "-BYE-":
        window["-OUTPUT-"].update(
            f"Viso gero {values['-NAME-']}",
            text_color="#ff9999"
        )

window.close()
