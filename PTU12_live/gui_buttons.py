import PySimpleGUIQt as sg


layout = [
    [sg.Text("Pick your lucky number")],
]
for row in range(0, 10):
    layout.append([sg.Button(f"{row*10 + col}") for col in range(0, 10)])

window = sg.Window("Button Matrix", layout, location=(100, 100))
event, values = window.read(close=True)
print(values)
