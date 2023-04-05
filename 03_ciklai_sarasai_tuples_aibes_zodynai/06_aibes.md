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

## Užduotys

### Pirma užduotis

- Sukurkite aibę su skaičiais.
- Pridėkite skaičių į aibę
- Atspausdinkite papildytą aibę.

### Antra užduotis

- Sukurkite naują aibę su skaičiais.
- Ištrinkite skaičių iš aibės.
- Atspausdinkite pakoreguotą aibę.

### Trečia užduotis

- Sukurkite naują aibę iš abiejų turimų aibių su tais elementais, kurie yra bendri.
- Atspausdinkite naują aibę.

### Ketvirta užduotis

- Sukurkite naują aibę iš pirmoje ir antroje užduotyje sukurtų aibių su tais elementais, kurie yra pirmoje aibėje, bet ne antroje.
- Atspausdinkite naują aibę.

### Penkta užduotis

- Sukurkite naują aibę iš pirmoje ir antroje užduotyje sukurtų aibių su tais elementais, kurie yra unikalūs tik antroje.
- Atspausdinkite naują aibę.

### Bonus užduotis

- Pakelkite penktosios užduoties aibės elementus kvadratu.

## Atsakymai į užduotis

<details><summary>❗Rodyti atsakymus</summary>
<br>
<details>
<summary>Pirma užduotis</summary>
<hr>

```Python
pirma_aibe = {1, 2, 3, 4}
pirma_aibe.add(5)
print(pirma_aibe)
```

Rezultatas:

```Text
{1, 2, 3, 4, 5}
```

</details>
<details>
<summary>Antra užduotis</summary>
<hr>

```Python
antra_aibe = {3, 4, 5, 6, 7, 8}
antra_aibe.discard(7)
print(antra_aibe)
```

Rezultatas:

```Text
{3, 4, 5, 6, 8}
```

</details>
<details>
<summary>Trečia užduotis</summary>
<hr>

```Python
trecia_aibe = pirma_aibe.intersection(antra_aibe)
print(trecia_aibe)
```

Rezultatas:

```Text
{3, 4, 5}
```

</details>
<details>
<summary>Ketvirta užduotis</summary>
<hr>

```Python
ketvirta_aibe = pirma_aibe.difference(antra_aibe)
print(ketvirta_aibe)
```

Rezultatas:

```Text
{1, 2}
```

</details>
<details>
<summary>Penkta užduotis</summary>
<hr>

```Python
penkta_aibe = antra_aibe.difference(pirma_aibe)
print(penkta_aibe)
```

Rezultatas:

```Text
{6, 8}
```

</details>
<details>
<summary>Bonus užduotis</summary>
<hr>

```Python
aibe_kvadratu = {x**2 for x in penkta_aibe}
print('5 užduoties aibės elementai kvadratu:', aibe_kvadratu)
```

Rezultatas:

```Text
5 užduoties aibės elementai kvadratu: {64, 36}
```

</details>
</details>
