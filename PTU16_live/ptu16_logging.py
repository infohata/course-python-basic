import logging

logging.basicConfig(
    filename="logging.log", 
    encoding="UTF-8", 
    level=logging.INFO,
    format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
)
logging.info("Programa veikia")

class Asmuo:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde
        logging.info(f"Sukurtas darbuotojas: {self.__str__()}")

    def __str__(self) -> str:
        return f"{self.vardas} {self.pavarde}"

tadas = Asmuo("Jonas", "Jonaitis")
rokas = Asmuo("Petras", "Petraitis")
print(tadas)
print(rokas)
