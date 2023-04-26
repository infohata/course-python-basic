# Loginimas

Loginimas yra procesas, kai informacija apie įvykius, veiksmus, klaidas ir kt. yra užrašoma į atskirą failą arba įrašoma į konsolę. Loginimas yra svarbus norint stebėti programos veikimą, nes jis leidžia sekti, ką daro programa ir kaip ji reaguoja į tam tikras situacijas.

Python programavimo kalboje loginimo mechanizmas yra įgyvendintas su moduliu `logging`. Šis modulis leidžia pritaikyti loginimo mechanizmą pagal savo poreikius, pavyzdžiui, nustatant loginimo lygį, loginimo pranešimo formatą, loginimo tikslą ir kt.

## Standartinis `logger` iš `logging`

<!-- Nesugalvoju šios dalies (facepalm emoji) -->

```Python
import logging

logging.warning("Klaida!")
```

Rezultatas:

```Text
WARNING:root:Klaida!
```

## Pranešimų lygiai - `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`

Python loginimo sistemą sudaro keletas iš anksto apibrėžtų pranešimo lygių:

- `DEBUG` - naudojamas, kai reikia daugiau informacijos apie vykdymą. Tai yra aukščiausias pranešimo lygis.
- `INFO` - naudojamas informuoti apie normalų vykdymą ir kodą, kuris jau yra įvykdytas sėkmingai.
- `WARNING` - naudojamas, kai programa susiduria su problema, kuri gali turėti neigiamų padarinių, bet jos vykdymas tęsiasi.
- `ERROR` - naudojamas, kai programa susiduria su problema, dėl kurios negalima tęsti vykdymo.
- `CRITICAL` - naudojamas, kai programa susiduria su rimta klaida, kuri neleidžia programai tęsti vykdymo.

```Python
import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug('Debugging message')
logging.info('Informational message')
logging.warning('Warning message')
logging.error('Error message')
logging.critical('Critical message')
```

Šiame pavyzdyje nustatome loginimo lygį `DEBUG` lygyje, ir tada iškviečiame kelis logerio metodus, kurie išveda pranešimus į konsolę. Priklausomai nuo nustatytos loginimo lygio reikšmės, bus išvesti arba nebus išvesti visi pranešimai:

```Python
DEBUG:root:Debugging message
INFO:root:Informational message
WARNING:root:Warning message
ERROR:root:Error message
CRITICAL:root:Critical message
```

## Minimalaus loginimo lygio nustatymas

Minimalaus loginimo lygio nustatymas yra svarbus komponentas norint kontroluoti kokius log'us gauti ir kokius ignoruoti. Tai yra naudinga, kai norite matyti tik tam tikro lygio logus, o likusius ignoruoti ir padidinti įrašų skaitymo efektyvumą.

Norint nustatyti minimalų loginimo lygį, reikia nustatyti reikiamą lygio parametrą loggerio konfigūracijoje, pvz.:

```Python
import logging

# nustatomas minimalus lygis į INFO
logging.basicConfig(level=logging.INFO)
```

Kai lygis nustatomas į `INFO`, bus atvaizduojami visi log'ai, kurių lygis yra `INFO` arba didesnis. Kitų lygių log'ai, tokie kaip `DEBUG`, nebus atvaizduojami, pvz.:

```Python
# loggeris sukuriamas
logger = logging.getLogger(__name__)

# pranešimai
logger.debug("Šis pranešimas nebus atvaizduotas")
logger.info("Šis pranešimas bus atvaizduotas")
```

Rezultatas:

```Text
INFO:__main__:Šis pranešimas bus atvaizduotas
```

Norint ignoruoti visus pranešimus, išskyrus kritinius, tereikia nustatyti minimalų loginimo lygį į `CRITICAL`:

```Python
import logging

# nustatomas minimalus lygis į CRITICAL
logging.basicConfig(level=logging.CRITICAL)

# loggeris sukuriamas
logger = logging.getLogger(__name__)

# pranešimai
logger.debug("Šis pranešimas nebus atvaizduotas")
logger.info("Šis pranešimas nebus atvaizduotas")
logger.warning("Šis pranešimas nebus atvaizduotas")
logger.error("Šis pranešimas nebus atvaizduotas")
logger.critical("Šis pranešimas bus atvaizduotas")
```

Rezultatas:

```Text
CRITICAL:__main__:Šis pranešimas bus atvaizduotas
```

## Loginimas į failą

Loginimas į failą yra dažnas būdas sekti, kas vyksta programoje, ypač kai ji veikia ilgai arba yra pasiekiama per kelias mašinas. Šio tipo loginimas leidžia saugoti informaciją apie programos veikimą ir analizuoti ją vėliau. Pvz.:

```Python
import logging

logging.basicConfig(filename='logeris.log', encoding="UTF-8", level=logging.INFO)
logging.info("Programa veikia")
```

Kiekvienas pranešimas bus pridėtas prie `logeris.log` failo, todėl programą paleidus kelis kartus, galime matyti visą programos veikimą:

```Text
INFO:root:Programa veikia
INFO:root:Programa veikia
```

## Loginimo pranešimo formatas

Loginimo pranešimo formatas yra svarbus, nes jis nusako, kaip informacija bus išvedama į `log` failą. Pagrindiniai loginimo pranešimo formatavimo elementai yra: laiko žymė, loginimo lygis, pranešimas ir kita papildoma informacija.

Formatavimo simboliai:

- `asctime` - laiko žymė, kuri nurodo, kada pranešimas buvo išvestas.
- `name` - loggerio pavadinimas.
- `levelname` - loginimo lygis.
- `message` - pranešimas, kuris bus išvestas.

```Python
import logging

logging.basicConfig(
    filename='logeris.log', 
    encoding='UTF-8', 
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logging.info('Programa veikia')
```

Rezultatas:

```Text
2023-04-14 08:31:17,279 - root - INFO - Programa veikia
```

Daugiau formatavimo parametrų čia: <https://docs.python.org/3/library/logging.html#logrecord-attributes>

## Loginimas su objektais

Logerio pranešimas gali būti ne tik paprastas tekstas, tačiau į jį galima įtraukti pvz. objektus:

```Python
import logging

logging.basicConfig(filename='logeris.log', encoding="UTF-8",
level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

class Asmuo:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde
        logging.info(f"Sukurtas darbuotojas: {self.vardas} {self.pavarde}")

tadas = Asmuo("Jonas", "Jonaitis")
rokas = Asmuo("Petras", "Petraitis")
```

Rezultatas:

```Text
2023-04-14 08:34:23,184:INFO:Sukurtas darbuotojas: Jonas Jonaitis
2023-04-14 08:34:23,185:INFO:Sukurtas darbuotojas: Petras Petraitis
```

## Savo logger'io sukūrimas

Vienas iš standartinio loggerio trūkumų yra tas, kad jis yra globalus ir naudojamas visam programos kodo blokui. Tai gali būti problematiška didesniuose projektuose, kai reikia tiksliai nustatyti, kur koks pranešimas turėtų būti išspausdintas.

Vienas iš būdų išspręsti šią problemą yra sukurti savo logger'į. Tai leis naudoti skirtingus loggerius skirtinguose programos vietose ir nustatyti skirtingus lygius bei nustatymus. Pvz.:

```Python
import logging

def create_logger(logger_name, log_file):
    # Sukuriamas logger'is
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    
    # Sukuriamas log handleris, kad pranešimai būtų išsaugomi į failą
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)

    # Sukuriamas formatteris, kad pranešimai būtų formatuojami pagal pageidavimą
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Priskiriamas handleris loggeriui
    logger.addHandler(file_handler)

    return logger

# Naudojimo pavyzdys
mano_logeris = create_logger('mano_logeris', 'naujas_logeris.log')
mano_logeris.debug('Debug pranešimas')
mano_logeris.info('Info pranešimas')
mano_logeris.warning('Warning pranešimas')
```

Rezultatas naujai sukurtame faile `naujas_logeris.log`:

```Text
2023-04-14 08:42:10,941 - mano_logeris - DEBUG - Debug pranešimas
2023-04-14 08:42:10,942 - mano_logeris - INFO - Info pranešimas
2023-04-14 08:42:10,942 - mano_logeris - WARNING - Warning pranešimas
```

## Loginimas į failą ir į terminalą

Logeris gali nukreipti savo išvestis į skirtingus kanalus, pvz. į failą ir į terminalą. Tai yra naudinga, kai norite matyti pranešimus tiesiogiai terminalo lange, taip pat ir juos išsaugoti faile ilgesniam saugojimui. Pvz.:

```Python
# Sukuriame console handler'į, kuris spausdins pranešimus į terminalą
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

# Pridedame handler'ius į logger'į
logger.addHandler(file_handler) 
logger.addHandler(console_handler)
```

Visas pilnas kodas:

```Python
import logging

def create_logger(logger_name, log_file):
    # Sukuriamas logger'is
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    
    # Sukuriamas log handleris, kad pranešimai būtų išsaugomi į failą
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)

    # Sukuriamas formatteris, kad pranešimai būtų formatuojami pagal pageidavimą
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Sukuriame console handler'į, kuris spausdins pranešimus į terminalą
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    # Pridedame handler'ius į logger'į
    logger.addHandler(file_handler) 
    logger.addHandler(console_handler)

    return logger

# Naudojimo pavyzdys
mano_logeris = create_logger('mano_logeris', 'naujas_logeris.log')
mano_logeris.debug('Debug pranešimas')
mano_logeris.info('Info pranešimas')
mano_logeris.warning('Warning pranešimas')
```

Rezultatas terminale:

```Text
2023-04-14 08:46:19,370 - mano_logeris - DEBUG - Debug pranešimas
2023-04-14 08:46:19,371 - mano_logeris - INFO - Info pranešimas
2023-04-14 08:46:19,371 - mano_logeris - WARNING - Warning pranešimas
```

Rezultatas faile:

```Text
2023-04-14 08:46:19,370 - mano_logeris - DEBUG - Debug pranešimas
2023-04-14 08:46:19,371 - mano_logeris - INFO - Info pranešimas
2023-04-14 08:46:19,371 - mano_logeris - WARNING - Warning pranešimas
```

## Klaidų loginimas su `logger.exception`

`logging` modulis turi metodą `exception`, kuris leidžia išsaugoti pranešimą apie klaidą ir jos išsamesnę informaciją. Pvz.:

```Python
import logging

logging.basicConfig(filename='logeris.log', encoding='utf-8', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    a = 1 / 0
except Exception as e:
    logging.exception("Klaida: %s", e)
```

Rezultatas:

```Text
2023-04-14 08:51:47,068 - ERROR - Klaida: division by zero
Traceback (most recent call last):
  File "main.py", line 6, in <module>
    a = 1 / 0
ZeroDivisionError: division by zero
```

## Užduotys

### Pirma užduotis

Patobulinkite savo šaldytuvo programą:

- Gaudykite visas galimas vartotojo sąsajos klaidos, ypač įvedant kiekius.
- Šaldytuvo saugojimo į failą/ištraukimo iš failo klaidų gaudymą galite įgyvendinti per `try` `except`.
- Sukurkite loggerį, kuris į failą kauptų informaciją apie įdėtus ir išimtus produktus su kiekiais, ir veiksmo data/laiku.

### Antra užduotis

Patobulinkite savo biudžeto programą:

- gaudykite klaidą, vartotojui įvedant neteisingus parametrus kuriant pajamų arba išlaidų įrašus.
- sukurkite loggerį, kuris logintų, kada vartotojas bando išleisti daugiau pinigų, negu turi.
