from datetime import date


class AutoMetuKlaida(ValueError):
    pass


class Automobilis:
    def __init__(self, modelis:str, marke:str, metai:int) -> None:
        self.modelis = modelis
        self.marke = marke
        self.metai = metai

    @property
    def metai(self) -> int:
        return self.__metai
    
    @metai.setter
    def metai(self, metai:int):
        if type(metai) != int:
            raise ValueError("metai turi būti skaičius")
        elif not 1886 <= metai <= (date.today().year + 1):
            raise AutoMetuKlaida("auto negali būti toks senas, arba jo dar nėra")
        self.__metai = metai

    def __str__(self) -> str:
        return f"{self.marke} {self.modelis} {self.metai}"


guolis = Automobilis("Volkswagen", "Golf", 1997)
guolis.metai = 2027
print(guolis)
