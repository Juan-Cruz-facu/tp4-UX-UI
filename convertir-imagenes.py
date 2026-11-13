"""Convierte tus fotos a los formatos que usa la landing (AVIF + WebP + JPG).

Uso:
  1. pip install pillow
  2. Poné tus fotos en una carpeta "originales/" con estos nombres (jpg o png):
       hero, coffee-1..4, dessert-1..4  -> se generan en 3 formatos
       avatar-1..3                      -> se genera solo JPG
  3. python convertir-imagenes.py
Las imágenes se guardan en assets/img/ (pisan los placeholders).
"""
from pathlib import Path
from PIL import Image, ImageOps

SRC, OUT = Path("originales"), Path("assets/img")
OUT.mkdir(parents=True, exist_ok=True)

def find(name):
    for ext in (".jpg", ".jpeg", ".png", ".webp"):
        p = SRC / f"{name}{ext}"
        if p.exists():
            return p

def save3(img, name):
    img = img.convert("RGB")
    img.save(OUT / f"{name}.jpg", quality=80)
    img.save(OUT / f"{name}.webp", quality=75)
    img.save(OUT / f"{name}.avif", quality=55)

jobs = [("hero", (1920, 1000)), ("hero-768", (768, 640))]
jobs += [(f"{k}-{i}", (668, 728)) for k in ("coffee", "dessert") for i in range(1, 5)]
for name, size in jobs:
    src = find("hero" if name.startswith("hero") else name)
    if src:
        save3(ImageOps.fit(Image.open(src), size), name); print("OK", name)
    else:
        print("falta", name)

for i in range(1, 4):
    src = find(f"avatar-{i}")
    if src:
        ImageOps.fit(Image.open(src).convert("RGB"), (112, 112)).save(OUT / f"avatar-{i}.jpg", quality=80); print("OK avatar", i)
