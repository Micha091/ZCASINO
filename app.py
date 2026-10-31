# -*-coding:Latin-1 -*
import os
import modules

montant = 100
print("Vous statez a 100 E")

while montant >= 1:
    choix = modules.choix()
    if choix == "Au revoir !!!":
        print(choix)
        break
    else:
        mise = modules.mise(montant)
        nbr = modules.nbr()
        cou1, cou2 = modules.couleur(choix, nbr)
        print("Vous avez choisi:",choix)
        print("Vous avez mise:",mise)
        print("Votre couleur est:",cou1)
        print("Le nombre tire est:",nbr)
        print("La couleur obtenue est:",cou2)
        if choix == nbr:
            montant = montant + (mise * 10)
            print("Vous avez gagne:",mise * 10,"E")
            print("Votre nouveau montant est:",montant)
        elif cou1 == cou2:
            montant = montant - (mise * 0.5)
            print("Vous avez perdu:",mise * 0.5, "E")
            print("Votre nouveau montant est:", montant)
        else:
            montant = montant - mise
            print("Vous avez perdu:",mise, "E")
            print("Votre nouveau montant est:", montant)




if montant < 1:
    print("Vous n'avez plus d'argent, vous avez perdu !!!")
else:
    print("Vous avez quitter le jeu")
    print("Il vous reste",montant,"E")

    os.system("pause")