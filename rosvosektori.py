from math import pi

def laske_sektorin_ala(sade, sisakulma):
    sektorin_ala = sisakulma / 360 * pi * sade ** 2
    return round(sektorin_ala, 4) 

sade_1 = float(input("Anna ympyrän säde: "))
sisakulma_1 = float(input("Anna sektorin sisäkulma asteina: "))
print("Sektorin pinta-ala: ", laske_sektorin_ala(sade_1, sisakulma_1))
