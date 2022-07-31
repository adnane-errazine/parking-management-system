def creationCompteabo(conn,mail,mdp) :
    cur=conn.cursor()
    sql="INSERT INTO Compte VALUES('%s','%s')"%(mail,mdp)
    cur.execute(sql)
    conn.commit()
    nom = input("Quel est votre nom :")
    prenom = input("Quel est votre prénom: ")
    # Affichage des abonné deja existant
    try:
        sql="SELECT * FROM Abonne"
        cur.execute(sql)
        print("--Abonné--\n")
        res = cur.fetchall()
        for raw in res:
            id = raw[0]
            nom2 = raw[1]
            prenom2 = raw[2]
            mail2 = raw[3]
            print("- %i %s %s | %s" %(id,nom2,prenom2,mail2))
    except psycopg2.IntegrityError as e:
        conn.rollback()
        print("Message système :", e)
    idabo= int(input("idabo: "))
    sql2="SELECT * FROM Occasionnel WHERE iduser = %i "%(idabo)
    cur.execute(sql2)
    raw = cur.fetchone()

    if raw == None:
        try:
            sql3 = "INSERT INTO Abonne VALUES(%i, '%s', '%s', '%s')"%(idabo, nom, prenom, mail)
            cur.execute(sql3)
            conn.commit()
            print("Bienvenue M/ MME %s %s dans votre espace abonné !\n"%(nom, prenom))
        except psycopg2.IntegrityError as e:
            conn.rollback()
            print("Message système :", e)
    else:
        print("Erreur: Contraintes d'heritage abstrait non satisfait, veuillez renseigner un identifiant different de ceux présent dans la clase Occasionel")
        abort()


def creationCompteOccas(conn,mail,mdp) :
    cur=conn.cursor()
    sql="INSERT INTO Compte VALUES('%s','%s')"%(mail,mdp)
    cur.execute(sql)
    conn.commit()
    #nom = input("Quel est votre nom :")
    #prenom = input("Quel est votre prénom: ")
    # Affichage des abonné deja existant
    try:
        sql="SELECT * FROM Occasionnel"
        cur.execute(sql)
        print("--Occasionnels--\n")
        res = cur.fetchall()
        for raw in res:
            id = raw[0]
            mail2 = raw[1]
            print("- %i | %s" %(id,mail2))
    except psycopg2.IntegrityError as e:
        conn.rollback()
        print("Message système :", e)
    idoccas = int(input("idabo: "))
    sql2="SELECT * FROM Abonne WHERE iduser = %i "%(idabo)
    cur.execute(sql2)
    raw = cur.fetchone()

    if raw == None:
        try:
            sql3 = "INSERT INTO Abonne VALUES(%i, '%s')"%(idoccas, mail)
            cur.execute(sql3)
            conn.commit()
            print("Bienvenue M/ MME dans votre espace abonné !\n")
        except psycopg2.IntegrityError as e:
            conn.rollback()
            print("Message système :", e)
    else:
        print("Erreur: Contraintes d'heritage abstrait non satisfait, veuillez renseigner un identifiant different de ceux présent dans la clase Occasionel")
        abort()

