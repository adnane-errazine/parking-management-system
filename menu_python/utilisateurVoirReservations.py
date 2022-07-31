def utilisateurVoirReservations(conn,mail):
        cur=conn.cursor()
        try:
            sql="SELECT * FROM Reservation WHERE mail='%s'"%mail
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
            print("id : %i \t methode de paiement : %s \t date_transaction : %s \t date_debut : %s \t date_fin : %s \t mail: %s \t place:%i \t Vehicule : %s \n")%(id,methode,date_transaction,date_debut,date_fin,mail,place,vehicule)
            raw=cur.fetchone()
