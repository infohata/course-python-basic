import os
while True:
    os.system('clear')
    print("-------[ Mūsų uber programėlė ]----------")
    print("1: aidas")
    print("0: išeiti")
    pasirinkimas = input("Pasirinkite: ")
    if pasirinkimas == "0":
        break
    if pasirinkimas == "1":
        tekstas = input("Šaukite: ")
        print((tekstas+" ") * 3)
        input("paspauskite ENTER kad tęsti...")
