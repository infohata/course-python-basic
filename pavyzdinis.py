from datetime import datetime

def ar_pirminis(skaicius):
    if skaicius < 2:
        return False
    for i in range(2, skaicius):
        if skaicius % i == 0:
            return False
    return True

def pirminiai_iki_n(iki=9223372036854775806, nuo=3):
    for skaicius in range(nuo, iki+1):
        if ar_pirminis(skaicius):
            yield skaicius

pirminiai = pirminiai_iki_n(nuo=100000000)
laikas = datetime.now()

def trukme(nuo = laikas):
    return datetime.now() - nuo

while True:
    print(f"{trukme()} - {next(pirminiai)} - {trukme()}")
