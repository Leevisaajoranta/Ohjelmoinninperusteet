# Arvaa-luku peli

# Pythonin oma satunnaisuuteen liittyvä funktio
import random

# Tehdään pelin aloitus
def arvaa_luku():
    numero = random.randint(1, 100)
    yritykset = 0
    print("Tervetuloa Arvaa-luku peliin!")
    print("Yritä arvata numero väliltä 1-100.")

# Tehdään silmukka, joka jatkuu kunnes käyttäjä arvaa oikein
    while True:
        try:
            arvaus = int(input("Anna arvaus: "))
            yritykset += 1

            if arvaus > numero:
                print("Liian suuri!")
            elif arvaus < numero:
                print("Liian pieni!")
            else:
                print(f"Oikein! Luku oli {numero}, ja arvasit sen {yritykset} yrityksellä.")
                break

# Virheellisen syötteen viesti
        except ValueError:
            print("Syötäthän vain numeroita!")

# Käynnistää pelin
arvaa_luku()