from datetime import datetime
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float, DateTime

engine = create_engine('sqlite:///PTU16_live/db/projektai.db')
Base = declarative_base()
session = sessionmaker(engine)()


class Projektas(Base):
    __tablename__ = "Porojektas"
    id = Column(Integer, primary_key=True)
    pavadinimas = Column("pavadinimas", String(50))
    kaina = Column("kaina", Float())
    sukurta = Column("sukurta", DateTime, default=datetime.utcnow)

    def __init__(self, pavadinimas, kaina):
        self.pavadinimas = pavadinimas
        self.kaina = kaina

    def __repr__(self):
        return f"({self.id}, {self.pavadinimas}, {self.kaina}, {self.sukurta})"


def select_project(session=session) -> Projektas | None:
    try:
        id = int(input("Pasirinkite projektą: "))
        projektas = session.get(Projektas, id)
    except Exception as error:
        print(error.__class__, error)
    else:
        return projektas

def ieskoti(session=session) -> None:
    pavadinimas = input("Pavadinimas (galimas tuščias): ")
    try:
        kaina_nuo = float(input("Kaina nuo: "))
    except ValueError:
        kaina_nuo = None
    try:
        kaina_iki = float(input("Kaina iki: "))
    except ValueError:
        kaina_iki = None
    uzklausa = session.query(Projektas)
    if len(pavadinimas) > 0:
        uzklausa = uzklausa.filter(Projektas.pavadinimas.ilike(f"%{pavadinimas}%"))
    if type(kaina_nuo) == float:
        uzklausa = uzklausa.filter(Projektas.kaina >= kaina_nuo)
    if type(kaina_iki) == float:
        uzklausa = uzklausa.filter(Projektas.kaina <= kaina_iki)
    rasti = uzklausa.all()
    if len(rasti) > 0:
        for rastas in rasti:
            print(rastas)
    else:
        print("Projektų pagal užklausą nėra")
    input("Spauskite ENTER kad tęsti...:")


try:
    Base.metadata.create_all(engine)
except Exception as error:
    print(error.__class__, error)

meniukas = """ Super duper projektų valdymo programėlė
0 - išeiti
1 - peržiūrėti visus
2 - paieška
3 - naujas projektas
4 - atnaujinti projektą
5 - uždaryi projektą
PASIRINKITE: """

while True:
    pasirinkimas = input(meniukas)
    if pasirinkimas == "0":
        print("Bye!")
        break
    elif pasirinkimas == "1":
        projektai = session.query(Projektas).all()
        for projektas in projektai:
            print(projektas)
    elif pasirinkimas == "2":
        ieskoti()
    elif pasirinkimas == "3":
        pavadinimas = input("Pavadinimas: ")
        try:
            kaina = float(input("Kaina: "))
            naujas = Projektas(pavadinimas, kaina)
        except Exception as error:
            print(error.__class__, error)
        else:
            if len(pavadinimas) > 0:
                session.add(naujas)
                session.commit()
                print("Done!")
    elif pasirinkimas == "4":
        projektas = select_project()
        if projektas:
            pavadinimas = input("Pavadinimas (tuščias kad nekeisti): ")
            if len(pavadinimas):
                projektas.pavadinimas = pavadinimas
            try:
                kaina = float(input("Kaina (tuščia kad nekeisti): "))
            except ValueError:
                pass
            else:
                projektas.kaina = kaina
            session.add(projektas)
            session.commit()
            print("Done!")
    elif pasirinkimas == "5":
        projektas = select_project()
        if projektas:
            session.delete(projektas)
            session.commit()
            print("Done!")
    else:
        print("Klaida: Netinkamas pasirinkimas")
