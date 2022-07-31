import psycopg2
from datetime import datetime

import gererClients
import adminGererReservations2
import admin_gerer_parking
import creationCompte
import verifierCompte
import utilisateurVoirReservations
import prix_zone
import gerer_mon_compte
import gere_vehicules
import UtilisateurReservation
import statistique

#conn=psycopg2.connect("dbname='dbnf18p0XX' user='nf18p0XX' host='tuxa.sme.utc' password='XXXXXXX'")
conn = psycopg2.connect("dbname ='nf18dbp22' user = 'guiutc' password = 'nf18p027'")
cur=conn.cursor()

i=-1
while i!='0':
        print("********** MENU GESTION DE PARKING **********")
        print("1 : Partie ADMIN")
        print("2 : Partie UTILISATEUR")
        print("0 : Quitter")
        i=input("Séléction : ")
        if i=='1':
            #------PARTIE ADMIN-------
            while i!='9':
                print("\n1 : Gérer les zones et parkings")
                print("2 : Gérer les utilisateurs")
                print("3 : Gérer les réservations")
                print("4 : Statistiques")
                print("9 : Revenir à l'accueil")
                i=input("Séléction : ")
                if i=='1':
                    #------PARTIE ADMIN/Zone/Parking------- 
                    print("\n1 : Afficher les zones")
                    print("2 : Ajouter une zone")
                    print("3 : Supprimer une zone")
                    print("4 : Modifier une zone/prix")
                    print("5 : Gérer les parkings de la zone")
                    print("6 : Afficher tous les parkings")
                    print("7 : Afficher toutes les places, tout parkings confondu")
                    print("8 : Afficher tous les véhicules")
                    print("9 : Revenir à l'accueil")
                    i=input("Séléction : ")
                    if i=='1':
                        print("Affichage des zones\n")
                        prix_zone.afficherZone(conn)
                    elif i=='2':
                        print("Creation d'une nouvelle zone \n")
                        prix_zone.creeZone(conn)
                    elif i =='3':
                        print("Supression d'une zone et des parkings associé en cascade")
                        prix_zone.suppressionZone(conn)
                    elif i=='4':
                        print("Modification d'une zone existante\n")
                        prix_zone.modifierZone(conn)
                    elif i=='5':
                        prix_zone.afficherZone(conn)
                        nomZone=input("Nom de la zone : ")
                        print("\n1 : Afficher les parkings de la zone")
                        print("2 : Ajouter un parking")
                        print("3 : Changer le parking de zone")
                        print("4 : Supprimer un parking")
                        print("5 : Ajouter des places dans le parking de la zone") # A FAIRE 
                        print("6 : Supprimer des places dans le parking de la zone")
                        print("9 : Revenir à l'accueil")
                        choix=input("Séléction : ")
                        if choix =='1':
                            print("Afficher les parkings d'une zone %s"%(nomZone))
                            admin_gerer_parking.afficherParking(conn,nomZone)  

                        elif choix =='2':
                            print("Ajouter un parking dans la zone %s"%(nomZone))
                            admin_gerer_parking.ajouterParking(conn,nomZone)
                        elif choix =='3':
                            print("Changer le parking de zone %s"%(nomZone))
                            admin_gerer_parking.modifierParking(conn,nomZone)
                        elif choix =='4':
                            print("Supression d'un parking de la zone %s "%(nomZone))
                            admin_gerer_parking.supressionParking(conn,nomZone)
                        elif choix =='5':
                            print("Ajout de places dans un parking de la zone %s "%(nomZone))
                            admin_gerer_parking.ajoutPlaces(conn,nomZone)
                        elif choix =='6':
                            print("Supression de place d'un parking de la zone %s "%(nomZone))
                            admin_gerer_parking.supressionPlaces(conn,nomZone)

                    elif i=='6':
                        print("Affichage de tous les parkings:")
                        prix_zone.afficherTousParking(conn)
                        
                    elif i=='7':
                        print("Affichage de tous les places, tous parkings confondu:")
                        prix_zone.afficherTousPlaces(conn)

                    elif i=='8':
                        print("Affichage de tous les vehicules:")
                        prix_zone.afficherTousVehicules(conn)

                elif i=='2':
                    #------PARTIE ADMIN/Utilisateurs------- 
                    print("\n1 : Afficher les utilisateurs")
                    print("2 : Ajouter un utilisateur")
                    print("3 : Supprimer un utilisateur")
                    print("9 : Revenir à l'accueil")
                    i=input("Séléction : ")
                    if i=='1':
                        gererClients.see_users(conn)
                    elif i=='2':
                        print("Abonne (1) ou Occasionnel (2) ?")
                        i=int(input("Séléction : "))
                        if i==1:
                            gererClients.addAbo(conn)
                        elif i==2:
                            gererClients.addOcca(conn)
                    elif i=='3':
                        gererClients.delete_user(conn)

                elif i=='3':
                    #------PARTIE ADMIN/Réservations-------
                    print("\n1 : Afficher les réservations")
                    print("2 : Supprimer toutes les réservations")
                    print("3 : Supprimer une réservation lié à un email")
                    print("4 : Ajouter une reservation")
                    print("9 : Revenir à l'accueil")
                    i=input("Séléction : ")
                    adminGererReservations2.gererReservations(conn,i)
                elif i=='4': 
                    statistique.statistique(conn)


        elif i=='2':
                #------PARTIE UTILISATEUR-------
            print("\n1 : Abonné")
            print("2 : Occasionnel")
            print("9 : Revenir à l'accueil")
            i=input("Séléction : ")
            if i=='1':
                    #------PARTIE UTILISATEUR/Abonné-------
                    res=input("Etes-vous déjà abonné ? (o/n)")
                    if res=='n':
                        mail=input("Saisissez votre mail : ")
                        mdp=input("Saisissez votre mdp : ")
                        creationCompte.creationCompteabo(conn,mail,mdp)
                    elif res=='o':
                        verifier=False
                        while (verifier==False):
                            mail=input("Saisissez votre mail : ")
                            mdp=input("Saisissez votre mdp : ")
                            verifier=verifierCompte.verifierCompte(conn,mail,mdp)
                    print("\n1 : Gérer mon compte")
                    print("2 : Gérer mes véhicules")
                    print("3 : Réserver une place")
                    print("4 : Voir mes réservations")
                    print("9: Revenir à l'accueil")
                    i=input("Séléction : ")
                    if i=='1':
                        gerer_mon_compte.gerer_mon_compte(conn,mail,mdp)
                    elif i=='2':
                        gere_vehicules.gerer_vehicules_abo(conn,mail)
                    elif i=='3':
                        print("Reservation d'une place") # NON FINIIIII
                        print("AAAAAAAAAAAAAAAAAAAAAAAA")
                        UtilisateurReservation.reservationAbonnement(conn,mail)

                    elif i=='4':
                        utilisateurVoirReservations.utilisateurVoirReservations(conn,mail)
            elif i=='2':
                    #------PARTIE UTILISATEUR/Occasionnel-------
                    print("\n1 : Réserver une place")
                    print("2 : Gérer mes véhicules")
                    print("3 : Acheter un ticket")
                    print("4 : Voir mes réservations")
                    print("9 : Revenir à l'accueil")
                    i=input("Séléction : ")
                    if i=='1':
                        reponse=input("Disposez-vous d'un compte ? (o/n)")
                        if reponse=='o':
                            verifier=False
                            while (verifier==False):
                                mail=input("Saisissez votre mail : ")
                                mdp=input("Saisissez votre mdp : ")
                                verifier=verifierCompte.verifierCompte(conn,mail,mdp)
                        elif reponse=='n':
                            print("Créez votre compte \n")
                            mail=input("Saisissez votre mail : ")
                            mdp=input("Saisissez votre mdp : ")
                            creationCompte.creationCompteOccas(conn,mail,mdp)
                            UtilisateurReservation.reservationOccas(conn,mail)
                       
                    elif i=='2':
                        gere_vehicules.gerer_vehicules_occa(conn,mail)
                    elif i=='3':
                        print("Achat d'un ticket")
                        UtilisateurReservation.achatTicket(conn,mail)
                    elif i=='4':
                        while (verifier==False):
                            mail=input("Saisissez votre mail : ")
                            mdp=input("Saisissez votre mdp : ")
                            verifier=verifierCompte.verifierCompte(conn,mail,mdp)
                        utilisateurVoirReservations.utilisateurVoirReservations(conn,mail)

conn.close()
