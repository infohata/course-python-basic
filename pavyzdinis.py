import random

print('Bus sugeneruoti 3 skaičiai')
print('Jei vienas iš jų – 5, tu pralaimėjai!')

for bandymas in range(3):
    skaicius = random.randint(1, 6)
    print(skaicius)
    if skaicius == 5:
        print('Pralaimėjai...')
        break
else:
    print('Laimėjai!')
