def kysy_salasana():
    while True:
        salainen_sana = input("Anna salasana vähintään 8 merkkiä pitkä: ")
        if len(salainen_sana) >= 8:
            print("Salasana on tarpeeksi pitkä.")
            return salainen_sana
        else:
            print("Salasana on liian lyhyt. Salasanassa pitää olla vähintään 8 merkkiä pitkä")

salasana = kysy_salasana()
print("Syöttämäsi salasana: ", salasana)
