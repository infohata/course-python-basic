# PySimpleGUI

PySimpleGUI yra Python paketas, leidžiantis visų lygių Python programuotojams kurti grafines vartotojo sąsajas (GUI). Naudodami "išdėstymą" ("layout"), kuriame yra valdikliai (PySimpleGUI jie vadinami "Elementais") jūs apibrėžiate savo GUI. Išdėstymas naudojamas sukurti langą, naudojant vieną iš 4 palaikomų sistemų, kad būtų galima interaktyviai naudotis sukurtu langu.

## Funkcionalumas

- Paprasta naudoti
- 4 palaikomos sistemos: tkinter, PyQt, wxPython, Remi
- Palaiko sudėtingas daugialanges sąsajas
- Palaiko platų valdiklių asortimentą, įskaitant mygtukus, teksto laukus, slankjuosčius ir kt.
- Palaiko individualias temas ir spalvas
- Palaiko įvykiais grįstą programavimą
- Išsami dokumentacija

![Getting over the GUI bar](/images/pysimple/01.jpg)

## Instaliavimas

```text
pip install PySimpleGUI
```

```text
pip freeze >requirements.txt
```

## "One-Shot" langas

Šis programos tipas vadinamas "One-Shot" programa, nes langas yra rodomas vieną kartą: surenkamos reikšmės ir po to jis yra uždaromas.

```Python
import PySimpleGUI as sg  # 1 dalis - Importavimas

# Apibrėžiame lango turinį
layout = [
    [sg.Text("Koks tavo vardas?")],  # 2 dalis - Išdėstymas
    [sg.Input()],
    [sg.Button("Patvirtinti")]]

# Sukuriamas langas
window = sg.Window("Lango Pavadinimas", layout)  # 3 dalis - Lango Apibrėžimas

# Atvaizduojame ir bendraujame su langu
event, values = window.read()  # 4 dalis - Įvykio kilpa arba Window.read() kvietimas

# Kažką darome su surinkta informacija
print("Sveiki", values[0], "! Ačiū, kad išbandėte PySimpleGUI")

# Baigiame darbą, pašalindami langą iš ekrano
window.close()  # 5 dalis - Uždaryti langą
```

## Interaktyvus langas

Šiame pavyzdyje mūsų langas liks ekrane, kol vartotojas uždarys langą arba paspaus „Išeiti“ mygtuką. Pagrindinis skirtumas tarp anksčiau matyto vienkartinio lango ir interaktyvaus lango yra "Įvykių Kilpa". Įvykių kilpa skaito įvykius ir įvestis iš jūsų lango.

```Python
import PySimpleGUI as sg

# Apibrėžiame lango turinį
layout = [
    [sg.Text("Koks tavo vardas?")],
    [sg.Input(key="-INPUT-")],
    [sg.Text(size=(40, 1), key="-OUTPUT-")],
    [sg.Button("Patvirtinti"), sg.Button("Išeiti")],
]

# Sukuriamas langas
window = sg.Window("Lango Pavadinimas", layout)

# Atvaizduojame ir bendraujame su langu, naudodami įvykių kilpą
while True:
    event, values = window.read()
    # Žiūrime, ar vartotojas nori išeiti, ar langas buvo uždarytas
    if event == sg.WINDOW_CLOSED or event == "Išeiti":
        break
    # Išvedame pranešimą į langą
    window["-OUTPUT-"].update(
        "Sveiki " + values["-INPUT-"] + "! Nusišypsokite dienai :)", text_color='#F7D060'
    )

# Baigiame darbą, pašalindami langą iš ekrano
window.close()
```

Pasižiūrėkime į kelis skirtumus tarp šio pavyzdžio ir "One-Shot" lango.

Pirma, pastebėsite išdėstymo skirtumus. Yra dvi ypač svarbios pakeitimų. Viena iš jų yra parametrų `key` pridėjimas į `Input` elemento ir vieno iš `Text` elementų. `Key` yra kaip elementui skirtas pavadinimas. Arba Python kalba tariant, tai yra žodyno raktas. Vėliau kode `Input` elemento raktas bus naudojamas kaip žodyno raktas.

Kitas skirtumas yra šio `Text` elemento pridėjimas:

```Python
[sg.Text(size=(40,1), key='-OUTPUT-')],
```

Čia pateikti 2 parametrai, vienas jau aptartas - tai `key`. Parametras "size" apibrėžia elemento dydį simboliais. Šiuo atveju mes nurodome, kad šis `Text` elementas yra 40 simbolių pločio ir 1 simbolio aukščio. Pastebėkite, kad nėra nurodytas joks tekstas, tai reiškia, kad jis bus tuščias. Tuščią eilutę galite lengvai pamatyti sukurtame lange.

Mes taip pat pridėjome mygtuką "Išeiti".

Įvykių ciklas turi mūsų įprastą `langas.read()` kvietimą.

Po read seka šis if teiginys:

```Python
if event == sg.WINDOW_CLOSED or event == 'Išeiti':
    break
```

Šis kodas tikrina, ar vartotojas uždaro langą spustelėdamas "X" ar spustelėjo mygtuką "Išeiti". Jei įvyksta bet kuri iš šių situacijų, tada kodas nutrauks įvykių ciklą.

Jei langas nebuvo uždarytas ir nebuvo paspaustas "Išeiti" mygtukas, tada vykdymas tęsiasi. Vienintelis dalykas, kuris galėjo įvykti, yra tai, kad vartotojas paspaudė mygtuką "Patvirtinti".

Paskutinis teiginys įvykių cikle yra šis:

```Python
window["-OUTPUT-"].update(
    "Sveiki " + values["-INPUT-"] + "! Nusišypsokite dienai :),text_color='#F7D060'
)
```

Šis teiginys atnaujina `Text` elementą, kuris turi raktą `-OUTPUT-`, su eilute. window['-OUTPUT-'] ieško elemento su raktu `-OUTPUT-`. Tas raktas priklauso mūsų tuščiam `Text` elementui. Kai tas elementas yra grąžinamas iš paieškos, tada kviečiamas jo atnaujinimo metodas. Beveik visi elementai turi atnaujinimo metodą.

## 💡 Elementų parametrai

Kiekvienam elementui galimi parametrai yra aprašyti šioje [dokumentacijoje](https://www.pysimplegui.org/en/latest/call%20reference/). Jei ieškosite `Text` elemento `update` metodo, rasite šį apibrėžimą:

![Update](/images/pysimple/02.jpeg)

## Procedūrinis elementų kūrimas ir išdėstymas

Lango išdėstymas yra "sąrašas iš sąrašų". Langai yra suskaidomi į "eilutes". Kiekviena eilutė jūsų lange tampa sąrašu išdėstyme. Sujungę visus sąrašus, turite išdėstymą... sąrašą iš sąrašų.

```Python
import PySimpleGUI as sg

layout = [[sg.Text("Eilutė 1, Stulpelis 1"), sg.Text("Eilutė 1, Stulpelis 2"), sg.Text("Eilutė 1, Stulpelis 3")],
          [sg.Text("Eilutė 2, Stulpelis 1"), sg.Text("Eilutė 2, Stulpelis 2"), sg.Text("Eilutė 2, Stulpelis 3")],
          [sg.Text("Eilutė 3, Stulpelis 1"), sg.Text("Eilutė 3, Stulpelis 2"), sg.Text("Eilutė 3, Stulpelis 3")],
          [sg.Text("Eilutė 4, Stulpelis 1"), sg.Text("Eilutė 4, Stulpelis 2"), sg.Text("Eilutė 4, Stulpelis 3")]]

window = sg.Window("Pavyzdys", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

window.close()
```

Taip pat galite naudoti ciklus arba net list comprehension, kad sukurtumėte mygtukų tinklelį vienoje kodo eilutėje:

```Python
import PySimpleGUI as sg

layout = [[sg.Button(f'{row}, {col}') for col in range(4)] for row in range(4)]

event, values = sg.Window('List Comprehensions', layout).read(close=True)
```

## Kodo perkeliamumas (angl. code portability)

PySimpleGUI dabar gali veikti keturiuose Python GUI karkasuose. Naudojamas karkasas nurodomas naudojant `import`. Kai kurioms programoms, norint jas paleisti kitame GUI karkase, nereikia papildomų pakeitimų. Keičiant iš PySimpleGUI į PySimpleGUIQt, PySimpleGUIWx, PySimpleGUIWeb, keičiamas karkasas taip:

![Keičiant į kitą karkasą](/images/pysimple/03.png)

## Programa su keliais langais

<!-- TODO: programa su lentele, CRUD veiksmais jos turiniui -->

## Visi elementai viename lange

```Python
import PySimpleGUI as sg

"""
    Demo - Element List
    All elements shown in 1 window as simply as possible.
    Copyright 2022 PySimpleGUI
"""


use_custom_titlebar = True if sg.running_trinket() else False

def make_window(theme=None):
    NAME_SIZE = 23

    def name(name):
        dots = NAME_SIZE-len(name)-2
        return sg.Text(name + ' ' + '•'*dots, size=(NAME_SIZE,1), justification='r',pad=(0,0), font='Courier 10')

    sg.theme(theme)

    # NOTE that we're using our own LOCAL Menu element
    if use_custom_titlebar:
        Menu = sg.MenubarCustom
    else:
        Menu = sg.Menu

    treedata = sg.TreeData()

    treedata.Insert("", '_A_', 'Tree Item 1', [1234], )
    treedata.Insert("", '_B_', 'B', [])
    treedata.Insert("_A_", '_A1_', 'Sub Item 1', ['can', 'be', 'anything'], )

    layout_l = [
                [name('Text'), sg.Text('Text')],
                [name('Input'), sg.Input(s=15)],
                [name('Multiline'), sg.Multiline(s=(15,2))],
                [name('Output'), sg.Output(s=(15,2))],
                [name('Combo'), sg.Combo(sg.theme_list(), default_value=sg.theme(), s=(15,22), enable_events=True, readonly=True, k='-COMBO-')],
                [name('OptionMenu'), sg.OptionMenu(['OptionMenu',],s=(15,2))],
                [name('Checkbox'), sg.Checkbox('Checkbox')],
                [name('Radio'), sg.Radio('Radio', 1)],
                [name('Spin'), sg.Spin(['Spin',], s=(15,2))],
                [name('Button'), sg.Button('Button')],
                [name('ButtonMenu'), sg.ButtonMenu('ButtonMenu', sg.MENU_RIGHT_CLICK_EDITME_EXIT)],
                [name('Slider'), sg.Slider((0,10), orientation='h', s=(10,15))],
                [name('Listbox'), sg.Listbox(['Listbox', 'Listbox 2'], no_scrollbar=True,  s=(15,2))],
                [name('Image'), sg.Image(sg.EMOJI_BASE64_HAPPY_THUMBS_UP)],
                [name('Graph'), sg.Graph((125, 50), (0,0), (125,50), k='-GRAPH-')]  ]

    layout_r  = [[name('Canvas'), sg.Canvas(background_color=sg.theme_button_color()[1], size=(125,40))],
                [name('ProgressBar'), sg.ProgressBar(100, orientation='h', s=(10,20), k='-PBAR-')],
                [name('Table'), sg.Table([[1,2,3], [4,5,6]], ['Col 1','Col 2','Col 3'], num_rows=2)],
                [name('Tree'), sg.Tree(treedata, ['Heading',], num_rows=3)],
                [name('Horizontal Separator'), sg.HSep()],
                [name('Vertical Separator'), sg.VSep()],
                [name('Frame'), sg.Frame('Frame', [[sg.T(s=15)]])],
                [name('Column'), sg.Column([[sg.T(s=15)]])],
                [name('Tab, TabGroup'), sg.TabGroup([[sg.Tab('Tab1',[[sg.T(s=(15,2))]]), sg.Tab('Tab2', [[]])]])],
                [name('Pane'), sg.Pane([sg.Col([[sg.T('Pane 1')]]), sg.Col([[sg.T('Pane 2')]])])],
                [name('Push'), sg.Push(), sg.T('Pushed over')],
                [name('VPush'), sg.VPush()],
                [name('Sizer'), sg.Sizer(1,1)],
                [name('StatusBar'), sg.StatusBar('StatusBar')],
                [name('Sizegrip'), sg.Sizegrip()]  ]

    # Note - LOCAL Menu element is used (see about for how that's defined)
    layout = [[Menu([['File', ['Exit']], ['Edit', ['Edit Me', ]]],  k='-CUST MENUBAR-',p=0)],
              [sg.T('PySimpleGUI Elements - Use Combo to Change Themes', font='_ 14', justification='c', expand_x=True)],
              [sg.Checkbox('Use Custom Titlebar & Menubar', use_custom_titlebar, enable_events=True, k='-USE CUSTOM TITLEBAR-', p=0)],
              [sg.Col(layout_l, p=0), sg.Col(layout_r, p=0)]]

    window = sg.Window('The PySimpleGUI Element List', layout, finalize=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT, keep_on_top=True, use_custom_titlebar=use_custom_titlebar)

    window['-PBAR-'].update(30) # Show 30% complete on ProgressBar
    window['-GRAPH-'].draw_image(data=sg.EMOJI_BASE64_HAPPY_JOY, location=(0,50))   # Draw something in the Graph Element

    return window

window = make_window()

while True:
    event, values = window.read()
    # sg.Print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if values['-COMBO-'] != sg.theme():
        sg.theme(values['-COMBO-'])
        window.close()
        window = make_window()
    if event == '-USE CUSTOM TITLEBAR-':
        use_custom_titlebar = values['-USE CUSTOM TITLEBAR-']
        sg.set_options(use_custom_titlebar=use_custom_titlebar)
        window.close()
        window = make_window()
    if event == 'Edit Me':
        sg.execute_editor(__file__)
    elif event == 'Version':
        sg.popup_scrolled(__file__, sg.get_versions(), keep_on_top=True, non_blocking=True)
window.close()
```

## 💡 Daugiau dokumentacijos ir pavyzdžių

- PySimpleGUI Cookbook: https://www.pysimplegui.org/en/latest/cookbook/
- PySimpleGUI on PyPI: https://pypi.org/project/PySimpleGUI/
- PySimpleGUI Demos: https://www.pysimplegui.org/en/latest/Demos/
