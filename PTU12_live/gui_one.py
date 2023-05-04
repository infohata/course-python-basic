import PySimpleGUI as sg

layout = [
    (sg.Text("Kaip sekasi?"), ),
    (sg.Input(key="-INPUT-"), ),
    (sg.Text(size=(40, 1), key="-OUTPUT-"), ),
    (sg.Button("Atsakyti"), ),
]

window = sg.Window("Nuotaikos tikrinimas", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    window["-OUTPUT-"].update(
        f'Supratom, kad jums sekasi {values["-INPUT-"]}',
        background_color="black",
        text_color="green",
    )
    # print(f"Supratom, kad jums sekasi {values[0]}")

window.close()
