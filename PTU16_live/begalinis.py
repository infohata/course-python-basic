import time

def begalinis():
    skaicius = 0
    while True:
        yield skaicius
        skaicius += 1

# print(f"{10 ** 8:,d}")
# input("ENTER to start:...")
startas = time.time()
trukme = startas
for tarpinis in begalinis():
    # if tarpinis % 1000000 == 0:
    #     trukme = time.time() - startas
    #     print(f"{trukme:10.4f}, {tarpinis // 1000000:20d}")
    if tarpinis > 10 ** 8:
        break
    # trukme = time.time() - startas
    # if trukme > 10:
    #     break
trukme = time.time() - startas
print(tarpinis // 1000000, trukme)
