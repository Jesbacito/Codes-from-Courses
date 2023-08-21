def laske_nelion_ala(sivun_pituus):
    pinta_ala = sivun_pituus ** 2
    return round(pinta_ala, 4)

sivun_pittuus = float(input("Anna neliön sivun pituus: "))
print("Neliön pinta-ala: ", laske_nelion_ala(sivun_pittuus))
