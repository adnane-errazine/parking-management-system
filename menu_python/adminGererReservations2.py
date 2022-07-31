from datetime import datetime
def gererReservations(conn,i):
    if i=='1':
        cur=conn.cursor()
        try:
            sql="SELECT * FROM Reservation"
            cur.execute(sql)
        except psycopg2.IntegrityError as e:
            conn.rollback()
            print("Message système :", e)
        raw = cur.fetchone()
        while (raw):
            id=raw[0]
            methode=raw[1]
            date_transaction=raw[2]
            date_debut=raw[3]
            date_fin=raw[4]
            mail=raw[5]
            place=int(raw[6])
            vehicule=raw[7]
            print("id : %i\t methode de paiement : %s\tdate_transaction : %s\tdate_debut : %s \tdate_fin : %s\tmail: %s\t place:%i\tVehicule : %s\n"%(id,methode,date_transaction,date_debut,date_fin,mail,place,vehicule))
            raw=cur.fetchone()
    if i=='2':
        cur = conn.cursor()
        try:
            sql="DELETE FROM Reservation"
            cur.execute(sql)
            conn.commit()
        except psycopg2.IntegrityError as e:
            conn.rollback()
            print("Message système :", e)
    if i=='3':
        temp=input("Veuillez saisir l'email associé à la reservation : ")
        cur = conn.cursor()
        try:
            sql="DELETE FROM Reservation WHERE mail='%s' " %temp
            cur.execute(sql)
            conn.commit()
        except psycopg2.IntegrityError as e:
         conn.rollback()
         print("Message système :", e)
    if i=='4':
        id = int(input("id transaction : "))
        methode=input("Methode de paiement : ")
        date_transaction=datetime.now()
        date_debut=input("Date debut : ")
        date_fin=input("Date fin : ")
        mail=input("votre mail : ")
        place=input("la place à réserver : ")
        vehicule=input("matricule de votre vehicule : ")
        sql="SELECT idtransaction FROM Reservation INTERSECT SELECT idtransaction FROM Ticket INTERSECT SELECT idtransaction FROM Abonnement"
        #CREATE VIEW ContrainteFilleSERIEUX AS SELECT idtransaction FROM Reservation INTERSECT SELECT idtransaction FROM Ticket INTERSECT SELECT idtransaction FROM Abonnement
        cur = conn.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        if(res==None):
            try:
             sql="INSERT INTO Reservation VALUES (%i, '%s', '%s', '%s', '%s', '%s', %i, '%s');"%(id,methode, date_transaction, date_debut, date_fin, mail, place, vehicule)
             cur.execute(sql)
             conn.commit()
            except psycopg2.IntegrityError as e:
             conn.rollback()
             print("Message système :", e)
        else :
             print("Contrainte héritage non respecter")