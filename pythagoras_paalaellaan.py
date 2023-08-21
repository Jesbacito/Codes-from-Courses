def laske_sivun_pituus(hypotenuusa):
    kyljen_pituus = ((hypotenuusa ** 2) / 2) ** (1 / 2)
    return round(kyljen_pituus, 4)

hypotenuusan_pituus = float(input("Anna tasakylkisen hypotenuusan pituus: "))
print("Kylkien pituus: ", laske_sivun_pituus(hypotenuusan_pituus))
