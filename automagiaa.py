def pyyda_syote(pyynto, virheviesti):
    while True:
        syote = input(pyynto)
        try:
            kokonaisluku = int(syote)
            return kokonaisluku
        except ValueError:
            print(virheviesti)

luku = pyyda_syote(
    "Anna kokonaisluku: ",
    "Et antanut kokonaislukua"
)
print(f"Annoit kokonaisluvun {luku}! Nohevaa toimintaa!")
hemulit = pyyda_syote(
    "Montako hemulia mahtuu muumitaloon? ",
    "Tämä ei ollut kelvollinen hemulien lukumäärä!"
)
print(f"Muumitaloon mahtuu {hemulit} hemulia")
