def choix():
    """ceci determine le choix"""
    while 1:
        choice = input("Entrer un nombre de 0 a 49 / 'Q' ou 'q' pour quitter")
        if choice == "q" or choice == "Q":
            return("Au revoir !!!")
            break
        else:
            try:
                choix = int(choice)
                assert choix > 0 and choix < 50
            except ValueError:
                print("Entrer un nombre entier")
                continue
            except AssertionError:
                print("Le nombre doit etre compris de 0 a 49")
                continue
            else:
                return choix
                break

def nbr():
    """ceci cree le nombre aleatoire"""
    from random import randrange
    nbr = randrange(50)
    return nbr

def couleur(choix, nbr):
    if choix % 2 == 0:
        couc = "N"
    else:
        couc = "R"
    if nbr % 2 == 0:
        coun = "N"
    else:
        coun = "R"
    return couc, coun

def mise(montant):
    while 1:
        miser = input("Faire votre mise")
        if miser == "Q" or miser == "q":
            return("Au revoir !!!")
            break
        else:
            try:
                mise = int(miser)
                assert mise <= montant
            except ValueError:
                print("Veuillez rentrer un nombre entier")
                continue
            except AssertionError:
                print("Rentrer un nombre qui est soit inferieur soit egal a votre montant actuel")
                continue
            else:
                return mise



