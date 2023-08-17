print("Sveiki atvykę į interaktyvų skaičiuotuvą!")
print("Pasirinkite veiksmą, kuriuo norite atlikti su dviem skaičiais:")
print("1 - Sudėtis")
print("2 - Atimtis")
print("3 - Daugyba")
print("4 - Dalyba")

pasirinkimas = input("Pasirinkite: ")
skaicius1 = float(input("Pirmas skai2ius: "))
skaicius2 = float(input("Antras skai2ius: "))

if pasirinkimas == "1":
    suma = skaicius1 + skaicius2
    print(f"Suma: {suma:10g}")
elif pasirinkimas == "2":
    skirtumas = skaicius1 - skaicius2
    print(f"Skitrumas: {skirtumas:10g}")
elif pasirinkimas == "3":
    sandauga = skaicius1 * skaicius2
    print(f"Sandauga: {sandauga:10g}")
elif pasirinkimas == "4":
    dalmuo = skaicius1 / skaicius2
    print(f"Dalmuo: {dalmuo:10g}")
else:
    print(f"Klaida: {pasirinkimas} n4ra teisingas pasirinkimas")
