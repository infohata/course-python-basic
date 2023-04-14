# Binary žymės

Kai dirbate su failais Python kalboje, galite juos atidaryti tekstiniu arba binariniu režimu. Tekstinis režimas skirtas dirbti su teksto failais, o binarinis režimas skirtas dirbti su dvejetainiais failais, tokie kaip paveikslėliai, garso failai arba bet kokie failai, kurių turinys nėra tekstas.

## `open()` funkcija su "rb" ir "wb" žymėmis

`"rb"` ir `"wb"` yra binarinio režimo žymės, naudojamos atidarant failus naudojant Python `open()` funkciją. `"rb"` reiškia "read binary" (skaityti dvejetainį), o `"wb"` reiškia "write binary" (rašyti dvejetainį).

Pavyzdys:

```Python
# Atidaryti dvejetainį failą skaitymui
with open('input.bin', 'rb') as input_file:
    binary_data = input_file.read()

# Atidaryti dvejetainį failą rašymui
with open('output.bin', 'wb') as output_file:
    output_file.write(binary_data)
```

## Darbas su dvejetainiais objektais (b''):

Dvejetainiai objektai yra naudojami Python programavimo kalboje, kad galėtumėte dirbti su dvejetainiais duomenimis, tokiomis kaip baitų seka. Jie atrodo taip: b'\x00\x01\x02'.

Pavyzdys:

```Python
binary_data = b'\x48\x65\x6c\x6c\x6f\x2c\x20\x57\x6f\x72\x6c\x64\x21'  # "Hello, World!" dvejetainiu formatu
print(binary_data)  # Išveda: b'Hello, World!'
```

## Failo kopijavimo funkcija

Štai paprasta funkcija, kuri kopijuoja dvejetainį failą iš vienos vietos į kitą:

```Python
def copy_image_file(input_file_path, output_file_path):
    with open(input_file_path, 'rb') as input_file:
        binary_data = input_file.read()
    with open(output_file_path, 'wb') as output_file:
        output_file.write(binary_data)
# Kopijuoti paveikslėlio failą naudojant funkciją
copy_image_file('input.png', 'output.png')
```
