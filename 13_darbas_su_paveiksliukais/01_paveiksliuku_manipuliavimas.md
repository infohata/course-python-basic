# Pillow biblioteka

Pillow yra populiari Python biblioteka, leidžianti atlikti įvairias paveikslėlių manipuliacijas. Ji nėra instaliuota pagal nutylėjimą, todėl mes ją turime susiinstaliuoti. Terminale įvykdome komandą:

```bash
pip install pillow
```

<!-- TODO: flow -->
<!-- Pademonstruojam kaip atsidaro img -->
<!-- Pabandom image.show() -->
<!-- Pabandom resized img uzseivint -->

## Paveikslėlio dydžio keitimas (Resize)

```Python
from PIL import Image

image = Image.open("paveiksliukas.jpg")
width, height = (400, 300)
new_size = (width, height) # vietoje "width" ir "height" įrašykite norimus parametrus, pvz.: (60, 80)
resized_image = image.resize(new_size)
resized_image.save("paveiksliukas_resized.jpg")
```

## Paveikslėlio apkarpymas (Crop)

Atkreipkite dėmesį, kad taškų koordinatės skaičiuojamos iš kairės į dešinę X, iš viršaus į apačią Y.

```Python
from PIL import Image

image = Image.open("paveiksliukas.jpg")
crop_area = (top_left_x, top_left_y, bottom_right_x, bottom_right_y) # įrašykite norimus parametrus, pvz.: (100, 100, 300, 200)
cropped_image = image.crop(crop_area)
cropped_image.save("paveiksliukas_cropped.jpg")
```

## Paveikslėlio miniatiūrų kūrimas (Thumbnails)

```Python
image = Image.open("paveiksliukas.jpg")
thumbnail_size = (width, height)
image.thumbnail(thumbnail_size)
image.save("paveiksliukas_thumbnail.jpg")
```

## Išskaidymas pikseliais ir surinkimas atgal

Paveikslėliai kompiuteryje dažniausiai saugomi naudojant RGB spalvų modelį, kuriame kiekviena spalva sudaryta iš trijų pagrindinių spalvų sudedamųjų dalių: raudonos (R), žalios (G) ir mėlynos (B). Šis pavyzdys atskleidžia, kaip galite atskirti šias spalvų sudedamąsias dalis ir sujungti jas atgal į vieną paveikslėlį.

```Python
from PIL import Image

def split_and_merge(image):
    image_r, image_g, image_b = image.split()
    merged_image = Image.merge("RGB", (image_r, image_g, image_b))
    return merged_image

image = Image.open("paveiksliukas.jpg")
merged_image = split_and_merge(image)
merged_image.save("paveiksliukas_merged.jpg")
```

- `image.split()` funkcija išskaido paveikslėlį į tris atskirus kanalus: raudoną (R), žalią (G) ir mėlyną (B). Šie kanalai yra atskiri paveikslėliai, kuriuose saugoma tik vienos spalvos sudedamoji dalis.
- Po išskaidymo, image_r, image_g ir image_b kintamieji saugo atitinkamai raudoną, žalią ir mėlyną spalvų sudedamąsias dalis.
- Tada naudojame Image.merge("RGB", (image_r, image_g, image_b)) funkciją, kuri sujungia raudoną, žalią ir mėlyną spalvų sudedamąsias dalis atgal į vieną paveikslėlį. "RGB" reiškia, kad norime sujungti spalvas pagal RGB modelį.

💡 Galite sukurti spalvų filtrą, pritaikant tam tikrą funkciją prie kiekvieno kanalo pikselių. Šiame pavyzdyje mes sukursime paprastą spalvų filtrą, padidinsime raudonos spalvos intensyvumą, sumažinsime žalios spalvos intensyvumą ir paliksime mėlynos spalvos intensyvumą nepakitę:

```Python
from PIL import Image

def apply_color_filter(image_r, image_g, image_b):
    # Padidiname raudonos spalvos intensyvumą
    image_r = image_r.point(lambda i: i * 1.5)

    # Sumažiname žalios spalvos intensyvumą
    image_g = image_g.point(lambda i: i * 0.5)

    # Paliekame mėlynos spalvos intensyvumą nepakitę
    image_b = image_b.point(lambda i: i)

    return image_r, image_g, image_b

def split_and_merge(image):
    image_r, image_g, image_b = image.split()
    image_r, image_g, image_b = apply_color_filter(image_r, image_g, image_b)
    merged_image = Image.merge("RGB", (image_r, image_g, image_b))
    return merged_image

image = Image.open("paveiksliukas.jpg")
merged_image = split_and_merge(image)
merged_image.save("paveiksliukas_filtered.jpg")
```

Šiame pavyzdyje mes išskaidome paveikslėlį į RGB kanalus, pritaikome spalvų filtrą naudojant apply_color_filter funkciją, tada sujungėme atnaujintus kanalus į vieną paveikslėlį. Dėl šio pakeitimo paveikslėlyje matysite, kad raudona spalva yra ryškesnė, žalia spalva yra šviesesnė, o mėlyna spalva išlieka nepakitusi.

## Filtrai

Pillow turi įvairių integruotų efektų, kuriuos galite pritaikyti prie savo paveikslėlių. Jie yra pasiekiami per ImageFilter klasę. 

```Python
image = Image.open("paveiksliukas.jpg")
blurred_image = image.filter(ImageFilter.BLUR)
blurred_image.save("paveiksliukas_blurred.jpg")
```

```Python
from PIL import Image, ImageFilter

image = Image.open("paveiksliukas.jpg")
contour_image = image.filter(ImageFilter.CONTOUR)
contour_image.save("paveiksliukas_contour.jpg")
```

```Python
from PIL import Image, ImageFilter

image = Image.open("paveiksliukas.jpg")
sharpen_image = image.filter(ImageFilter.SHARPEN)
sharpen_image.save("paveiksliukas_sharpen.jpg")
```

Daugiau informacijos apie įvairius efektus galite rasti [Pillow dokumentacija](https://pillow.readthedocs.io/en/stable/reference/ImageFilter.html).

## Išsaugojimas

```Python
from PIL import Image

# Atidarome paveikslėlį
image = Image.open("paveiksliukas.jpg")

# Atlikite norimas manipuliacijas su paveikslėliu
# ... (manipuliacijų kodas čia)

# Išsaugokite paveikslėlį nurodytu pavadinimu ir formatu
image.save("paveiksliukas_edited.png", "PNG")
```

## Užduotys

1. Paimkite savo portreto nuotrauką, ją apkarpyti ir sumažinti taip, kad liktų graži maža kvadratinė ikonėlė 128x128.
1. Padarykite savo ikėlę juodai baltą
1. Ant savo portreto dešinėje viršuje uždėkite permatomą png logotipą kompanijos, kuri Jums patinka.
