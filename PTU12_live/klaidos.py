try:
    skaicius = float(input("Įveskite skaičių: "))
    rezultatas = 10 / skaicius
except ZeroDivisionError:
    print("Negalima dalyba iš nulio")
except ValueError:
    print("Netinkamas skaičiaus formatas")
except:
    print("Klaida")
else:
    print("Rezultatas yra:", rezultatas)
