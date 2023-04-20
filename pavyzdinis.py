class Darbuotojas:
    def __init__(self, vardas, pavarde, atlyginimas=1000):
        self.vardas = vardas
        self.pavarde = pavarde
        self.atlyginimas = atlyginimas

    def info(self):
        print(f'---\n{self.vardas} {self.pavarde}, atlyginimas: {self.atlyginimas} €')

class Administratorius(Darbuotojas):
    pass


class Vadovas(Darbuotojas):
    def __init__(self, vardas, pavarde, atlyginimas, premija):
        super().__init__(vardas, pavarde, atlyginimas)
        self.premija = premija

    def info(self):
        super().info()
        print(f'Premija: {self.premija} €')


darbuotojas1 = Darbuotojas('Jonas', 'Jonaitis')
darbuotojas2 = Darbuotojas('Petras', 'Petraitis', 1200)
darbuotojas3 = Administratorius('Juozas', 'Juozaitis', 900)
vadovas1 = Vadovas('Antanas', 'Antanaitis', 1500, 500)

darbuotojai = [darbuotojas1, darbuotojas2, darbuotojas3, vadovas1]

for darbuotojas in darbuotojai:
    darbuotojas.info()
