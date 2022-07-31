import psycopg2

def see_users(conn):
    cur=conn.cursor()
    try:
        sql="SELECT * FROM Abonne"
        cur.execute(sql)
    except psycopg2.IntegrityError as e:
        conn.rollback()
        print("Message système :", e)
    print("--Abonné--\n")
    res = cur.fetchall()
    for raw in res:
        id = raw[0]
        nom = raw[1]
        prenom = raw[2]
        mail = raw[3]
        print("- %i %s %s | %s" %(id,nom,prenom,mail))

    cur=conn.cursor()
    try:
        sql="SELECT * FROM Occasionnel"
        cur.execute(sql)
    except psycopg2.IntegrityError as e:
        conn.rollback()
        print("Message système :", e)
    print("\n--Occasionnel--\n")
    res = cur.fetchall()
    for raw in res:
        id = raw[0]
        mail = raw[1]
        print("- %i %s" % (id,mail))

def creer_compte(conn, mail):
    addpwd=input("Password : ")
    cur=conn.cursor()
    sql = "INSERT INTO Compte VALUES ('%s', '%s')" % (mail,addpwd)
    cur.execute(sql)
    conn.commit()

def addAbo(conn):
    addnom=input("Nom de l'abonne : ")
    addprenom=input("Prenom de l'abonne : ")
    addmail=input("Mail de l'abonne : ")
    see_users(conn)
    addid=int(input("Id/Integer de l'abonne : "))
    print("Vous devez creer un compte")
    creer_compte(conn, addmail)
    cur = conn.cursor()
    try:
        sql = "INSERT INTO Abonne VALUES (%i, '%s', '%s', '%s')" % (addid, addnom, addprenom, addmail)
        cur.execute(sql)
        conn.commit()
    except psycopg2.IntegrityError as e:
        conn.rollback()
        print("Message système : ", e)
    print("Le compte et l'abonne ont bien ete cree")

def addOcca(conn):
    addmail=input("Mail de l'occasionnel : ")
    see_users(conn)
    addid=int(input("Id de l'occasionnel : "))
    print("Vous devez creer un compte")
    creer_compte(conn, addmail)
    cur = conn.cursor()
    try:
        sql = "INSERT INTO Occasionnel VALUES (%i,'%s')" % (addid,addmail)
        cur.execute(sql)
        conn.commit()
    except psycopg2.IntegrityError as e:
        conn.rollback()
        print("Message système : ", e)
    print("L'occasionnel a bien ete cree")

def delete_user(conn):
    user=int(input("Voulez-vous supprimer un abonne (1) ou un occasionnel (2) ?"))
    if user==1:
        id_abo=int(input("Quel est l'ID de l'abonne que vous voulez supprimer ?"))
        see_users(conn)
        cur = conn.cursor()
        try:
            sql = "DELETE FROM Abonne WHERE idUser=%i"%id_abo
            cur.execute(sql)
            conn.commit()
        except psycopg2.IntegrityError as e:
            conn.rollback()
            print("Message système : ", e)
    elif user==2:
        id_occa=int(input("Quel est l'ID de l'occasionnel que vous voulez supprimer ?"))
        cur = conn.cursor()
        try:
            sql = "DELETE FROM Occasionnel WHERE idUser=%i"%id_occa
            cur.execute(sql)
            conn.commit()
        except psycopg2.IntegrityError as e:
            conn.rollback()
            print("Message système : ", e)
    else:
        print("Erreur")
    
