from turtle import *

def piirra_ympyra(x, y, sade):
    r = sade
    up()
    setx(x)
    sety(y-r)
    down()
    circle(sade)
    
piirra_ympyra(50, 50, 30)
piirra_ympyra(-50, 50, 30)
piirra_ympyra(0, 0, 60)
up()
setx(0)
sety(0)
done()
