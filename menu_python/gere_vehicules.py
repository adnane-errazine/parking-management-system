import psycopg2

def gerer_vehicules_abo(conn,mail):
    cur= conn.cursor()
    print("Que voulez-vous faire ?")
    print("1 : Voir mes véhicules")
    print("2 : Ajouter un véhicule")
    i=int(input("Séléction : "))
    if i==1:
        try:
            sql="SELECT * FROM Vehicule, Abonne WHERE mail='%s' and Vehicule.idUserAbo=Abonne.iduser"%mail
            cur.execute(sql)
        except psycopg2.IntegrityError as e:
            conn.rollback()
            print("Message système :", e)
        raw = cur.fetchone()
        while (raw):
            immat=raw[0]
            idAbo=raw[1]
            idOca=raw[2]
            type=raw[4]
            print("immatriculation : %s \t idAbo : %i \t Type : %s \n")%(immat,idAbo,type)
            raw=cur.fetchone()
    if i==2:
        add_immat=input("Immatriculation du véhicule ? ")
        type=input("Type du véhicule ? ")
        try:
            sql="SELECT * FROM Vehicule, Abonne WHERE mail='%s' and Vehicule.idUserAbo=Abonne.iduser"%mail
            cur.execute(sql)
        except psycopg2.IntegrityError as e:
            conn.rollback()
            print("Message système :", e)
        raw = cur.fetchone()
        while (raw):
            immat=raw[0]
            idAbo=raw[1]
            idOca=raw[2]
            type=raw[4]
        try:
            sql="INSERT INTO Vehicule(Immatriculation,idUserAbo,type) VALUES ('%s',%i,'%s')"%(add_immat,idAbo,type)
            cur.execute(sql)
            conn.commit()
        except psycopg2.IntegrityError as e:
             conn.rollback()
             print("Message système :", e)

def gerer_vehicules_occa(conn,mail):
    cur.conn.cursor()
    print("Que voulez-vous faire ?")
    print("1 : Voir mes véhicules")
    print("2 : Ajouter un véhicule")
    i=int(input("Séléction : "))
    if i==1:
        try:
            sql="SELECT * FROM Vehicule, Occasionnel WHERE mail='%s' and Vehicule.iduserocca=Occasionnel.iduser"%mail
            cur.execute(sql)
        except psycopg2.IntegrityError as e:
            conn.rollback()
            print("Message système :", e)
        raw = cur.fetchone()
        while (raw):
            immat=raw[0]
            idAbo=raw[1]
            idOca=raw[2]
            type=raw[4]
            print("immatriculation : %s \t idOcca : %i \t Type : %s \n")%(immat,idOca,type)
            raw=cur.fetchone()
    if i==2:
        add_immat=input("Immatriculation du véhicule ? ")
        type=input("Type du véhicule ? ")
        try:
            sql="SELECT * FROM Vehicule, Occasionnel WHERE mail='%s' and Vehicule.idUserOcca=Occasionnel.iduser"%mail
            cur.execute(sql)
        except psycopg2.IntegrityError as e:
            conn.rollback()
            print("Message système :", e)
        raw = cur.fetchone()
        while (raw):
            immat=raw[0]
            idAbo=raw[1]
            idOca=raw[2]
            type=raw[4]
        try:
            sql="INSERT INTO Vehicule(Immatriculation,idUserOcca,type) VALUES ('%s',%i,'%s')"%(add_immat,idOca,type)
            cur.execute(sql)
            conn.commit()
        except psycopg2.IntegrityError as e:
             conn.rollback()
             print("Message système :", e)
