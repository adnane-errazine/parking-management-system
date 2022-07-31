
def statistique(conn):
 import datetime
 f=1
 while f==1:

    print("\n********** STATISTIQUE **********\n")
    print("1 : Statistique Generales") # à faire
    print("2 : Statistique Compte")
    print("3 : Statistique Vehicules")
    print("4 : Statistique Zones")
    print("5 : Statistique Parkings et Places")
    print("6 : Statistique Reservation") # à faire
    print("7 : Statistique Tickets")    # à faire
    print("8 : Statistique Abonnements") # à faire

    print("\n********** STATISTIQUE **********\n")
    print("1 : Statistique Compte")
    print("2 : Statistique Vehicules")
    print("3 : Statistique Zones")
    print("4 : Statistique Parkings et Places")
    print("5 : Statistique Reservation")
    print("6 : Statistique Tickets")
    print("7 : Statistique Abonnements") 


    print("0 : revenir en menu principale")
    choix=input("Séléction : ")
    if choix=='1' :
        print("********** STATISTIQUE Compte **********\n")
        print("1 : Nombres des utilisateurs")
        print("2 : Nombres des abonnées")
        print("3 : Nombres des occasionnels")
        i=input("Séléction : ")
        if i=='1' :
                cur = conn.cursor()
                sql = "SELECT DISTINCT  idUser FROM Abonne UNION SELECT idUser FROM Occasionnel"
                cur.execute(sql)
                raw = cur.fetchone()
                compt=0
                while (raw):
                    id = raw[0]
                    compt+=1
                    raw = cur.fetchone()
                print("nombre total des utilisateur : %i" %compt)
        if i=='2' :
                cur = conn.cursor()
                sql = "SELECT count(idUser) FROM ABONNE"
                cur.execute(sql)
                raw = cur.fetchone()
                id = raw[0]
                print("nombre total des abonnés : %i" %id)
        if i=='3' :
                cur = conn.cursor()
                sql = "SELECT count(idUser) FROM Occasionnel"
                cur.execute(sql)
                raw = cur.fetchone()
                id = raw[0]
                print("nombre total des occasionnels : %i" %id)

    if choix=='2' :
        print("********** STATISTIQUE Vehicules **********\n")
        print("1 : nombre des vehicules dans la base des données")
        print("2 : nombre des vehicules à deux roues")
        print("3 : nombre des vehicules Simple")
        print("4 : nombre des camions")
        print("5 : nombre des vehicules appartenants à des Abonnés")
        print("6 : nombre des vehicules appartenants à des occasionnels")
        i=input("Séléction : ")
        if i=='1' :
                cur = conn.cursor()
                sql = "SELECT count(immatriculation) FROM Vehicule"
                cur.execute(sql)
                raw = cur.fetchone()
                id = raw[0]
                print("nombre total des vehicules : %i" %id)
        if i=='2' :
                cur = conn.cursor()
                sql = "SELECT count(immatriculation) FROM Vehicule WHERE type= 'Deux roues'"
                cur.execute(sql)
                raw = cur.fetchone()
                id = raw[0]
                print("nombre total des vehicules à deux roues : %i" %id) 
        if i=='3' :
                cur = conn.cursor()
                sql = "SELECT count(immatriculation) FROM Vehicule WHERE type= 'Vehicule simple'"
                cur.execute(sql)
                raw = cur.fetchone()
                id = raw[0]
                print("nombre total des vehicules simples : %i" %id) 
        if i=='4' :
                cur = conn.cursor()
                sql = "SELECT count(immatriculation) FROM Vehicule WHERE type= 'Camion'"
                cur.execute(sql)
                raw = cur.fetchone()
                id = raw[0]
                print("nombre total des camions : %i" %id) 
        if i=='5' :
                cur = conn.cursor()
                sql = "SELECT count(immatriculation) FROM Vehicule WHERE idUserAbo IS NULL"
                cur.execute(sql)
                raw = cur.fetchone()
                id = raw[0]
                print("nombre des vehicules appartenants à des Abonnés : %i" %id) 
        if i=='6' :
                cur = conn.cursor()
                sql = "SELECT count(immatriculation) FROM Vehicule WHERE idUserOcca IS NULL"
                cur.execute(sql)
                raw = cur.fetchone()
                id = raw[0]
                print("nombre des vehicules appartenants à des occasionnels : %i" %id)
        if i=='7' :
                cur = conn.cursor()
                sql = "	SELECT iduserocca AS idUser, COUNT(*) AS Quantite_voiture FROM Vehicule WHERE iduserocca IS NOT NULL GROUP BY iduserocca UNION SELECT iduserabo AS idUser, COUNT(*) AS Quantite_voiture FROM Vehicule WHERE iduserabo IS NOT NULL GROUP BY iduserabo"
                cur.execute(sql)
                raw = cur.fetchone()
                while raw :
                    print("id de l'utilisateur : %i \tNombre de voitures : %i\n"%(raw[0],raw[1]))
                    raw = cur.fetchone()

    if choix=='3' :
        print("********** STATISTIQUE Zones **********\n")
        print("1 : Nombre des Zones: \n")
        print("2 : prix moyen de toutes les zones : \n")
        i=input("Séléction : ")
        if i=='1':
                cur = conn.cursor()
                sql = "SELECT count(nomzone) FROM Zone"
                cur.execute(sql)
                raw = cur.fetchone()
                id = raw[0]
                print("nombre des zones : %i" %id)
        if i=='2':
                cur = conn.cursor()
                sql = "SELECT sum(prix)/count(nomzone) FROM Zone"
                cur.execute(sql)
                raw = cur.fetchone()
                id = raw[0]
                print("prix moyen de toutes les zones : %i" %id)
    if choix=='4' :
        print("********** STATISTIQUE Parkings // Places **********\n")
        print("1 : Nombre de place dans tous les parkings : \n")
        print("2 : Nombre des parking : \n")
        print("3 : Visualiser les places disponibles\n")
        print("4 : Visualiser les places par types de vehicule\n")
        print("5 : Visualiser les places par types des places\n")
        i=input("Séléction : ")
        if i=='1':
                cur = conn.cursor()
                sql = "SELECT count(idPlace) FROM Place"
                cur.execute(sql)
                raw = cur.fetchone()
                id = raw[0]
                print("Nombre de place dans tous les parkings : %i" %id)
        if i=='2':
                cur = conn.cursor()
                sql = "SELECT count(adresse) FROM Parking"
                cur.execute(sql)
                raw = cur.fetchone()
                id = raw[0]
                print("Nombre des parking : %i" %id)
        if i=='3':
            print("1 : Places disponibles dans chaque parking\n")
            print("2 : Places disponibles dans l’ensemble des parkings\n")
            print("3 : Places disponibles en plein air dans chaque parking\n")
            print("4 : Places disponibles couvertes dans chaque parking\n")
            print("0 : Sortie du menu\n")
            t=1
            while t==1:
                temp=int(input("veuillez saisir votre choix :"))
                if temp==1:
                    cur = conn.cursor()
                    sql = "SELECT parking ,COUNT(idPlace) FROM Place WHERE libre=true GROUP BY parking ORDER BY COUNT"
                    cur.execute(sql)
                    raw = cur.fetchone()
                    print("Nombre des places disponibles dans chaque parking:\n")
                    while raw:
                        print ("\t%s \t%s"%(raw[0],raw[1]))
                        raw = cur.fetchone()
                elif temp==2 :
                    cur = conn.cursor()
                    sql = "SELECT COUNT(idPlace) AS Dispo FROM Place WHERE libre=true"
                    cur.execute(sql)
                    raw = cur.fetchone()
                    print("Nombre des places disponibles dans l’ensemble des parkings:\n")
                    while raw:
                        print ("\t%s "%(raw[0]))
                        raw = cur.fetchone()
                
                elif temp==3 :
                    cur = conn.cursor()
                    sql = "SELECT parking ,COUNT(idPlace) FROM Place WHERE type_place='Plein air' GROUP BY parking ORDER BY COUNT"
                    cur.execute(sql)
                    raw = cur.fetchone()
                    print("Nombre des places en plein air disponibles dans chaque parking:\n")
                    while raw:
                        print ("\t%s \t%s"%(raw[0],raw[1]))
                        raw = cur.fetchone()
                elif temp==4 :
                    cur = conn.cursor()
                    sql = "SELECT parking ,COUNT(idPlace) FROM Place WHERE type_place='Couvert' GROUP BY parking ORDER BY COUNT"
                    cur.execute(sql)
                    raw = cur.fetchone()
                    print("Nombre des places disponibles couvertes dans chaque parking:\n")
                    while raw:
                        print ("\t%s \t%s"%(raw[0],raw[1]))
                        raw = cur.fetchone()
                elif temp==0:
                    t=0
        if i=='4':
            print("1 : Places pour les véhicules de type deux roues dans chaque parking\n")
            print("2 : Places disponibles pour les véhicules de type deux roues dans chaque parking\n")
            print("3 : Places pour les véhicules simples dans chaque parking\n")
            print("0 : Sortie du menu\n")
            t=0
            while t==1:
                temp=int(input("veuillez saisir votre choix :"))
                if temp==1:

                    cur = conn.cursor()
                    sql = "SELECT parking ,COUNT(idPlace) FROM Place WHERE type_vehicule = 'Deux roues'  GROUP BY parking ORDER BY COUNT"
                    cur.execute(sql)
                    raw = cur.fetchone()
                    print("Nombre des places pour les véhicules de type deux roues dans chaque parking:\n")
                    while raw:
                        print ("\t%s \t%s"%(raw[0],raw[1]))
                        raw = cur.fetchone()
                elif temp==2:
                    cur = conn.cursor()
                    sql = "SELECT parking ,COUNT(idPlace) FROM Place WHERE type_vehicule = 'Deux roues' AND libre=true GROUP BY parking ORDER BY COUNT"
                    cur.execute(sql)
                    raw = cur.fetchone()
                    print("Nombre des places disponibles pour les véhicules de type deux roues dans chaque parking:\n")
                    while raw:
                        print ("\t%s \t%s"%(raw[0],raw[1]))
                        raw = cur.fetchone()
                
                elif temp==3:
                    cur = conn.cursor()
                    sql = "SELECT parking ,COUNT(idPlace) FROM Place WHERE type_vehicule = 'Vehicule simple'  GROUP BY parking ORDER BY COUNT"
                    cur.execute(sql)
                    raw = cur.fetchone()
                    print("Nombre des places pour les véhicules simples dans chaque parking:\n")
                    while raw:
                        print ("\t%s \t%s"%(raw[0],raw[1]))
                        raw = cur.fetchone()
                elif temp==4:
                    cur = conn.cursor()
                    sql = "SELECT parking ,COUNT(idPlace) FROM Place WHERE type_vehicule = 'Vehicule simple' AND libre=true GROUP BY parking ORDER BY COUNT"
                    cur.execute(sql)
                    raw = cur.fetchone()
                    print("Nombre des places disponibles pour les véhicules simples dans chaque parking:\n")
                    while raw:
                        print ("\t%s \t%s"%(raw[0],raw[1]))
                        raw = cur.fetchone()
                elif temp==5:
                    cur = conn.cursor()
                    sql = "SELECT parking ,COUNT(idPlace) FROM Place WHERE type_vehicule = 'Camion'  GROUP BY parking ORDER BY COUNT"
                    cur.execute(sql)
                    raw = cur.fetchone()
                    print("Nombre des places pour les camions dans chaque parking:\n")
                    while raw:
                        print ("\t%s \t%s"%(raw[0],raw[1]))
                        raw = cur.fetchone()
                elif temp==6:
                    cur = conn.cursor()
                    sql = "SELECT parking ,COUNT(idPlace) FROM Place WHERE type_vehicule = 'Camion' AND libre=true GROUP BY parking ORDER BY COUNT"
                    cur.execute(sql)
                    raw = cur.fetchone()
                    print("Nombre des places disponibles pour les camions dans chaque parking:\n")
                    while raw:
                        print ("\t%s \t%s"%(raw[0],raw[1]))
                        raw = cur.fetchone()
                elif temp==0:
                    t=0
        if i=='5':
            print("1 : Places en plein air dans chaque parking\n")
            print("2 : Places couvertes dans chaque parking\n")
            print("0 : Sortie du menu\n")
            t=0
            while t==1:
                temp=int(input("veuillez saisir votre choix :"))
                if temp==1:
                    cur = conn.cursor()
                    sql = "SELECT parking ,COUNT(idPlace) FROM Place WHERE type_place='Plein air' GROUP BY parking ORDER BY COUNT"
                    cur.execute(sql)
                    raw = cur.fetchone()
                    print("Nombre des places en plein air dans chaque parking:\n")
                    while raw:
                        print ("\t%s \t%s"%(raw[0],raw[1]))
                        raw = cur.fetchone()
                elif temp==2:
                    cur = conn.cursor()
                    sql = "SELECT parking ,COUNT(idPlace) FROM Place WHERE type_place='Couvert' GROUP BY parking ORDER BY COUNT"
                    cur.execute(sql)
                    raw = cur.fetchone()
                    print("Nombre des places couvertes dans chaque parking:\n")
                    while raw:
                        print ("\t%s \t%s"%(raw[0],raw[1]))
                        raw = cur.fetchone()
                elif temp==0:
                    t=0
    if choix=='5' :
        print("********** STATISTIQUE Reservation **********\n")
        print("1 : Nombre des reservations total\n")
        print("2 : Nombre des reservations active\n")
        print("3 : Methode de paiement la plus répandue\n")
        print("4 : Methode de paiement la moins répandue\n")
        print("5 : Nombre de reservations dans une année de votre choix\n")
        i=input("Séléction : ")
        if i=='1':
            cur = conn.cursor()
            sql = "SELECT count(idtransaction) FROM Reservation"
            cur.execute(sql)
            raw = cur.fetchone()
            id = raw[0]
            print("Nombre des reservations total : %i" %id)
        if i=='2':
            cur = conn.cursor()
            date=datetime.date.today()
            sql = "SELECT count(idtransaction) FROM Reservation WHERE date_expiration <= '%s'"%date
            raw = cur.fetchone()
            id = raw[0]
            print("Nombre des reservations active : %i" %id)
        if i=='3':
            cur = conn.cursor()
            sql = "SELECT methodepayment,COUNT(idtransaction) as max FROM Reservation group by methodepayment ORDER BY max DESC"
            cur.execute(sql)
            raw = cur.fetchone()
            print("Methode de paiement la plus répandue est %s , Nombre = %i" %(raw[0],raw[1]))
        if i=='4':
            cur = conn.cursor()
            sql = "SELECT methodepayment,COUNT(idtransaction) as max FROM Reservation group by methodepayment ORDER BY max ASC"
            cur.execute(sql)
            raw = cur.fetchone()
            print("Methode de paiement la moins répandue est %s , Nombre = %i" %(raw[0],raw[1]))
        if i=='5':
            cur = conn.cursor()
            annee=int(input("veuillez saisir une année : \n"))
            sql = "SELECT count(idtransaction) FROM Reservation WHERE EXTRACT(YEAR FROM date_expiration)=%i"%annee
            raw = cur.fetchone()
            id = raw[0]
            print("Nombre de reservations de l'année %i : %i" %(annee,id))
        
    if choix=='6' :
        print("********** STATISTIQUE Tickets **********\n")
        print("1: Nombre de tickets vendu.\n")
        print("2 : Methode de paiement la plus répandue\n")
        print("3 : Methode de paiement la moins répandue\n")
        print("4 : Nombre de tickets vendu dans une année de votre choix\n")
        i=input("Séléction : ")
        if i=='1':
            cur = conn.cursor()
            sql = "SELECT count(idtransaction) FROM Ticket"
            cur.execute(sql)
            raw = cur.fetchone()
            id = raw[0]
            print("Nombre de tickets vendu total : %i" %id)
        if i=='2':
            cur = conn.cursor()
            sql = "SELECT methodepayment,COUNT(idtransaction) as max FROM Ticket  group by methodepayment ORDER BY max DESC"
            cur.execute(sql)
            raw = cur.fetchone()
            print("Methode de paiement la plus répandue est %s , Nombre = %i" %(raw[0],raw[1]))
        if i=='3':
            cur = conn.cursor()
            sql = "SELECT methodepayment,COUNT(idtransaction) as max FROM Ticket  group by methodepayment ORDER BY max ASC"
            cur.execute(sql)
            raw = cur.fetchone()
            print("Methode de paiement la moins répandue est %s , Nombre = %i" %(raw[0],raw[1]))
        if i=='4':
            cur = conn.cursor()
            annee=int(input("veuillez saisir une année : \n"))
            sql = "SELECT count(idtransaction) FROM Ticket WHERE EXTRACT(YEAR FROM date_transaction)=%i"%annee
            raw = cur.fetchone()
            id = raw[0]
            print("Nombre de tickets vendu durant l'année %i : %i" %(annee,id))
    if choix=='7' :
        print("********** STATISTIQUE Abonnements **********\n")
        print("1 : Nombre d'abonnement total\n")
        print("2 : Nombre d'abonnement actif\n")
        print("3 : Methode de paiement la plus répandue\n")
        print("4 : Methode de paiement la moins répandue\n")
        print("5 : Nombre d'abonnement dans une année de votre choix\n")
        i=input("Séléction : ")
        if i=='1':
            cur = conn.cursor()
            sql = "SELECT count(idtransaction) FROM Abonnement"
            cur.execute(sql)
            raw = cur.fetchone()
            id = raw[0]
            print("Nombre d'abonnements total : %i" %id)
        if i=='2':
            cur = conn.cursor()
            date=datetime.date.today()
            sql = "SELECT count(idtransaction) FROM Abonnement WHERE date_fin  <= '%s'"%date
            raw = cur.fetchone()
            id = raw[0]
            print("Nombre d'abonnements actifs : %i" %id)
        if i=='3':
            cur = conn.cursor()
            sql = "SELECT methodepayment,COUNT(idtransaction) as max FROM Abonnement  group by methodepayment ORDER BY max DESC"
            cur.execute(sql)
            raw = cur.fetchone()
            print("Methode de paiement la plus répandue est %s , Nombre = %i" %(raw[0],raw[1]))
        if i=='4':
            cur = conn.cursor()
            sql = "SELECT methodepayment,COUNT(idtransaction) as max FROM Abonnement  group by methodepayment ORDER BY max ASC"
            cur.execute(sql)
            raw = cur.fetchone()
            print("Methode de paiement la moins répandue est %s , Nombre = %i" %(raw[0],raw[1]))
        if i=='5':
            cur = conn.cursor()
            annee=int(input("veuillez saisir une année : \n"))
            sql = "SELECT count(idtransaction) FROM Abonnement WHERE EXTRACT(YEAR FROM date_fin)=%i"%annee
            raw = cur.fetchone()
            id = raw[0]
            print("Nombre d'abonnement de l'année %i : %i" %(annee,id))
    if choix=='0':
        f=0
