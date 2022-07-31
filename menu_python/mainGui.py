
import psycopg2
import prix_zone
"""
host = 'tuxa.sme.utc'
user = 'nf18p027'
password = 'ZvD2ubS3'
dbname = 'dbnf18p027'
"""

conn = psycopg2.connect("dbname ='nf18dbp22' user = 'guiutc' password = 'nf18p027'")
cur=conn.cursor()

i=-1
while i!='0':
    print("********** MENU GESTION DE PARKING ***********")
    print("1 : Gérer les clients\n")
    print("2 : Gérer les réservations\n")
    print("3 : Gestion des prix et des zone\n")
    print("4 : Voir les parking et places\n")
    print("5 : Statistiques\n")
    print("0 : Sortie du menu\n")
    i=input("Séléction : ")
    if i=='1':
        """
        print("********** MENU GESTION DES CLIENTS **********\n")
        print("1 : Ajouter un un abonnée\n")
        print("2 : Ajouter un occasionnel\n")
        print("3 : Ajouter un vehicule à un abonné\n")
        print("4 : Ajouter un vehicule à un occasionnel\n")
        temp=int(input("veuillez saisir votre choix :"))
        if temp=='1':
            #addAbo(conn)
        elif temp=='2':
            #addOcca(conn)
        elif temp=='3':
            #addVehiculAbo(conn)
        elif temp=='4':
            #addVehiculOcca(conn)
    """
    elif i=='2':
        print("Réservations :")
    elif i=='3':
        print("Prix par zone :")
        prix_zone.prix_zone(conn)
    elif i=='4':
        print("Parking et places :")
    elif i=='5':
        print("Statistiques :")
        print("********** Statistiques ******our v****\n")
        print("1 : Le nombre des utilisateurs\n")
        print("2 : Afficher le nombre de places disponibles dans chaque parking\n")
        print("3 : Afficher les détails de l'abonnement de chaque personne\n")
        print("4 : Requete pour afficher le nombre d’abonnement par parking\n")
        print("5 : Requete pour afficher le nombre de tickets par parking\n")
        temp=int(input("veuillez saisir votre choix :"))
        if temp=='1':
            nbUtilisateurStat(conn)
        elif temp=='2':
            nbPlaceDispoStat(conn)
        elif temp=='3':
            detailAboStat(conn)
        elif temp=='4':
            nbAboParParking(conn)
        elif temp=='5':
            nbAboParParking(conn)

    elif i=='0':
        exit()
        conn.close()
    else:
       raise ValueError

