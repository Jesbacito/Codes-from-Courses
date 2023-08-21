import turtle

def piirra_spiraali(vari, kaarien_lkm, alkusade, sadeen_kasvu, viivan_paksuus=1):
    turtle.color(vari)
    turtle.pensize(viivan_paksuus)

    for _ in range(kaarien_lkm):
        turtle.circle(alkusade, 90)
        alkusade += sadeen_kasvu

def piirra_tiedostosta(tiedoston_nimi):
    with open(tiedoston_nimi, "r") as tiedosto:
        for rivi in tiedosto:
            spiraali_tiedot = rivi.strip().split(",")
            vari = spiraali_tiedot[0]
            kaarien_lkm = int(spiraali_tiedot[1])
            alkusade = int(spiraali_tiedot[2])
            sadeen_kasvu = float(spiraali_tiedot[3])
            viivan_paksuus = int(spiraali_tiedot[4])
            piirra_spiraali(vari, kaarien_lkm, alkusade, sadeen_kasvu, viivan_paksuus)

turtle.speed(0)
piirra_tiedostosta("spiraali.txt")
turtle.done()
