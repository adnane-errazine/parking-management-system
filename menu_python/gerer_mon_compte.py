def gerer_mon_compte(conn,mail,mdp):
    cur=conn.cursor()
    print("Voulez-vous modifier le mail (1) ou le mdp (2) ?")
    i=int(input("Séléction : "))
    if i==1:
        modif_mail=input("Nouveau mail ? ")
        sql="UPDATE Compte SET mail='%s' WHERE mail='%s'"%(modif_mail,mail)
        cur.execute(sql)
    elif i==2:
        modif_mdp=input("Nouveau mdp ? ")
        sql="UPDATE Compte SET password='%s' WHERE password='%s'"%(modif_mdp,mdp)
        cur.execute(sql)
    else:
        print("Erreur de saisie")

