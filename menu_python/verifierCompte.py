def verifierCompte(conn,mail,password):
    cur=conn.cursor()
    sql="SELECT * FROM Compte WHERE mail='%s' AND password='%s'"%(mail,password)
    cur.execute(sql)
    raw = cur.fetchone()
    if(raw==None):
        print("Vous avez saisi un email ou mdp incorrect !")
        return False
    else:
        cur=conn.cursor()
        sql="SELECT nom, prenom FROM Abonne WHERE mail='%s' "%(mail)
        cur.execute(sql)
        raw = cur.fetchone()
        nom = raw[0]
        prenom = raw[1]

        print("Bienvenue M/ MME %s %s dans votre compte"%(nom, prenom))
        return True



def verifierCompteoccas(conn,mail,password):
    cur=conn.cursor()
    sql="SELECT * FROM Compte WHERE mail='%s' AND password='%s'"%(mail,password)
    cur.execute(sql)
    raw = cur.fetchone()
    if(raw==None):
        print("Vous avez saisi un email ou mdp incorrect !")
        return False
    else:
        print("Bienvenue %s dans votre compre"%(mail))
        return True
