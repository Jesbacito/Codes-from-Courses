from math import pi

def laske_nelio_ala(x):
    pinta_ala = float(x) ** 2
    return pinta_ala

def laske_sektorin_ala(kyljen_pituus):
    sektorin_ala = 45 / 360 * pi * float(kyljen_pituus) ** 2
    return sektorin_ala

def laske_sivun_pituus(x):
    kyljen_pituus = ((float(x) ** 2) / 2) ** (1 / 2)
    return kyljen_pituus

def laske_kolmion_pinta_ala(kyljen_pituus, x):
    kolmion_korkeus = ((kyljen_pituus ** 2) / 2) ** (1 / 2)
    kolmion_pinta_ala = kolmion_korkeus * float(x) / 2
    return kolmion_pinta_ala

def laske_kuvion_ala(x):
    pieni_nelio = laske_nelio_ala(x)
    kyljen_pituus = laske_sivun_pituus(x)
    pieni_sektori = laske_sektorin_ala(kyljen_pituus)
    pieni_kolmio =  laske_kolmion_pinta_ala(kyljen_pituus, x)
    suuri_nelio = (laske_sivun_pituus(x) *2) ** 2
    suuri_sektori = 270 / 360 * pi * (2 * float(kyljen_pituus)) **2
    kuvion_ala = pieni_nelio + pieni_sektori + pieni_kolmio + suuri_nelio + suuri_sektori
    return round(kuvion_ala, 4)

x1 = input("Anna x: ")
print(laske_kuvion_ala(x1))
