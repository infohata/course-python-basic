class Automobilis:
    def __init__(self, marke, modelis, metai=2023, spalva='pilka', **kwargs):
        self.marke = marke
        self.modelis = modelis
        self.metai = metai
        self.spalva = spalva
        self.max_greitis = 200
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.__greitis = 0

guolis = Automobilis("Volkswagen", "Golf", kuro_tipas="benzinas", variklis="1.6ti")
print(f"{guolis.marke} {guolis.modelis}, {guolis.metai} m. {guolis.spalva}. Variklis: {guolis.variklis} {guolis.kuro_tipas}. Max. {guolis.max_greitis} km/h")
# Volkswagen Golf, 2023 m. pilka. Variklis: 1.6ti benzinas. Max. 200 km/h
astra = Automobilis("Opel", "Astra", kuro_tipas="benzinas", variklis="1.6", max_greitis=160)
print(f"{astra.marke} {astra.modelis}, {astra.metai} m. {astra.spalva}. Variklis: {astra.variklis} {astra.kuro_tipas}. Max. {astra.max_greitis} km/h")
# Opel Astra, 2023 m. pilka. Variklis: 1.6 benzinas. Max. 160 km/h

def informacija(obj):
    print(f"{obj.marke} {obj.modelis}, {obj.metai} m. {obj.spalva}. Variklis: {obj.variklis} {astra.kuro_tipas}. Max. {obj.max_greitis} km/h")    

informacija(guolis)
informacija(astra)
