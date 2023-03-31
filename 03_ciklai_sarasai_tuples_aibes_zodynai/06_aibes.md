# Aibės

Aibės (`sets`) yra kolekcijos tipo objektai, kurie skiriasi nuo sąrašų (`list`) ir `tuple` tuo, kad jos saugo tik unikalius elementus. Tai reiškia, kad, jei į aibę bandome įdėti jau esantį elementą, jis nebus pridėtas į aibę ir nebus atvaizduotas kelis kartus. Sąrašai ir `tuple` gali saugoti kartojančius elementus, taip pat skirtingai nei aibė, jie saugo elementus tvarkos tvarka. Kitas svarbus skirtumas yra tai, kad aibės nenaudoja indeksų, taigi jų elementų tvarka nėra nurodoma.

## Aibių kūrimas

Norint sukurti aibę, galima tiesiog užrašyti elementus tarp skliaustų `{}`, atskirtus kableliais. Pvz.:

```Python
mano_aibe = {'obuolys', 'bananas', 'apelsinas'}
```

Jei norite sukurti tuščią aibę, galite naudoti funkciją `set()`:

```Python
tuscia_aibe = set()
```

## Aibių metodai

Aibės turi daug įvairių metodų, kurie yra naudingi, kai reikia atlikti aibės elementų paiešką, filtravimą, rikiavimą ir kt. Štai keli pagrindiniai aibių metodai su pavyzdžiais:

`add()` - prideda vieną elementą į aibę:

```Python
aibe = {1, 2, 3}

aibe.add(4)
print(aibe) # {1, 2, 3, 4}
```

`update()` - prideda kitą aibę arba sąrašą į aibę:

```Python
aibe = {1, 2, 3}

sarasas = [3, 4, 5]
aibe.update(sarasas)
print(aibe) # {1, 2, 3, 4, 5}
```

❗ Aibėje negalima saugoti elementų, kurie kartojasi (dubliuojasi). Jei bandysite pridėti elementą, kuris jau yra aibėje, jis tiesiog nebus pridėtas ir nieko neįvyks:

`remove()` - pašalina elementą iš aibės. Jeigu elemento nėra aibėje, išmetamas `KeyError` klaidos pranešimas:

```Python
aibe = {1, 2, 3}

aibe.remove(2)
print(aibe) # {1, 3}

aibe.remove(4) # KeyError: 4
```

`discard()` - pašalina elementą iš aibės. Jeigu elemento nėra aibėje, jokio klaidos pranešimo nėra:

```Python
aibe = {1, 2, 3}

aibe.discard(2)
print(aibe) # {1, 3}

aibe.discard(4)
print(aibe) # {1, 3}
```

`pop()` - pašalina ir grąžina bet kurį elementą iš aibės. Jeigu aibė yra tuščia, išmetamas KeyError klaidos pranešimas:

```Python
aibe = {1, 2, 3}

elementas = aibe.pop()
print(aibe) # {2, 3}
print(elementas) # 1
```

`clear()` - pašalina visus elementus iš aibės:

```Python
aibe = {1, 2, 3}
aibe.clear()
print(aibe) # set()
```

`copy()` - grąžina aibės kopiją:

```Python
aibe = {1, 2, 3}
kopija = aibe.copy()
print(kopija) # {1, 2, 3}
```

`union()` - sujungia aibes be pasikantojančių elementų:

```Python
aibe1 = {1, 2, 3}
aibe2 = {3, 4, 5}
aibe3 = aibe1.union(aibe2)
print(aibe3) # {1, 2, 3, 4, 5}
```

`intersection` - grąžina visus elementus, kurie yra abiejose aibėse:

```Python
aibe1 = {1, 2, 3}
aibe2 = {3, 4, 5}
aibe4 = aibe1.intersection(aibe2)
print(aibe4) # {3}
```

`difference()` - grąžina visus elementus, kurie yra pirmoje aibėje, bet nėra antroje aibėje:

```Python
aibe1 = {1, 2, 3}
aibe2 = {3, 4, 5}
aibe5 = aibe1.difference(aibe2)
print(aibe5) # {1, 2}
```

## Sąrašo pavertimas aibe

Jeigu turite sąrašą su pasikartojančiais elementais ir norite sukurti aibę be pasikartojančių elementų, galite naudoti `set()` funkciją. Ši funkcija sukuria aibę iš sąrašo ir automatiškai pašalina pasikartojančius elementus:

```Python
sarasas = [1, 2, 3, 2, 1, 4, 5, 4]
aibe = set(sarasas)
print(aibe) # {1, 2, 3, 4, 5}
```

## Aibių iteravimas

Aibės yra iteruojamos struktūros, kurias galima lengvai peržiūrėti su ciklais arba įvairiais aibių metodais. Pvz.:

```Python
aibe = {1, 2, 3}
for elementas in aibe:
    print(elementas)
```

Rezultatas:

```Text
1
2
3
```

# Užduotys

- Sukurkite dvi aibes su skaičiais.
- Grąžinkite tuos elementus, kurie yra bendri abiejoms aibėms.
- Grąžinkite tuos elementus, kurie yra pirmoje aibėje, bet ne antroje.
- Sukurkite trečią aibę, kurioje yra unikalūs elementai tik iš antrosios aibės.
- Pakelkite trečiosios aibės elementus kvadratu.

## Atsakymai į užduotis

<details><summary>❗Rodyti atsakymus</summary>
<hr>

```Python
aibe1 = {1, 2, 3, 4, 5}
aibe2 = {4, 5, 6, 7, 8}

bendra_aibe = aibe1.intersection(aibe2)
print('Bendra aibė:', bendra_aibe)

unikalios_aibe1 = aibe1.difference(aibe2)
print('Unikalūs aibės 1 elementai:', unikalios_aibe1)

aibe3 = aibe2.difference(aibe1)
print('Nauja aibė su aibės 2 unikaliais elementais:', aibe3)

aibe3_kvadratu = {x**2 for x in aibe3}
print('Aibės 3 elementai kvadratu:', aibe3_kvadratu)
```

Rezultatas:

```Text
Bendra aibė: {4, 5}
Unikalūs aibės 1 elementai: {1, 2, 3}
Nauja aibė su aibės 2 unikaliais elementais: {8, 6, 7}
Aibės 3 elementai kvadratu: {64, 49, 36}
```

</details>