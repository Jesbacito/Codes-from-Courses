import turtle

def piirra_spiraali(vari, kaarien_lkm, alkusade, sadeen_kasvu, viivan_paksuus=1):
    turtle.color(vari)
    turtle.pensize(viivan_paksuus)

    for _ in range(kaarien_lkm):
        turtle.circle(alkusade, 90)
        alkusade += sadeen_kasvu

turtle.speed(0)
piirra_spiraali("black", 20, 10, 3)
piirra_spiraali("red", 10, 20, 4, 3)
piirra_spiraali("blue", 10, -20, -4, 3)
turtle.done()
