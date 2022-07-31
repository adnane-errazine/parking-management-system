from datetime import datetime
import psycopg2
import prix_zone

def reservationAbonnement(conn,mail): # Demander le type de place que souhaite l'utilisateur
    cur=conn.cursor()
    prix_zone.afficherTousParking(conn)
    adressePark= input("Parking pour l'abonnement de la place: ")
    typePlace= {1: 'Plein air', 2:'Couvert'}
    i=0
    while (i <1 or i>2):
        i = int(input("Type de place à ajouter: 1/Plein air | 2/Couvert: "))

    try:#Affichage des vehicules de l'utilisateurs:
        sql="SELECT * FROM Vehicule, Abonne WHERE mail='%s' and Vehicule.idUserAbo=Abonne.iduser"%mail
        cur.execute(sql)
        raw = cur.fetchone()
        while (raw):
            immat=raw[0]
            idAbo=raw[1]
            idOca=raw[2]
            type=raw[4]
            print("immatriculation : %s \t idAbo : %i \t Type : %s \n")%(immat,idAbo,type)
            raw=cur.fetchone()

    except psycopg2.IntegrityError as e:
        conn.rollback()
        print("Message système :", e)
    
    immat = input("Immatriculation du véhicule")
    cur=conn.cursor()
    sql2 = "SELECT type FROM Vehicule V INNER JOIN Abonne A ON V.idUserAbo=A.iduser WHERE A.iduser ='%s' AND V.immatriculation = '%s'"%(mail,immat) # Selection du type d u vehciule pour verifier la disponibilité de la place 
    cur.execute(sql2)
    raw = cur.fetchone()
    typeVehicule =  raw[0]
    
    cur=conn.cursor()
    sql3 = "SELECT COUNT(idPlace) FROM Place WHERE type_vehicule = '%s' AND libre=True AND type_place = '%s' AND parking = '%s' "%(typeVehicule, typePlace[i], adressePark)
    cur.execute(sql3)
    raw = cur.fetchone()
    nbPlacesDispo = raw[0]
    print("Nombre de places disponible pour le type:%s  dans le parking %s: %i"(typeVehicule, adressePark, nbPlacesDispo))

    cur=conn.cursor()
    sql4 = "SELECT idPlace FROM Place WHERE type_vehicule = '%s' AND libre=True AND type_place = '%s' AND parking = '%s' "%(typeVehicule, adressePark)
    cur.execute(sql4)
    raw = cur.fetchone()
    idplace = raw[0]

    if nbPlacesDispo != 0:
        date_transaction=datetime.now()
        date_debut=input("Date debut : ")
        date_fin=input("Date fin : ")
        methodepay=input("Methode de paiement : ")

        # AFFICHAGE DES ABONNEMENTS AFIN DE CHOISIR LE BON ID
        cur=conn.cursor()
        try:
            sql5="SELECT * FROM Reservation"
            cur.execute(sql5)
        except psycopg2.IntegrityError as e:
            conn.rollback()
            print("Message système :", e)
        raw = cur.fetchone()
        while (raw):
            id=raw[0]
            methode2=raw[1]
            dateTransaction=raw[2]
            dateDebut=raw[3]
            dateFin=raw[4]
            mail2=raw[5]
            place=int(raw[6])
            vehicule=raw[7]
            print("id : %i\t methode de paiement : '%s'\tdate_transaction : %s\tdate_debut : %s \tdate_fin : %s\tmail: %s\t place:%i\tVehicule : %s\n"%(id,methode2,dateTransaction,dateDebut,dateFin,mail2,place,vehicule))
            raw=cur.fetchone()

        idtransac = int(input("Id transaction:"))
        # Verification de la contrainte d'héritage
        sql6="SELECT idtransaction FROM Reservation INTERSECT SELECT idtransaction FROM Ticket INTERSECT SELECT idtransaction FROM Abonnement"
        #CREATE VIEW ContrainteFilleSERIEUX AS SELECT idtransaction FROM Reservation INTERSECT SELECT idtransaction FROM Ticket INTERSECT SELECT idtransaction FROM Abonnement
        cur = conn.cursor()
        cur.execute(sql6)
        res = cur.fetchall()
        if(res==None):
            try:
                cur=conn.cursor()
                sql7 = "INSERT INTO Abonnement VALUES(%i, '%s','%s', '%s', '%s', '%s', %i)"%(idtransac, methodepay, date_transaction, date_debut, date_fin, mail, immat, idplace)
                cur.execute(sql7)
                conn.commit()
                print("L'abonnement %i a été crée avec succès à la date %s dans le parking %s. La place accordé à votre véhicule est %i. "%(idtransac, date_transaction, adressePark, idplace))

            except psycopg2.IntegrityError as e:
                conn.rollback()
                print("Message système :", e)







def reservationOccas(conn,mail):
    cur=conn.cursor()
    afficherTousParking(conn)
    adressePark= input("Parking pour l'abonnement de la place")
    try: #Affichage des vehicules de l'utilisateurs:
        sql="SELECT * FROM Vehicule, Abonne WHERE mail='%s' and Vehicule.idUserAbo=Abonne.iduser"%mail
        cur.execute(sql)
        while (raw):
            immat=row[0]
            idAbo=row[1]
            idOca=row[2]
            type=row[4]
            print("immatriculation : %s \t idAbo : %i \t Type : %s \n")%(immat,idAbo,type)
            raw=cur.fetchone()
            
    except psycopg2.IntegrityError as e:
        conn.rollback()
        print("Message système :", e)

    
    immat = input("Immatriculation du véhicule")
    

