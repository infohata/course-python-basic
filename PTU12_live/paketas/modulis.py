def labas(vardas):
    return f"Labas {vardas}"

def sudetis(*args):
    suma = 0
    for arg in args:
        suma += arg
    return suma

class Gyvunas():
    def __init__(self, vardas="") -> None:
        self.vardas = vardas

    def eiti(self):
        print("einu")

vienas = 1
du_p_du = sudetis(2, 2)
vienas = 11
