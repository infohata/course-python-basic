from typing import Any
from sqlalchemy import create_engine, Integer, String, Float, DateTime
from sqlalchemy.orm import sessionmaker, DeclarativeBase, mapped_column
from datetime import datetime

engine = create_engine('sqlite:///projektai.db')
Session = sessionmaker(bind=engine)
session = Session()

class Base(DeclarativeBase):
    pass


class Projektas(Base):
    __tablename__ = "projektas"
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(50), nullable=False)
    price = mapped_column(Float(2), nullable=False)
    created = mapped_column(DateTime, default=datetime.utcnow)

    def __init__(self, **kw: Any):
        # super().__init__(**kw)
        for key, value in kw.items():
            setattr(self, key, value)
    
    def __repr__(self) -> str:
        return f"({self.id}, {self.name}, {self.price}, {self.created})"


def spausdinti(session):
    projektai = session.query(Projektas).all()
    print("-------------------")
    for projektas in projektai:
        print(projektas)
    print("-------------------")
    return projektai


while True:
    pasirinkimas = input("""Pasirinkite veiksmą: 
1 - atvaizduoti projektus
2 - sukurti projektą
3 - pakeisti projektą
4 - ištrinti projektą
0 - išeiti
>:""")

    try:
        pasirinkimas = int(pasirinkimas)
    except:
        pass

    if pasirinkimas == 1:
        spausdinti(session)

    elif pasirinkimas == 2:
        name = input("Įveskite projekto pavadinimą: ")
        price = float(input("Įveskite projekto kainą: "))
        projektas = Projektas(name=name, price=price)
        session.add(projektas)
        session.commit()

    elif pasirinkimas == 3:
        projektai = spausdinti(session)
        try:
            keiciamas_id = int(input("Pasirinkite norimo pakeisti projekto ID: "))
            keiciamas_projektas = session.get(Projektas, keiciamas_id)
        except Exception as e:
            print(f"Klaida: {e}")
        else:
            pakeitimas = int(input("Ką norite pakeisti: 1 - pavadinimą, 2 - kainą: "))
            if pakeitimas == 1:
                keiciamas_projektas.name = input("Įveskite projekto pavadinimą: ")
            if pakeitimas == 2:
                keiciamas_projektas.price = float(input("Įveskite projekto kainą: "))
            session.commit()

    elif pasirinkimas == 4:
        projektai = spausdinti(session)
        trinamas_id = int(input("Pasirinkite norimo ištrinti projekto ID: "))
        try:
            trinamas_projektas = session.get(Projektas, trinamas_id)
            session.delete(trinamas_projektas)
            session.commit()
        except Exception as e:
            print(f"Klaida: {e}")

    elif pasirinkimas == 0:
        print("Ačiū už tvarkingą uždarymą")
        break

    else:
        print("Klaida: Neteisingas pasirinkimas")
