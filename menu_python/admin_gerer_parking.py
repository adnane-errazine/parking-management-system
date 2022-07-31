from datetime import datetime
import psycopg2
import prix_zone

def afficherParking(conn,nomZone):
	cur= conn.cursor()
	sql = "SELECT * FROM Parking WHERE zone = '%s'"%(nomZone)
	cur.execute(sql)
	raw = cur.fetchone()
	while raw :
		adresse = raw[0]
		maxPlaceAir = raw[1]
		MaxPlaceCouvert = raw[2]
		zone = raw[3]
		print("\t%s[%i | %i ]  %s"%(adresse, maxPlaceAir, MaxPlaceCouvert, zone))
		raw = cur.fetchone()



def ajouterParking(conn, nomZone):
	cur= conn.cursor()
	adresse = input("adresse du nouveau parking: ")
	maxPlaceAir = int(input("Nombre total de place plein air: "))
	maxPlaceCouvert = int(input("Nombre total de place couvertes: "))

	try:
		sql = "INSERT INTO Parking VALUES('%s', %i, %i, '%s')"%(adresse, maxPlaceAir, maxPlaceCouvert, nomZone)
		cur.execute(sql)
		conn.commit()
		print("Nouveau parking d'adresse %s [Place air: %i | Place Couvertes: %i] dans la zone %s ajouté avec succès"%(adresse, maxPlaceAir, maxPlaceCouvert, nomZone))

	except psycopg2.IntegrityError as e :
		conn.rollback()
		print("Message d'erreur système:",e)


def modifierParking(conn, nomZone): # Changement de zone d'un parking
	cur= conn.cursor()
	sql = "SELECT * FROM Parking WHERE zone = '%s'"%(nomZone)
	cur.execute(sql)
	raw = cur.fetchone()
	while raw :
		adresse = raw[0]
		maxPlaceAir = raw[1]
		MaxPlaceCouvert = raw[2]
		zone = raw[3]
		print("\t%s[%i | %i ]  %s"%(adresse, maxPlaceAir, MaxPlaceCouvert, zone))
		raw = cur.fetchone()

	cur= conn.cursor()
	adresse = input("Adresse du parking à modifier: ")
	nouvzone = input("Zone pour changer le parking: ")
	try:

		sql = "UPDATE Parking SET zone = '%s' WHERE adresse = '%s'"%(nouvzone, adresse)
		cur.execute(sql)
		conn.commit()

		cur= conn.cursor()
		sql2 = "SELECT prix FROM Zone WHERE nomzone = '%s'"%(nouvzone)
		cur.execute(sql2)
		raw = cur.fetchone()
		nouv_prix = raw[0]
		print("Le parking d'adresse: %s a été modifié, nouvelle zone: %s [%i$]"%(adresse, nouvzone, nouv_prix))
	except psycopg2.IntegrityError as e :
		conn.rollback()
		print("Message d'erreur système:",e)


def supressionParking(conn, nomZone):
	afficherParking(conn,nomZone)
	cur= conn.cursor()
	adresse = input("Adresse du parking à supprimer: ")
	try:
		sql = "DELETE FROM Parking WHERE adresse = '%s'"%(adresse) #Attention, la table Place possède les parkings en clés étrangère, la supression cause une supression en cascades des places
		
		cur.execute(sql)
		conn.commit()
		print("Le parking d'adresse: %s a été supprimé, les places et abonnements lui faisant référence aussi."%(adresse))
	except psycopg2.IntegrityError as e:
		 conn.rollback()
		 print("Message système :", e)

def ajoutPlaces(conn, nomZone):
	afficherParking(conn,nomZone)
	cur= conn.cursor()
	adresse = input("Adresse du parking pour y ajouter des places libres: ")
	sql = "SELECT max_place_plein_air FROM Parking WHERE adresse = '%s'"%(adresse)
	cur.execute(sql)
	raw = cur.fetchone()
	MaxPleinAir = raw[0]

	cur= conn.cursor()
	sql2 = "SELECT max_place_couvert FROM Parking WHERE adresse = '%s'"%(adresse)
	cur.execute(sql2)
	raw = cur.fetchone()
	MaxCouvert = raw[0]
	
	nbPlacesCouvertes = -1
	nbPlacesPleinAir = -1
	while (nbPlacesCouvertes <0 or nbPlacesPleinAir<0 or  nbPlacesCouvertes > MaxCouvert or nbPlacesCouvertes>MaxPleinAir):
		nbPlacesCouvertes = int(input("Nombre de places couvertes que vous voulez ajouter: "))
		nbPlacesPleinAir = int(input("Nombre de places plein air que vous voulez ajouter: "))

	if (nbPlacesCouvertes != 0):
		print("\nAjout des places couvertes ")
		for i in range(nbPlacesCouvertes):
			typePlaceVehic= {1: 'Deux roues', 2:'Vehicule simple', 3:'Camion'}
			i=0
			while (i <1 or i>3):
				i = int(input("Type de place à ajouter: 1/Deux roues | 2/Vehicule Simple | 3/Camion "))
		
			prix_zone.afficherTousPlaces(conn)
			idPlace = int(input("Id de la place: "))
			cur= conn.cursor()
			try:
				
				sql3="INSERT INTO Place VALUES(%i, '%s', 'Couvert', '%s', True)"%(idPlace, adresse, typePlaceVehic[i])
				cur.execute(sql3)
				conn.commit()
			except psycopg2.IntegrityError as e:
				 conn.rollback()
				 print("Message système :", e)
		print("Ajout des %i places couvertes libres realisé avec succès"%(nbPlacesCouvertes))

	if (nbPlacesPleinAir != 0):
		for i in range(nbPlacesPleinAir):
			typePlaceVehic= {1: 'Deux roues', 2:'Vehicule simple', 3:'Camion'}
			i=0
			while (i <1 or i>3):
				i = int(input("Type de place à ajouter: 1/Deux roues | 2/Vehicule simple | 3/Camion: "))

			prix_zone.afficherTousPlaces(conn)
			idPlace = int(input("Id de la place: "))
			cur= conn.cursor()
			try:
				#print(typePlaceVehic[i])
				sql4="INSERT INTO Place VALUES(%i, '%s', 'Plein air', '%s', True)"%(idPlace, adresse, typePlaceVehic[i])
				cur.execute(sql4)
				conn.commit()
				
			except psycopg2.IntegrityError as e:
				 conn.rollback()
				 print("Message système :", e)
		print("Ajout des %i places Plein Air libre realisé avec succès"%(nbPlacesCouvertes))


def supressionPlaces(conn,nomZone):
	afficherParking(conn,nomZone)
	cur= conn.cursor()
	prix_zone.afficherTousPlaces(conn)
	i=0
	i = int(input("Combien de places souhaiteriez vous supprimer ?"))

	for i in range(i):
		try:
			idPlace = int(input("Id de la place: "))
			sql = "DELETE FROM Place WHERE idPlace = %i "%(idPlace)
			cur.execute(sql)
			conn.commit()
			print("Suprresion de la place d'id %i realisé avec succès"%(idPlace))

		except psycopg2.IntegrityError as e:
					 conn.rollback()
					 print("Message système :", e)
# AJOUTER SUPPRIMER DES PLACES

