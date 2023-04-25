import pickle
import os

with open('PTU12_live/saldytuvas/zveris.pkl', 'rb') as zveries_guolis:
    zveris = pickle.load(zveries_guolis)

# print(zveris.vardas)
zveris.eiti()
print(os.stat('PTU12_live/saldytuvas/zveris.pkl'))
