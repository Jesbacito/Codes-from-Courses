def muotoile_heksaluvuksi(kokonaisluku, bitti):
    try:
        kokonaisluku = int(kokonaisluku)
        bitti = int(bitti)
        heksa = hex(kokonaisluku)[2:]
        muotoilu2 = max(bitti // 4, len(heksa))
        heksaluku = heksa.zfill(muotoilu2)
        return heksaluku
    except ValueError:
        print('Anna vain kokonaislukuja.')

kokonaisluku1 = input('Anna kokonaisluku: ')
bitti1 = input('Anna bittien lukumäärä: ')
heksaluku1 = muotoile_heksaluvuksi(kokonaisluku1, bitti1)
print(heksaluku1)
