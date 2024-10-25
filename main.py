import random
import time
#import playsound



#Ici on initialise les valeurs
#variable pour le jeu numero 1

nul=0
player = 0
robot = 0
round = 0
jetons_gagne=0
#seule cette  variables sont communes au deux jeux car elle conditionne la participation
porte_feuille = 500
jetons_gagne_totaux=0

#variable pour le jeu numero 2 
nul2=0
player2 = 0
robot2 = 0
round2 = 0
gain=0
gain2=0
jetons_gagne2=0


#affiche un ASCII art
mystring=('''█───█─▄▀▀─█───▄▀▀─▄▀▀▄─█▄─▄█─▄▀▀
█───█─█───█───█───█──█─█▀▄▀█─█──
█───█─█▀▀─█───█───█──█─█─▀─█─█▀▀
█▄█▄█─█───█───█───█──█─█───█─█──
─▀─▀───▀▀──▀▀──▀▀──▀▀──▀───▀──▀▀''')
print(mystring)




#affiche tous les jeux disponible
def Jeux():
  reponse_choisir=int(input(" A quel jeux voulez-vous jouer?\n 1/ Le jeu classique \n 2/ La roue de la fortune"))
#jeu a compléter si temps disponible
  if reponse_choisir== 1:
    print("REGLE:\n\n Chaque victoire vous rapportera 200 jetons et chaque défaite vous enlève 200 jetons. Les matches nul ne vous rapporte rien et ne vous feront rien perdre.")
    time.sleep(2)
    print("Lancement du jeu et bonne chance")
    leJeuClassique(robot,nul,player,porte_feuille,round,jetons_gagne)
  if reponse_choisir==2:
    print("REGLE:\n\n Chaque victoire vous permettra de tourner la roue qui procure des jetons de 200 a 500 aléatoirement. Les défaites vous feront perdre 200 jetons. Les matches nul ne vous rapporteront rien et ne vous feront rien perdre.")
    roue_du_hasard(robot2,nul2,player2,round2,jetons_gagne2,porte_feuille,gain,gain2)



    
#jeu de base
def leJeuClassique(robot,nul,player,porte_feuille,round,jetons_gagne):
  jetons_gagne2=0
  while porte_feuille >0:
      arreter=int(input("Voulez vous jouer ou arreter maintenant: \n 1_ Arreter\n 2_Jouer"))
      if arreter== 1:
        porte_feuille=0
        menu(jetons_gagne,jetons_gagne2,jetons_gagne_totaux)
      if arreter== 2:
        a=input("Tapez p pour pierre , f pour feuille ou c pour ciseaux :")
        b = random.randint(1, 3)
        if a == "p" and b == 1:
            nul =  nul + 1
            round=round+1
            print("Partie :",round)
            print("pierre vs pierre")
            print("Il y a aucun gagnant")
            print("le resultat final : Plapyer = ", player, "nul = ", nul, "robot = ", robot)
        elif a == "p" and b == 3:
            player = player + 1
            round=round+1
            porte_feuille=porte_feuille + 200
            jetons_gagne=jetons_gagne + 200
            print("Partie :",round)
            print("\r\npierre vs ciseaux ")
            print("Vous avez gagné, vous gagnez 200 jetons.")
            #playsound('bruit de piece.mp3')
            print("le resutat final : Player ", player, "nul", nul, "robot ", robot)
        elif a == "p" and b == 2:
            robot = robot + 1
            round=round+1
            porte_feuille=porte_feuille - 200
            jetons_gagne=jetons_gagne-200
            print("\r\nPartie :",round)
            print("pierre vs feuille ")
            print("Vous avez perdu,vous perdez 200 jetons.")
            print("le resutat final : Player ", player, "nul", nul, "robot ", robot)
        if a == "c" and b == 1:
            robot = robot + 1
            round=round+1
            porte_feuille=porte_feuille - 200
            jetons_gagne=jetons_gagne-200
            print("\r\nPartie :",round)
            print("ciseaux vs pierre ")
            print("Vous avez perdu")
            print("le resutat final : Player ", player, "nul", nul, "robot ", robot)
        elif a == "c" and b == 2:
            player = player + 1
            round=round+1
            porte_feuille=porte_feuille - 200
            jetons_gagne=jetons_gagne-200
            print("\r\nPartie :",round)
            print("ciseaux vs feuille")
            print("Vous avez perdu,vous perdez 200 jetons.")
            print("le resutat final : Player ", player, "nul", nul, "robot ", robot)
        elif a == "c" and b == 3:
            nul = nul + 1
            round=round+1
            print("\r\nPartie :",round)
            print("ciseaux vs ciseaux ")
            print("Il y a aucun gagnant")
            print("le resutat final : Player", player, "nul", nul, "robot", robot)
        if a == "f" and b == 1:
            player = player + 1
            round=round+1
            porte_feuille=porte_feuille + 200
            jetons_gagne=jetons_gagne + 200
            print("\r\nPartie :",round)
            print("feuille vs pierre")
            print("Vous avez gagné, vous gagnez 200 jetons.")
            #playsound('bruit de piece.mp3')
            print("le resutat final : Player ", player, "nul", nul, "robot ", robot)
        elif a == "f" and b == 2:
            nul = nul + 1
            round=round+1
            print("\r\nPartie :",round)
            print("feuille vs feuille ")
            print("Il y a aucun gagnant")
            print("le resutat final : Player ", player, "nul", nul, "robot ", robot)
        elif a == "f" and b == 3:
            robot = robot + 1
            round=round+1
            jetons_gagne=jetons_gagne-200
            porte_feuille=porte_feuille - 200
            print("\r\nPartie :",round)
            print("feuille vs ciseaux ")
            print("Vous avez perdu,vous perdez 200 jetons.")
            print("le resutat final : Player ", player, "nul", nul, "robot ", robot)
  if porte_feuille<0:
    print("Vous etes malheureusement en manque de jetons, veuillez quittez le casino merci de votre compréhension ")
    menu(jetons_gagne,jetons_gagne_totaux,jetons_gagne2)





    
#deuxieme jeu
def roue_du_hasard(robot2,nul2,player2,round2,jetons_gagne2,porte_feuille,gain,gain2):
  while porte_feuille >0:
      arreter=int(input("Voulez vous jouer ou arreter maintenant: \n 1_ Arreter\n 2_Jouer"))
      if arreter== 1:
        porte_feuille=0
        menu(jetons_gagne,jetons_gagne2,jetons_gagne_totaux)
      if arreter== 2:
        a=input("Tapez p pour pierre , f pour feuille ou c pour ciseaux :")
        b = random.randint(1, 3)
        if a == "p" and b == 1:
            nul2 =  nul2 + 1
            round2=round2+1
            print("Partie :",round2)
            print("pierre vs pierre")
            print("Il y a aucun gagnant")
            print("le resultat final : Plapyer = ", player2, "nul = ", nul2, "robot = ", robot2)
        elif a == "p" and b == 3:
            player2 = player2 + 1
            round2=round2+1
            gain=random.randint(200, 500)
            porte_feuille=porte_feuille + gain
            jetons_gagne2=jetons_gagne2 + gain
            print("Partie :",round2)
            print("\r\npierre vs ciseaux ")
            print("Vous avez gagné, la roue vous a attribué",gain,"jetons.")
            #playsound('bruit de piece.mp3')
            print("le resutat final : Player ", player2, "nul", nul2, "robot ", robot2)
        elif a == "p" and b == 2:
            robot2 = robot2 + 1
            round2=round2+1
            porte_feuille=porte_feuille - 200
            jetons_gagne2=jetons_gagne2-200
            print("\r\nPartie :",round2)
            print("pierre vs feuille ")
            print("Vous avez perdu,vous perdez 200 jetons.")
            print("le resutat final : Player ", player2, "nul", nul2, "robot ", robot2)
        if a == "c" and b == 1:
            robot2 = robot2 + 1
            round2=round2+1
            porte_feuille=porte_feuille - 200
            jetons_gagne2=jetons_gagne2-200
            print("\r\nPartie :",round2)
            print("ciseaux vs pierre ")
            print("Vous avez perdu,vous perdez 200 jetons.")
            print("le resutat final : Player ", player2, "nul", nul2, "robot ", robot2)
        elif a == "c" and b == 2:
            player2 = player2 + 1
            round2=round2+1
            jetons_gagne2=jetons_gagne2-200
            porte_feuille=porte_feuille - 200
            print("\r\nPartie :",round2)
            print("ciseaux vs feuille")
            print("Vous avez perdu,vous perdez 200 jetons.")
            print("le resutat final : Player ", player2, "nul", nul2, "robot ", robot2)
        elif a == "c" and b == 3:
            nul2 = nul2 + 1
            round2=round2+1
            print("\r\nPartie :",round2)
            print("ciseaux vs ciseaux ")
            print("Il y a aucun gagnant")
            print("le resutat final : Player", player2, "nul", nul2, "robot", robot2)
        if a == "f" and b == 1:
            player2 = player2 + 1
            round2=round2+1
            gain2=random.randint(200,500)
            porte_feuille=porte_feuille + gain2
            jetons_gagne2=jetons_gagne2 + gain2
            print("\r\nPartie :",round2)
            print("feuille vs pierre")
            print("Vous avez gagné, la roue vous a attribué",gain2,"jetons.")
            #playsound('bruit de piece.mp3')
            print("le resutat final : Player ", player2, "nul", nul2, "robot ", robot2)
        elif a == "f" and b == 2:
            nul2 = nul2 + 1
            round2=round2+1
            print("\r\nPartie :",round2)
            print("feuille vs feuille ")
            print("Il y a aucun gagnant.")
            print("le resutat final : Player ", player2, "nul", nul2, "robot ", robot2)
        elif a == "f" and b == 3:
            robot2 = robot2 + 1
            round2=round2+1
            jetons_gagne2=jetons_gagne2-200
            porte_feuille=porte_feuille - 200
            print("\r\nPartie :",round2)
            print("feuille vs ciseaux ")
            print("Vous avez perdu,vous perdez 200 jetons.")
            print("le resutat final : Player ", player2, "nul", nul2, "robot ", robot2)
  if porte_feuille<0:
      print("Vous etes malheureusement en manque de jetons, veuillez quittez le casino merci de votre compréhension ")
      menu(jetons_gagne,jetons_gagne2,jetons_gagne_totaux)
  
  


#premiere condition d'accesibilité
def age():
    nombre_age=int(input("Quel age avez vous?"))
    if nombre_age>=18:
            print("acces autorisé")
            menu(jetons_gagne,jetons_gagne2,jetons_gagne_totaux)
    if nombre_age<=17:
        print("acces refusé")


#ligue pour classer les utilisateurs
def ligue_classement(jetons_gagne_totaux):
        if jetons_gagne_totaux<=100:
            print("vous n'avez obtenue aucune ligue pour votre sesion")
        if  998>=jetons_gagne_totaux>=100:
            print("Vous etes classé en ligue bronze.")
        if  999>=jetons_gagne_totaux>=701:
            print("Vous etes classé en ligue argent.")
        if  1999>=jetons_gagne_totaux>=1000:
            print("Vous etes classé en ligue or.")
        if  jetons_gagne_totaux>=2000:
            print("Vous etes classé en ligue diamant.")




#menu principal
def menu(jetons_gagne,jetons_gagne_totaux,jetons_gagne2):
  reponse_bienvenue=0
  while reponse_bienvenue not in [1,2,3]:
    reponse_bienvenue=int(input("Bienvenue sur le menu de notre casino en ligne.A noter que ce Casino n'utilise que le mecanisme du pierre , feuille, ciseaux ce qui le rend unique en son genre.\n Le casino vous offre 500 jetons pour commencer votre session de jeu.\n Nous vous rappelons que l'acces n'est autorisé qu'à toute personne majeur et non interdite de jeu. Si vous etes mineur veulez fermer ce jeu.\n1_Commencer a jouer \n 2_ Consulter les mentions légales \n 3_Quittez"))
  if reponse_bienvenue== 1:
    for i in range(1,4):
      print("Chargement des données...")
      time.sleep(2)
    print("Chargement réussi, vous pouvez commencer a jouer")
    time.sleep(2)
    Jeux()
  if reponse_bienvenue ==2:
    print("Jeu désigné par l'entreprise LOGUT-YANI BRAHIMI, toute copie ou reproduction et interdite.")
    time.sleep(2)
    menu(jetons_gagne,jetons_gagne_totaux,jetons_gagne2)
  if reponse_bienvenue ==3:
    jetons_gagne_totaux=jetons_gagne_totaux+500
    jetons_gagne_totaux=jetons_gagne2+jetons_gagne
    if jetons_gagne_totaux>0:
      print("Merci de votre visite. Votre solde de jetons est de ",jetons_gagne_totaux,"jetons.")
      ligue_classement(jetons_gagne_totaux)
    if jetons_gagne_totaux <=0:
        print("Attention votre solde de jetons est négatif ,merci de régularisé votre compte ou de faire un pret au casino pour continuer, votre dette s'élève a",jetons_gagne_totaux,"jetons.")
      


age()

# question mise a jour
#gain aleatoire
#variable tirelire 300 jetons
#compteur partie total
#ecriture python fichier
#leaderboard
#art jeton ...
#roue multiplicateur aléatoire
#sortie du jeu si il veut
#login utilisateur
#jeu bingo (bille qui roule)

# question mise a jour 
#gain aleatoire
#variable tirelire 500 jetons
#compteur partie total 
#ecriture python fichier
#leaderboard 
#art jeton ... 
#roue multiplicateur aléatoire
#sortie du jeu si il veut 
#login utilisateur 
#jeu bingo (bille qui roule)
