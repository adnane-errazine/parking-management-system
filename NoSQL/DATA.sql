    INSERT INTO Compte(mail, password) VALUES ('boris.lefoll1@gmail.com','nf18p037');
    INSERT INTO Compte(mail, password) VALUES ('errazine.adnane@gmail','nf18p030');
    INSERT INTO Compte(mail, password) VALUES ('erickmwatanabek@gmail.com','nf18p047');
    INSERT INTO Compte(mail, password) VALUES ('alberguillaumek@gmail.com','nf18p027');
    INSERT INTO Compte(mail, password) VALUES ('italo.ferreira@gmail.com','wslbrasil');
    INSERT INTO Compte(mail, password) VALUES ('gabriel.medina@gmail.com','wslbrasil');
    INSERT INTO Compte(mail, password) VALUES ('felipe.toledo@gmail.com','wslbrasil');
    INSERT INTO Compte(mail, password) VALUES ('johnjohn.florence@gmail.com','wslbrasil');

    INSERT INTO Compte(mail, password) VALUES ('adnane.momo@gmail.com','nf18');
    INSERT INTO Compte(mail, password) VALUES ('valider_uv@gmail.com','bonnenote');
    INSERT INTO Compte(mail, password) VALUES ('dernierRapport@gmail.com','nf18valider');
    INSERT INTO Compte(mail, password) VALUES ('adnane.errazine@gmail.com','ezggwp');
    INSERT INTO Compte(mail, password) VALUES ('moris@gmail.com','haha');
    INSERT INTO Compte(mail, password) VALUES ('lo21IA02@gmail.com','tropdur');


    INSERT INTO Abonne VALUES (1,'LE FOLL','Boris','boris.lefoll1@gmail.com',
    '[{"immatriculation":"8462AM","type":"Deux roues"},
    {"immatriculation":"909BT","type":"Deux roues"},
    {"immatriculation":"1342AM","type":"Camion"}]');
    INSERT INTO Abonne VALUES (2,'ALBER','Guillaume','alberguillaumek@gmail.com','[{"immatriculation":"9859BT","type":"Camion"}]');
    INSERT INTO Abonne VALUES (3,'FERREIRA','Italo','italo.ferreira@gmail.com','[{"immatriculation":"9397JK","type":"Deux roues"},{"immatriculation":"9276XO","type":"Vehicule simple"}]');
    INSERT INTO Abonne VALUES (4,'Medina','Gabriel','gabriel.medina@gmail.com','[{"immatriculation":"4398LK","type":"Deux roues"}]');

    INSERT INTO Abonne VALUES (8,'momo','faba','adnane.momo@gmail.com','[{"immatriculation":"97842D","type":"Vehicule simple"}]');
    INSERT INTO Abonne VALUES (9,'rahoul','gasmi','valider_uv@gmail.com','[{"immatriculation":"TCIP21","type":"Camion"}]');
    INSERT INTO Abonne VALUES (12,'nas','XX','moris@gmail.com','[{"immatriculation":"DZE134","type":"Vehicule simple"},{"immatriculation":"SDFS24","type":"Deux roues"}]');

    INSERT INTO Occasionnel VALUES (5,'errazine.adnane@gmail','[{"Immatriculation":"6948XR", "type":"Camion"},{"Immatriculation":"5687RT","type":"Deux roues"}]');
    INSERT INTO Occasionnel VALUES (6,'erickmwatanabek@gmail.com','[{"Immatriculation":"9875ZT","type":"Vehicule simple"}]');
    INSERT INTO Occasionnel VALUES (7,'johnjohn.florence@gmail.com',
        '[{"Immatriculation":"8990ZT","type":"Deux roues"},
        {"Immatriculation":"7645HG","type":"Vehicule simple"}]');

    INSERT INTO Occasionnel VALUES (10,'dernierRapport@gmail.com','[{"Immatriculation":"234563","type":"Vehicule simple"},{"Immatriculation":"GE2345","type":"Camion"}]');
    INSERT INTO Occasionnel VALUES (11,'adnane.errazine@gmail.com','[{"Immatriculation":"53G234","type":"Vehicule simple"},{"Immatriculation":"UE2134","type":"Deux roues"}]');
    INSERT INTO Occasionnel VALUES (13,'lo21IA02@gmail.com','[{"Immatriculation":"RAA425","type":"Camione"},{"Immatriculation":"SIX345","type":"Deux roues"}]');

    INSERT INTO Vehicule(Immatriculation,idUserAbo,type) VALUES ('8462AM',1,'Deux roues');
    INSERT INTO Vehicule(Immatriculation,idUserAbo,type) VALUES ('9859BT',2,'Camion');
    INSERT INTO Vehicule(Immatriculation,idUserAbo,type) VALUES ('909BT',1,'Deux roues');
    INSERT INTO Vehicule(Immatriculation,idUserOcca,type) VALUES ('6948XR',5,'Camion');
    INSERT INTO Vehicule(Immatriculation,idUserAbo,type) VALUES ('1342AM',1,'Camion');
    INSERT INTO Vehicule(Immatriculation,idUserOcca,type) VALUES ('9875ZT',6,'Vehicule simple');
    INSERT INTO Vehicule(Immatriculation,idUserOcca,type) VALUES ('5687RT',5,'Deux roues');

    INSERT INTO Vehicule(Immatriculation,idUserOcca,type) VALUES ('324522',10,'Deux roues');
    INSERT INTO Vehicule(Immatriculation,idUserOcca,type) VALUES ('234RF3',11,'Vehicule simple');
    INSERT INTO Vehicule(Immatriculation,idUserAbo,type) VALUES ('123ZAE',12,'Vehicule simple');
    INSERT INTO Vehicule(Immatriculation,idUserOcca,type) VALUES ('4574ZE',13,'Camion');
    INSERT INTO Vehicule(Immatriculation,idUserOcca,type) VALUES ('ERT234',7,'Vehicule simple');
    
    /*
    INSERT INTO Zone VALUES ('Centre-ville',6);
    INSERT INTO Zone VALUES ('Plage',12);
    INSERT INTO Zone VALUES ('Centre Commercial',3);
    INSERT INTO Zone VALUES ('Rio',4);
    */
    INSERT INTO Parking VALUES ('12 rue Couttolenc', 100, 80, '{"nomzone":"Plage", "prix":12}');
    INSERT INTO Parking VALUES ('56 rue du general', 0, 180,'{"nomzone":"Centre-ville", "prix":6}');
    INSERT INTO Parking VALUES ('1 rue Bouvines', 100, 100,'{"nomzone":"Centre Commercial", "prix":6}');
    INSERT INTO Parking VALUES ('Botafogo Praia Shopping', 134, 90,'{"nomzone":"Rio", "prix":4}');
    INSERT INTO Parking VALUES ('Shopping Rio Sul', 134, 100,'{"nomzone":"Rio", "prix":4}');
    INSERT INTO Parking VALUES ('Trocadero', 124, 100,'{"nomzone":"Paris", "prix":13}');
    INSERT INTO Parking VALUES ('Champs Elysees', 144, 89,'{"nomzone":"Paris", "prix":13}');

    INSERT INTO Parking VALUES ('shaun the sheep', 100, 50,'{"nomzone":"Fes", "prix":1}');
    INSERT INTO Parking VALUES ('sunny parking', 300, 300,'{"nomzone":"Marrakesh", "prix":3}');

    INSERT INTO Place VALUES (1,'12 rue Couttolenc','Plein air','Deux roues',False);
    INSERT INTO Place VALUES (2,'12 rue Couttolenc','Couvert','Vehicule simple',True);
    INSERT INTO Place VALUES (3,'12 rue Couttolenc','Couvert','Vehicule simple',False);
    INSERT INTO Place VALUES (4,'12 rue Couttolenc','Couvert','Vehicule simple',False);
    INSERT INTO Place VALUES (5,'56 rue du general','Plein air','Camion',False);
    INSERT INTO Place VALUES (6,'1 rue Bouvines','Couvert','Camion',True);
    INSERT INTO Place VALUES (7,'1 rue Bouvines','Couvert','Camion',True);
    INSERT INTO Place VALUES (8,'Trocadero','Couvert','Deux roues',True);
    INSERT INTO Place VALUES (9,'Trocadero','Plein air','Deux roues',True);
    INSERT INTO Place VALUES (10,'Trocadero','Couvert','Camion',True);
    INSERT INTO Place VALUES (11,'Botafogo Praia Shopping','Plein air','Camion',True);
    INSERT INTO Place VALUES (12,'Botafogo Praia Shopping','Couvert','Vehicule simple',True);
    INSERT INTO Place VALUES (13,'Botafogo Praia Shopping','Couvert','Deux roues',true);

    INSERT INTO Place VALUES (14,'shaun the sheep','Couvert','Deux roues',false);
    INSERT INTO Place VALUES (15,'shaun the sheep','Couvert','Camion',false);
    INSERT INTO Place VALUES (16,'shaun the sheep','Couvert','Vehicule simple',false);
    INSERT INTO Place VALUES (17,'sunny parking','Plein air','Vehicule simple',false);
    INSERT INTO Place VALUES (18,'sunny parking','Plein air','Deux roues',false);
    INSERT INTO Place VALUES (19,'sunny parking','Plein air','Camion',false);

    INSERT INTO Ticket(idtransaction, methodepayment, date_transaction, date_fin, place, parking, occasionnel) VALUES (1,'Guichet','2022-05-19 17:00:00','2022-05-19 18:00:00',2,'12 rue Couttolenc',7);
    INSERT INTO Ticket VALUES (2,'Automate','2022-05-18 17:00:00','2022-05-19 01:00:18',3,'12 rue Couttolenc',5);
    INSERT INTO Ticket VALUES (3,'Automate','2022-05-19 17:00:00','2022-05-20 01:00:18',3,'12 rue Couttolenc',6);

    INSERT INTO Ticket VALUES (14,'Automate','2022-05-19 17:00:00','2022-05-20 01:00:18',17,'sunny parking',10);
    INSERT INTO Ticket VALUES (15,'Automate','2022-05-19 17:00:00','2022-05-20 01:00:18',18,'sunny parking',11);
    INSERT INTO Ticket VALUES (16,'Automate','2022-05-19 17:00:00','2022-05-20 01:00:18',14,'shaun the sheep',13);

    INSERT INTO Abonnement VALUES(4,'Guichet','2022-05-18 17:00:00','2022-05-19','2022-05-20','boris.lefoll1@gmail.com', '8462AM', 1);
    INSERT INTO Abonnement VALUES(5,'Automate','2022-05-17 17:00:00','2022-05-19','2022-05-22','alberguillaumek@gmail.com','9859BT',5);
    INSERT INTO Abonnement VALUES(6,'Automate','2022-05-16 17:00:00','2022-05-19','2022-05-23','boris.lefoll1@gmail.com', '909BT',6);
    INSERT INTO Abonnement VALUES(7,'Guichet','2022-05-16 17:00:00','2022-05-19','2022-05-24','alberguillaumek@gmail.com','1342AM',7 );

    INSERT INTO Abonnement VALUES(11,'Automate','2023-01-14 23:50:20','2023-10-27','2024-10-27','valider_uv@gmail.com','1342AM',14 );
    INSERT INTO Abonnement VALUES(12,'Automate','2022-08-25 17:00:00','2022-08-26','2022-09-25','moris@gmail.com','1342AM',15 );
    INSERT INTO Abonnement VALUES(13,'Guichet','2022-07-09 08:30:00','2023-01-02','2024-05-24','adnane.momo@gmail.com','1342AM',16 );

    INSERT INTO Reservation
    VALUES (8,'Automate','2022-05-16 17:00:00','2022-05-18','2022-06-18','boris.lefoll1@gmail.com',2,'8462AM');
    INSERT INTO Reservation
    VALUES (9,'Automate','2022-05-16 17:00:00','2022-05-18','2022-05-19','errazine.adnane@gmail',3,'9859BT');
    INSERT INTO Reservation
    VALUES (10,'Automate','2022-01-16 17:00:00','2022-02-18','2022-07-18','erickmwatanabek@gmail.com',4,'6948XR');
