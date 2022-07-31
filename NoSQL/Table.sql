DROP TABLE IF EXISTS Abonnement;
DROP TABLE IF EXISTS Ticket;
DROP TABLE IF EXISTS Reservation;

DROP TABLE IF EXISTS Place;
DROP TABLE IF EXISTS Parking; 
--DROP TABLE IF EXISTS Zone;

DROP TABLE IF EXISTS Vehicule;

DROP TABLE IF EXISTS Occasionnel;
DROP TABLE IF EXISTS Abonne;

DROP TABLE IF EXISTS Compte;


CREATE TABLE Compte(
  mail VARCHAR PRIMARY KEY,
  password VARCHAR NOT NULL
);

CREATE TABLE Abonne(
idUser INTEGER PRIMARY KEY,
nom VARCHAR NOT NULL,
prenom VARCHAR NOT NULL,
mail VARCHAR REFERENCES Compte(mail) ON DELETE CASCADE,
vehicule JSON
);

CREATE TABLE Occasionnel(
idUser INTEGER PRIMARY KEY,
mail VARCHAR REFERENCES Compte(mail) ON DELETE CASCADE,
vehicule JSON NOT NULL
);

--On garde la table vehicule pour pouvoir y accéder à partir de réservation et de abonnement
CREATE TABLE Vehicule(
Immatriculation VARCHAR PRIMARY KEY,
idUserAbo INTEGER REFERENCES Abonne(idUser) ON DELETE CASCADE,
idUserOcca INTEGER REFERENCES Occasionnel(idUser) ON DELETE CASCADE,
type VARCHAR NOT NULL CHECK( type = 'Deux roues' OR type = 'Camion' OR type = 'Vehicule simple')
);

--TABLE zone obsolete puisqu'elle est maintenant représentée par le type JSON dans Parking
/*CREATE TABLE Zone (
  nomZone VARCHAR PRIMARY KEY,
  Prix FLOAT NOT NULL,
  CHECK (Prix>=0)
);*/


CREATE TABLE Parking (
  adresse VARCHAR PRIMARY KEY,
  max_place_plein_air INTEGER,
  max_place_couvert INTEGER,
  --zone VARCHAR REFERENCES Zone(nomZone) ON DELETE CASCADE,
  zone JSON NOT NULL,
  CHECK (max_place_plein_air>=0),
  CHECK (max_place_couvert>=0)
  );

CREATE TABLE Place (
  idPlace INTEGER PRIMARY KEY,
  parking VARCHAR REFERENCES Parking(adresse) ON DELETE CASCADE,
  type_place VARCHAR NOT NULL CHECK(type_place = 'Plein air' OR type_place = 'Couvert'),
  type_vehicule VARCHAR NOT NULL CHECK (type_vehicule = 'Deux roues' OR type_vehicule ='Camion' OR type_vehicule = 'Vehicule simple'),
  libre BOOLEAN NOT NULL
);

CREATE TABLE Reservation(
  idTransaction INTEGER PRIMARY KEY,
  methodePayment VARCHAR NOT NULL CHECK (methodePayment = 'Guichet' OR methodePayment ='Automate' OR methodePayment ='Reservation'),
  date_transaction TIMESTAMP NOT NULL,
  date_debut TIMESTAMP NOT NULL,
  date_Expiration TIMESTAMP NOT NULL,
  mail VARCHAR REFERENCES Compte(mail) ON DELETE CASCADE,
  place_reserve INTEGER REFERENCES Place(idPlace) ON DELETE CASCADE,
  vehicule_immat VARCHAR REFERENCES Vehicule(immatriculation) ON DELETE CASCADE,
  CHECK(date_Expiration > date_debut),
  CHECK (date_transaction < date_debut)
);

CREATE TABLE Ticket (
  idTransaction INTEGER PRIMARY KEY,
  methodePayment VARCHAR NOT NULL CHECK (methodePayment='Guichet' OR methodePayment='Automate' OR methodePayment='Reservation'),
  date_transaction TIMESTAMP NOT NULL,
  date_fin TIMESTAMP NOT NULL,
  place INTEGER REFERENCES Place(idPlace) ON DELETE CASCADE,
  parking VARCHAR REFERENCES Parking(adresse) ON DELETE CASCADE,
  occasionnel INTEGER REFERENCES Occasionnel(idUser)ON DELETE CASCADE,
  CHECK (date_transaction < date_fin)
);

CREATE TABLE Abonnement(
  idTransaction INTEGER PRIMARY KEY,
  methodePayment VARCHAR NOT NULL CHECK (methodePayment='Guichet' OR methodePayment='Automate' OR methodePayment='Reservation'),
  date_transaction TIMESTAMP NOT NULL,
  date_Debut TIMESTAMP NOT NULL,
  date_Fin TIMESTAMP NOT NULL,
  mail VARCHAR NOT NULL REFERENCES Compte(mail) ON DELETE CASCADE,
  vehicule_immat VARCHAR REFERENCES Vehicule(immatriculation) ON DELETE CASCADE,
  place INTEGER REFERENCES Place(idPlace) ON DELETE CASCADE,

  CHECK (date_Fin > date_Debut),
  CHECK (date_transaction < date_Debut)
);
