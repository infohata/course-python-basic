import pickle

with open('PTU16_live/saldytuvas.pickle', 'rb') as fridge_file:
    fridge = pickle.load(fridge_file)
    fridge.contents = pickle.load(fridge_file)

fridge.add('salotos', 1)
fridge.list_products()
print(fridge.check('pienas', 2))
