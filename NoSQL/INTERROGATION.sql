/*Requête pour voir l'ensemble des utilisateurs : (Fusion d' abonné et occasionnel)*/
	SELECT mail FROM Compte;
	Ou
    SELECT DISTINCT  idUser FROM Abonne UNION SELECT idUser FROM Occasionnel;
/*Requête pour voir le nombre des utilisateurs :*/
	SELECT COUNT(mail) FROM Compte;
/*Requête pour voir l'ensemble des abonnés*/
	SELECT nom,prenom,mail FROM Abonne
/*Requête pour voir le nombre des abonnés*/
	SELECT count(idUser) FROM Abonne;
/*Requete pour voir l'ensemble des occasionnels*/
	SELECT mail FROM Occasionnel;
/*Requete pour voir le nombre des occasionnels*/
	SELECT count(idUser) FROM Occasionnel;
/*Requete pour voir l'ensemble des parkings*/
	SELECT * FROM Parking;
/*Requete pour voir le nombre des parkings*/
	SELECT count(adresse) FROM Parking;

/*Requete pour voir l'ensemble des places utilisés dans chaque parking (du plus petit au plus grand)*/
    SELECT parking ,COUNT(idPlace)
    FROM Place
    WHERE libre=false
    GROUP BY parking
    ORDER BY COUNT
/*Requete pour voir l'ensemble des places dans chaque parking (du plus petit au plus grand)*/
	SELECT parking ,COUNT(idPlace)
    FROM Place
    GROUP BY parking
    ORDER BY COUNT;
/*Requete pour afficher le nombre de places disponibles dans chaque parking*/
	SELECT parking ,COUNT(idPlace)
    FROM Place
    WHERE libre=true
    GROUP BY parking
    ORDER BY COUNT;
/*Requete pour afficher le nombre de places disponibles dans l’ensemble des parkings*/
	SELECT COUNT(idPlace) AS Dispo
    FROM Place
    WHERE libre=true;
/*Requete pour voir l'ensemble des places en plein air dans chaque parking (du plus petit au plus grand)*/
	SELECT parking ,COUNT(idPlace)
    FROM Place
    WHERE type_place='Plein air'
    GROUP BY parking
    ORDER BY COUNT;
/*Requete pour voir l'ensemble des places en plein air et libre dans chaque parking (du plus petit au plus grand)*/
	SELECT parking ,COUNT(idPlace)
    FROM Place
    WHERE type_place='Plein air' AND libre=true
    GROUP BY parking
    ORDER BY COUNT;
/*Requete pour voir l'ensemble des places couvertes dans chaque parking (du plus petit au plus grand)*/
	SELECT parking ,COUNT(idPlace)
    FROM Place
    WHERE type_place='Couvert'
    GROUP BY parking
    ORDER BY COUNT;
/*Requete pour voir l'ensemble des places couvertes et libre dans chaque parking (du plus petit au plus grand)*/
	SELECT parking ,COUNT(idPlace)
    FROM Place
    WHERE type_place='Couvert' AND libre=true
    GROUP BY parking
    ORDER BY COUNT;
/*Requete pour voir l'ensemble des places pour les véhicules de type deux roues dans chaque parking (du plus petit au plus grand)*/
    SELECT parking ,COUNT(idPlace)
    FROM Place
    WHERE type_vehicule = 'Deux roues' 
    GROUP BY parking
    ORDER BY COUNT;
/*Requete pour voir l'ensemble des places pour les véhicules de type deux roues libre dans chaque parking (du plus petit au plus grand)*/
    SELECT parking ,COUNT(idPlace)
    FROM Place
    WHERE type_vehicule = 'Deux roues'  AND libre=true
    GROUP BY parking
    ORDER BY COUNT;
/*Requete pour voir l'ensemble des places pour les véhicules simples dans chaque parking (du plus petit au plus grand)*/
	SELECT parking ,COUNT(idPlace)
    FROM Place
    WHERE type_vehicule = 'Vehicule simple' 
    GROUP BY parking
    ORDER BY COUNT;
/*Requete pour voir l'ensemble des places pour les véhicules simples libre dans chaque parking (du plus petit au plus grand)*/
	SELECT parking ,COUNT(idPlace)
    FROM Place
    WHERE type_vehicule = 'Vehicule simple' AND libre=true
    GROUP BY parking
    ORDER BY COUNT;
/*Requete pour voir l'ensemble des places pour les camions libre dans chaque parking (du plus petit au plus grand)*/
	SELECT parking ,COUNT(idPlace)
    FROM Place
    WHERE type_vehicule ='Camion'
    GROUP BY parking
    ORDER BY COUNT;

/*Requete pour voir l'ensemble des places pour les camions libre dans chaque parking (du plus petit au plus grand)*/
	SELECT parking ,COUNT(idPlace)
    FROM Place
    WHERE type_vehicule ='Camion' AND libre=true
    GROUP BY parking
    ORDER BY COUNT;

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/*Requete pour voir les détails de l'abonnement de chaque personne */
	SELECT Ab.nom,Ab.prenom,Ab.mail,A.dateDebut,A.dateFin,A.methodePayment
    FROM Abonnement A JOIN Abonne Ab ON A.mail=Ab.mail;
/*Requete pour voir le nombre de parking par zone*/
	SELECT zone,COUNT(*) FROM Parking GROUP BY zone;
/*Requete pour voir le nombre de ticket vendu*/
	SELECT COUNT(idTransaction) AS Ventes FROM Ticket;



/*Requete pour afficher le nombre de voiture par utilisateur*/
	SELECT iduserocca AS idUser, COUNT(*) AS Quantite_voiture FROM Vehicule WHERE iduserocca IS NOT NULL GROUP BY iduserocca
    UNION
    SELECT iduserabo AS idUser, COUNT(*) AS Quantite_voiture FROM Vehicule WHERE iduserabo IS NOT NULL GROUP BY iduserabo;

/*Requete pour afficher le nombre moyen de voiture par utilisateur*/

/*Requete pour afficher le nombre d’abonnement par parking*/
    SELECT parking,COUNT(parking)
    FROM Abonnement
    group by parking;
/*Requete pour afficher le nombre de tickets par parking l’année 2022*/
	SELECT parking,COUNT(parking)
    FROM Ticket
    WHERE EXTRACT(YEAR FROM date_transaction)>2022
    GROUP BY parking;


/*Requete pour voir le nombre de payment Automate par parking*/
	SELECT parking,COUNT(*) AS Automate FROM Ticket WHERE methodepayment='Automate' GROUP BY parking 
    UNION
    SELECT parking,COUNT(*) AS Automate FROM Abonnement WHERE methodepayment='Automate' GROUP BY parking
    UNION
    SELECT parking,COUNT(*) AS Automate FROM Place INNER JOIN Reservation ON Place.idplace=Reservation.place_reserve 
    GROUP BY parking;
;

/*Requete pour voir le chiffre d'affaire d'un parking*/
	SELECT COUNT
/*Requete pour voir le chiffre d'affaire de l'ensemble des parkings*/
	SELECT COUNT


/*? Requete pour voir l'ID des places reservés par parking
	SELECT idplace FROM Place WHERE place_reserve IS NOT NULL
? Requete pour voir l'ID des places reservés par qui dans quel parking
	SELECT mail,parking,idplace FROM Place INNER JOIN Reservation ON Place.place_reserve=Reservation.idtransaction*/

