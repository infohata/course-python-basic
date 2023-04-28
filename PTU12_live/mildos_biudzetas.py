import os
class Irasas:
    def __init__(self, suma: float, komentaras: str) -> str:
        """
        Inicializuoja 'Irasas' klasės objektą su nurodytais kintamaisiais.

        :param suma: 'Irasas' objekto suma.
        :type suma: float
        :param komentaras: 'Irasas' objekto komentaras.
        :type komentaras: str
        """
        self.suma = suma
        self.komentaras = komentaras


class Islaidos(Irasas):
    def __init__(self, suma: float, komentaras: str, gavejas: str):
        super().__init__(suma, komentaras)
        self.gavejas = gavejas


class Pajamos(Irasas):
    def __init__(self, suma: float, komentaras: str, siuntejas: str):
        super().__init__(suma, komentaras)
        self.siuntejas = siuntejas


class Biudzetas:
    zurnalas = []

    def ataskaita(self) -> str:
        """
        Atspausdina biudžeto žurnalą.
        """
        print(biudzetas.get_balansas_string())
        for irasas in self.zurnalas:
            if isinstance(irasas, Pajamos):
                print(f'\033[1;32;40m-=Pajamos\033[0m: Suma: {irasas.suma:.2f} €, komentaras: {irasas.komentaras}, siuntėjas: {irasas.siuntejas}')
            elif isinstance(irasas, Islaidos):
                print(f'\033[1;31;40m-=Išlaidos\033[0m: Suma: {irasas.suma:.2f} €, komentaras: {irasas.komentaras}, gavėjas: {irasas.gavejas}')

    def balansas(self):
        """
        Atspausdina balansą.
        """
        pajamos = sum([irasas.suma for irasas in self.zurnalas if isinstance(irasas, Pajamos)])
        islaidos = sum([irasas.suma for irasas in self.zurnalas if isinstance(irasas, Islaidos)])
        print(f'Pajamos: {pajamos}')
        print(f'Išlaidos: {islaidos}')
        if islaidos > pajamos:
            print("Išlaidos viršija pajamas.")
        return pajamos - islaidos
    
    def get_balansas_string(self) -> str:
        """
        Grąžina eilutę, nurodančią dabartinį biudžeto balansą
        Returns a string indicating the current balance of the budget.
        """
        balansas = self.balansas()
        if len(self.zurnalas) == 0:
            return "\033[1;31;40mBiudžeto sąrašas yra tuščias..\033[0m"
        else:
            return f"\033[1;32;40m-=Bendras balansas\033[0m: {balansas:.2f} €."
    
    def ivesti_pajamas(self, irasas):
        self.zurnalas.append(irasas)


biudzetas = Biudzetas()


def ivesti_pajamas(biudzetas: Biudzetas) -> None:
    print("")
    print("Įveskite \033[1;32;40m gautų \033[0m pajamų sumą pvz. 1250.04 ir spauskite 'Enter':")
    suma = float(input("-->>> "))
    print("Įveskite pajamų siuntėją ir spauskite 'Enter':")
    siuntejas = input("-->>> ")
    print("Įveskite komentarą ir spauskite 'Enter':")
    komentaras = input("-->>> ")
    pajamos = Pajamos(suma, komentaras, siuntejas)
    biudzetas.ivesti_pajamas(pajamos)
    print("")
    print(f"Pajamos {suma:.2f} € buvo pridėtos prie biudžeto.")
    print(biudzetas.get_balansas_string())

def ivesti_islaidas(biudzetas: Biudzetas) -> None:
    suma = float(input("Įveskite išlaidų sumą: "))
    gavejas = input("Įveskite išlaidų gavėją: ")
    komentaras = input("Įveskite komentarą: ")
    islaidos = Islaidos(suma, komentaras, gavejas)
    biudzetas.ivesti_pajamas(islaidos)
    print(f"Išlaidos {suma:.2f} € buvo išimta iš biudžeto.")
    print(biudzetas.get_balansas_string())


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print("\n\t\033[1;36;40m-----=== Biudžeto skaičiavimo programa ===-----\033[0m\n")
        print("\t\t\033[1;32;40m--= Pasirinkite veiksmą =--\033[0m\n")
        print("\t\033[1;32;40m1\033[0m. Sukurti pajamų įrašą")
        print("\t\033[1;32;40m2\033[0m. Sukurti išlaidų įrašą")
        print("\t\033[1;32;40m3\033[0m. Ataskaita\n")
    
        print("\t\033[1;31;40m0\033[0m. Uždaryti programą\n")
        meniu = int(input('Įveskite pasirinkimą \033[1;32;40m1\033[0m, \033[1;32;40m2\033[0m, \033[1;32;40m3\033[0m arba \033[1;31;40m0\033[0m ir spauskite "Enter": '))

        if meniu == 1:
            ivesti_pajamas(biudzetas)
        elif meniu == 2:
            ivesti_islaidas(biudzetas)
        elif meniu == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            biudzetas.ataskaita() 
        elif meniu == 0:
            break
        else:
            print("\n\033[1;31;40mNeteisingas pasirinkimas, bandykite dar kartą!\033[0m\n")
