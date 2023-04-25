import os

print(os.getcwd())
if os.path.exists("PTU12_live"):
    os.chdir("PTU12_live")
    print(os.getcwd())
if os.path.exists('saldytuvas.json'):
    print("yra šaldytuvas")
if not os.path.exists("saldytuvas"):
    os.makedirs("saldytuvas")
if os.path.exists("saldytuvas.json"):
    print("moving fridge....")
    with open("saldytuvas.json", "r") as senas:
        with open("saldytuvas/saldytuvas.json", "w") as naujas:
            naujas.write(senas.read())
    print("copied.")
    os.remove("saldytuvas.json")
    print("deleted.")

# print(os.listdir(os.getcwd()))
from pprint import pprint
pprint(os.stat('saldytuvas/saldytuvas.json'))

