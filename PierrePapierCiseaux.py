import random as rd
def PierrePapierCiseaux(nbr_partie):
    score_joueur = 0
    score_ordi = 0
    options = ["pierre", "papier", "ciseaux"]
    while nbr_partie > 0:
        print(f"Your score: {score_joueur} \t  Computer score {score_ordi}")
        choix_joueur = input("Vous jouez quoi:__")
        while choix_joueur  not in options:
             choix_joueur = input("Vous jouez quoi:__")
             choix_joueur.lower()
        choix_ordi = rd.choice(options)

        
        if choix_joueur == choix_ordi:
             print("Meme choix")
        elif choix_joueur == "pierre" and choix_ordi == "ciseaux":
            score_joueur = score_joueur +1
        elif choix_joueur == "papier" and choix_ordi == "pierre":
            score_joueur = score_joueur +1
        elif choix_joueur == "ciseaux" and choix_ordi == "pierre":
            score_joueur = score_joueur +1
        else:
            score_ordi = score_ordi +1

        nbr_partie = nbr_partie -1
    if score_joueur > score_ordi:
        print("Congrats !!!!! You're the Winner")
    elif score_joueur == score_ordi:
        print("Egalite pas de vainqueur")
    else:
        print("Computer is the winner ")
           

PierrePapierCiseaux(3)