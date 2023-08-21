import aasimaaritelmat

def nayta_tila(tila):
    valinnat = aasimaaritelmat.VALINNAT if not tila['ELÄKE'] else aasimaaritelmat.ELAKEVALINNAT
    valinnat_str = ', '.join(valinnat)
    
    print(f"Aasi on {tila['IKÄ']} vuotta vanha ja rahaa on {tila['RAHA']} mk.")
    print(f"Kylläisyys: {tila['KYLLÄISYYS']}")
    print(f"Onnellisuus: {tila['ONNELLISUUS']}")
    print(f"Jaksaminen: {tila['JAKSAMINEN']}")
    
    if tila['ELÄKE']:
        print("Aasi on jäänyt eläkkeelle.")
    print("Valinnat:", valinnat_str)

def pyyda_syote(tila):
    if not tila['ELÄKE']:
        valinnat = aasimaaritelmat.VALINNAT
    else:
        valinnat = aasimaaritelmat.ELAKEVALINNAT
    
    while True:
        valinnat_str = ', '.join(valinnat)
        valinta = input(f"Anna seuraava valinta ({valinnat_str}): ")
        
        if valinta in valinnat:
            return valinta
        else:
            print("Virheellinen syöte!")
            