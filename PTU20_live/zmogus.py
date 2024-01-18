import pickle
import os
import logging

logging.basicConfig(
    filename='zmones.log', 
    level=logging.DEBUG,
    encoding='utf-8',
    format='%(asctime)s / %(name)s / %(levelname)s / %(message)s'
)

class Zmogus:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius
        logging.debug(f"sukurtas Zmogus objektas: vardas: {self.vardas}, amzius: {self.amzius}")

    def __str__(self):
        return f"{self.vardas}, {self.amzius} metų"


class AgeError(ValueError):
    pass


def input_age(prompt="age: "):
    amzius = int(input(prompt))
    logging.info(f"ivestas amzius: {amzius}")
    if amzius > 100:
        raise AgeError('zmones tiek negyvena')
    if amzius < 0:
        raise AgeError('zmogus mire negimes')
    return amzius

if __name__ == "__main__":
    try:
        vardas = input("vardas: ")
        amzius = input_age("metai: ")
    except ValueError as error: ## arba Exception, arba AgeError
        print(f'Klaida {error.__class__.__name__}: {error}')
        exit()

    zmogus = Zmogus(vardas, amzius)
    ZMONES_FILE = 'PTU20_live/zmones.pkl'

    if os.path.exists(ZMONES_FILE):
        with open(ZMONES_FILE, "rb") as zmones_file:
            zmones = pickle.load(zmones_file)
            zmones.append(zmogus)
    else:
        zmones = [zmogus]
    with open(ZMONES_FILE, "wb") as zmones_file:
        pickle.dump(zmones, zmones_file)

    print('---[ Visi zmones ]---')
    for zmogus in zmones:
        print(zmogus)
