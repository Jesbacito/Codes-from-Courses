def nayta_tulokset(tiedoston_nimi):
    try:
        with open(tiedoston_nimi, 'r') as tiedosto:
            rivit = tiedosto.readlines()
            for rivi in rivit:
                tiedot = rivi.strip().split(',')
                pelaaja1_nimi = tiedot[0]
                pelaaja2_nimi = tiedot[1]
                pelaaja1_pisteet = tiedot[2]
                pelaaja2_pisteet = tiedot[3]
                tulostus = f"{pelaaja1_nimi} {pelaaja1_pisteet} - {pelaaja2_pisteet} {pelaaja2_nimi}"
                print(tulostus)
    except FileNotFoundError:
        print("Tiedostoa ei löytynyt.")
    except Exception as e:
        print(f"Virhe: {e}")

nayta_tulokset("hemulicup.csv")
