def aanesta(sanakirja):
    print("Anna äänesi, vaihtoehdot ovat:")
    vaihtoehdot = ", ".join(sanakirja.keys())
    print(vaihtoehdot)
    
    syote = input("> ").lower()
    if syote in sanakirja:
        sanakirja[syote] += 1
    else:
        sanakirja["virhe"] += 1

def nayta_tulokset(sanakirja):
    for vaihtoehto, aanet in sanakirja.items():
        palkki = "#" * aanet
        print(f"{vaihtoehto.capitalize():<5}: {palkki}")

verouudistus = {
    "jaa": 0,
    "ei": 0,
    "eos": 0,
    "virhe": 0
}
nalle_puh_presidentiksi = {
    "jaa": 12,
    "ei": 0,
    "eos": 5,
    "virhe": 4
}

print("Suoritetaanko verouudistus?")
aanesta(verouudistus)
nayta_tulokset(verouudistus)

print("\nNalle Puh presidentiksi?")
aanesta(nalle_puh_presidentiksi)
nayta_tulokset(nalle_puh_presidentiksi)
