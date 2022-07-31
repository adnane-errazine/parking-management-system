import psycopg2

def afficherZone(conn):
    cur= conn.cursor()
    sql = "SELECT * FROM Zone"
    cur.execute(sql)
    row = cur.fetchone()
    while row :
        nomzone = row[0]
        prix = row[1]
        print("\t%s[%s$]"%(nomzone, prix))
        row = cur.fetchone()

def creeZone(conn):
    cur = conn.cursor()
    nomzone = input("Nom de la nouvelle zone: ")
    prix = int(input("Prix de la zone"))

    try:
        sql = "INSERT INTO Zone VALUES('%s',%i)" % (nomzone, prix)
        cur.execute(sql)
        conn.commit()
        print("La zone %s de prix %i a bien été crée"%(nomzone, prix))
    except psycopg2.IntegrityError as e :
        conn.rollback()
        print("Message d'erreur système:",e)


def modifierZone(conn):
    cur= conn.cursor()
    sql = "SELECT * FROM Zone"
    cur.execute(sql)
    row = cur.fetchone()
    while row :
        print("\t%s[%s$]"%(row[0], row[1]))
        row = cur.fetchone()

    nomzone = input("Nom de la zone à modifier: ")
    nouv_nom_zone = input("Nouveau nom de zone: ")
    nouv_prix = int(input("Nouveau prix: "))
    try:
        sql = "UPDATE Zone SET nomZone= '%s',prix=%i WHERE nomzone = '%s'"%(nouv_nom_zone, nouv_prix, nomzone)
        cur.execute(sql)
        conn.commit()
        print("La zone %s a été modifié, nouveau nom : %s, nouveau prix: %i"%(nomzone, nouv_nom_zone, nouv_prix))
    except psycopg2.IntegrityError as e :
        conn.rollback()
        print("Message d'erreur système:",e)

def afficherTousParking(conn):
    cur= conn.cursor()
    sql = "SELECT * FROM Parking"
    cur.execute(sql)
    row = cur.fetchone()
    print("\tAdresse [Place_Plein_Air | Place_Couvert]  Zone\n")
    while row :
        adresse = row[0]
        maxPlaceAir = row[1]
        MaxPlaceCouvert = row[2]
        zone = row[3]

        print("\t%s[%i | %i ]  %s"%(adresse, maxPlaceAir, MaxPlaceCouvert, zone))
        row = cur.fetchone()
    print("\nTous les parkings ont été affichés avec succès ")

def suppressionZone(conn):
    afficherZone(conn)
    nomzone = input("Nom de la zone à supprimer: ") 
    cur= conn.cursor()
    try:
        sql = "DELETE FROM Zone WHERE nomzone = '%s' "%(nomzone) # #Attention, la table Zone possède des parkings apparaissant en clés étrangère, la supression cause une supression en cascades des parkings et place associés

        cur.execute(sql)
        conn.commit()
        print("La zone: %s a été supprimé, les parkings, places et abonnements lui faisant référence aussi."%(nomzone))

    except psycopg2.IntegrityError as e:
         conn.rollback()
         print("Message système :", e)

def afficherTousPlaces(conn):
    cur= conn.cursor()
    sql = "SELECT * FROM Place"
    cur.execute(sql)
    row = cur.fetchone()
    print("\n\tidplace | adresse du parking | [Type de Places | Type de Vehicules]  | Libre")
    while row :
        idplace = row[0]
        adressePark = row[1]
        typePlace = row[2]
        typeVehicule = row[3]
        libre = row[4]

        print("\t%i | %s | [%s | %s ]  %s"%(idplace, adressePark, typePlace, typeVehicule, libre))
        row = cur.fetchone()
    print("\nToutes les places ont été affichés avec succès ")


def afficherTousVehicules(conn):
    cur= conn.cursor()
    sql = "SELECT immatriculation, type FROM Vehicule"
    cur.execute(sql)
    row = cur.fetchone()
    print("\n\tImmatriculation | type")
    while row :
        immat = row[0]
        typeVehicule = row[1]

        print("\t%s | %s"%(immat, typeVehicule))
        row = cur.fetchone()
    print("\nToutes les véhicules ont été affichés avec succès ")