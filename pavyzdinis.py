print("Sveiki atvykę į interaktyvų skaičiuotuvą!")
print("Pasirinkite veiksmą, kuriuo norite atlikti su dviem skaičiais:")
print("1 - Sudėtis")
print("2 - Atimtis")
print("3 - Daugyba")
print("4 - Dalyba")

choice = input("Įveskite savo pasirinkimą (1-4): ")
num1 = float(input("Įveskite pirmąjį skaičių: "))
num2 = float(input("Įveskite antrąjį skaičių: "))

if choice == '1':
    result = num1 + num2
    print("Rezultatas: ", result)
elif choice == '2':
    result = num1 - num2
    print("Rezultatas: ", result)
elif choice == '3':
    result = num1 * num2
    print("Rezultatas: ", result)
elif choice == '4':
    result = num1 / num2
    print("Rezultatas: ", result)
else:
    print("Netinkamas pasirinkimas")
