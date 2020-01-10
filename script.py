from random import randrange

class Mot(object):
    def __init__(self, romaji=None, fr=None):
        self.romaji = romaji
        self.fr = fr

liste = []
i = 0

liste.append(Mot("hayai", "rapide, tôt"))
liste.append(Mot("osoi", "lent, tardif"))
liste.append(Mot("semai", "étroit"))
liste.append(Mot("benri", "pratique, commode"))
liste.append(Mot("fuben", "incommode"))
liste.append(Mot("norimono", "moyens de transport"))
liste.append(Mot("hikôki", "avion"))
liste.append(Mot("densha", "train"))
liste.append(Mot("michi", "chemin, rue"))

listeNum = list(range(1, len(liste)+1))

while i < len(liste):
    rand = randrange(len(liste))
    if listeNum[rand] != 0:
        i += 1
        mot = liste[rand]
        motPropose = input("Traduction de : " + mot.fr + " ? ")
        if mot.romaji == motPropose:
            print("Oui !")
        else:
            print("Non ! La réponse était : " + mot.romaji)
        print("")
        listeNum[rand] = 0
