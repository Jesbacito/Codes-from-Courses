def jakolasku(luku_1, luku_2):
    if luku_2 != 0:
        jako = luku_1 / luku_2
        return jako
    else:
        return'Tällä ohjelmalla ei pääse äärettömyyteen'

def kertolasku(luku_1, luku_2):
    kerto = luku_1 * luku_2
    return kerto

def yhteenlasku(luku_1, luku_2):
    yhteen = luku_1 + luku_2
    return yhteen

def vahennyslasku(luku_1, luku_2):
    vahennys = luku_1 - luku_2
    return vahennys

operaatio = input('Valitse operaatio (/, *, +, -): ')

if operaatio in ['/', '*', '+', '-']:
    try:
        luku1 = float(input('Anna luku 1: '))
        luku2 = float(input('Anna luku 2: '))

        if operaatio == '/':
            tulos = jakolasku(luku1, luku2)
        elif operaatio == '*':
            tulos = kertolasku(luku1, luku2)
        elif operaatio == '+':
            tulos = yhteenlasku(luku1, luku2)
        elif operaatio == '-':
            tulos = vahennyslasku(luku1, luku2)
        
        print('Tulos: ', tulos)
    except ValueError:
        print('Ei tämä ole mikään luku')

else: 
    print('Operaatiota ei ole olemassa')
