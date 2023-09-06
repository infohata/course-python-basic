import PySimpleGUI as sg

layout = []
rows = "12345678"
columns = "ABCDEFGH"
for row_id, row in enumerate(rows):
    row_list = []
    for col_id, column in enumerate(columns):
        if row_id % 2 == 0:
            if col_id % 2 == 0:
                color = '#ffffff'
                text_color = '#000000'
            else:
                color = '#000000'
                text_color = '#ffffff'
        else:
            if col_id % 2 == 0:
                color = '#000000'
                text_color = '#ffffff'
            else:
                color = '#ffffff'
                text_color = '#000000'
        row_list.append(sg.Button(
            column+row, 
            button_color=(color, text_color), 
            key=f"cell_{column}{row}"
        ))
    layout.append(row_list)

window = sg.Window("Chess", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    print(event)

window.close()
