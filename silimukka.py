def pyyda_syote(pyynto, virheviesti):
    while True:
        syote = input(pyynto)
        try:
            kokonaisluku = int(syote)
            if kokonaisluku > 1:
                return kokonaisluku
            else:
                print(virheviesti)
        except ValueError:
            print(virheviesti)

def tarkista_alkuluku(luku):
    if luku <= 1:
        return False
    for i in range(2, int(luku**0.5) + 1):
        if luku % i == 0:
            return False
    return True

luku = pyyda_syote(
    "Anna kokonaisluku, joka on suurempi kuin 1: ",
    "Pieleen meni :'(."
)

if tarkista_alkuluku(luku):
    print("Kyseessä on alkuluku.")
else:
    print("Kyseessä ei ole alkuluku.")
    