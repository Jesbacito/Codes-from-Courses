import math

def muunna_xy_koordinaateiksi(kulma, vektorin_pituus):
    x_1 = vektorin_pituus * math.cos(kulma)
    y_1 = vektorin_pituus * math.sin(kulma)
    x = round(x_1)
    y = round(y_1)
    return x, y      

kuluma = float(input("Anna kulma radiaaneina: "))
vektorin_pittuus = float(input("Anna vektorin pituus: "))
print("koordinaatit: ", muunna_xy_koordinaateiksi(kuluma, vektorin_pittuus))
