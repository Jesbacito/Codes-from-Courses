def laske_nopeus(matka, aika):
    try:
        nopeus = round((matka / 1000) / (aika / 3600), 2)
        return nopeus
    
    except ValueError:
        print('Vähemmän donitseja, enemmän puhtaita numeroita.')

try:
    matka = float(input('Anna auton kulkema matka metreinä: '))
    aika = float(input('Anna auton käyttämä aika sekunteina: '))
    
    nopeus = laske_nopeus(matka, aika)
    print(f"{matka:.2f} metriä {aika:.2f} sekunnissa "
          f"kulkeneen auton nopeus on {nopeus:.2f} km/h.")
    
except ValueError:
    print('Vähemmän donitseja, enemmän puhtaita numeroita.')
    