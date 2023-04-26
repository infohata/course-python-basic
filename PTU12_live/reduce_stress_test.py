from datetime import datetime
from functools import reduce

def sudetis(a, b):
    return a + b

print("---- reduce")
pradzia = datetime.now()
trys_devynerios = range(1, 10000000)
print(reduce(sudetis, trys_devynerios))
print(datetime.now() - pradzia)

print("---- for ciklas")
pradzia = datetime.now()
suma = 0
for skaicius in trys_devynerios:
    suma += skaicius
print(suma)
print(datetime.now() - pradzia)


