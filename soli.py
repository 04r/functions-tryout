
# Meer dan 4 jaar praktijkervaring met dieren-dressuur OF meer dan 5 jaar ervaring met jongleren OF meer dan 3 jaar praktijkervaring met acrobatiek
# In bezit van een Diploma MBO-4 ondernemen
# In bezit van een geldig Vrachtwagen rijbewijs
# In bezit van een hoge hoed
# Is man EN heeft Snor breder dan 10 cm OF is vrouw EN draagt rood krulhaar langer dan 20 cm.
# Let op: Je hoeft alleen een man naar zijn snorlengte te vragen en alleen een vrouw naar haar krulhaarlengte.
# Is langer dan 150 cm
# Is zwaarder dan 90 kg
# Heeft Certificaat “Overleven met gevaarlijk personeel”



# naam = input("Wat is jouw naam: ")
# leeftijd = input("Hou oud ben je: ")

# prak = input("Hoeveel jaar praktijkervaring heeft u met dieren-dressuur? ")


diploma = "Heeft u meer dan 4 jaar praktijkervaring met dieren-dressuur OF meer dan 5 jaar ervaring met jongleren OF meer dan 3 jaar praktijkervaring met acrobatiek: "
rijbewijs = "Geldig Vrachtwagen rijbewijs?: "
hogehoed = "In bezit van een hoge hoed?: "
morf = "Bent u een vrouw of een man?"
vrouw = "Heeft u rood krulhaar langer dan 20 cm?: "
man = "Heeft u een Snor breder dan 10 cm?: "
cm = "Is langer dan 150 cm "
gewicht = "Gewicht?: "
certi = "Heeft Certificaat “Overleven met gevaarlijk personeel”?: "

def main():

    step = input("Bent u een man of een vrouw?: ").lower()

    if step == "man":
        x = input(diploma).lower()
        if x == "ja":
            xd = input(rijbewijs).lower()
            if xd == "ja":
                lel = input(hogehoed).lower()
                if lel == "ja":
                    aaa = input(cm).lower()
                    if aaa == "ja":
                        asdsad = input(man).lower()
                        if asdsad == "ja":
                            kilo = input("Bent u zwaarder dan 90 KG? ").lower()
                            if kilo == "nee":
                                print("Sorry, je moet boven de 90 KG zijn.")
                            else:
                                kgk = input(certi).lower()
                                if kgk == "ja":
                                    print("We nemen jou aan!")
                                    exit()
    elif step == "vrouw":
        x = input(diploma).lower()
        if x == "ja":
            xd = input(rijbewijs).lower()
            if xd == "ja":
                lel = input(hogehoed).lower()
                if lel == "ja":
                    aaa = input(cm).lower()
                    if aaa == "ja":
                        asdsad = input(vrouw).lower()
                        if asdsad == "ja":
                            kilo = input("Bent u zwaarder dan 90 KG?").lower()
                            if kilo == "nee":
                                print("Sorry, je moet boven de 90 KG zijn.")
                            else:
                                kgk = input(certi).lower()
                                if kgk == "ja":
                                    print("We nemen jou aan!")
                                    exit()


main()