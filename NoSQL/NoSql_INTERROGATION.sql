-- Nombre des zones. 
select distinct count(zone->>'nomzone') as nombre_des_zones
from Parking;
--Selection des zones et leurs prix respectivement.
select distinct zone->>'nomzone' as nombre_des_zones,cast(zone->>'prix' as integer) as prix
from Parking;
--prix moyen de toutes les zones
select distinct avg(cast(zone->>'prix' as integer)) as Moyenne
from Parking;
-- nombre des places plein air dans chaque zone
select zone->>'nomzone' as zone,sum(max_place_plein_air) as nombre_place_plein_air
from Parking
group by zone->>'nomzone'

-- nombre des places plein air dans chaque zone
select zone->>'nomzone' as zone,sum(max_place_couvert) as nombre_place_plein_air
from Parking
group by zone->>'nomzone'
--nombre total des place par zone
select P.zone->>'nomzone' as zone, sum((select sum(nb) 
from (values(P.max_place_plein_air),(P.max_place_couvert)) as maxplaces(nb))) as nombre_total
from Parking P
group by P.zone->>'nomzone'


-- zone avec plus de places couvertes que pleines.
select zone->>'nomzone'as zone, zone->>'prix' as prix,max_place_plein_air,max_place_couvert 
from Parking
where max_place_plein_air > max_place_couvert


--nombre de vehicule pour chaque abonne
select a.iduser,a.nom,a.prenom,count(v.immatriculation) as nombre_vehicule
from abonne a, JSON_TO_RECORDSET(a.vehicule) v (immatriculation varchar,type TEXT)
group by a.iduser,a.nom,a.prenom
--nombre de vehicule pour chaque occasionnel // à vérifier
select a.iduser,a.mail,count(v.immatriculation) as nombre_vehicule
from occasionnel a, JSON_TO_RECORDSET(a.vehicule) v (immatriculation varchar,type TEXT)
group by a.iduser,a.mail


--nombre de vehicule de type "deux roues" pour les abonnes
select count(v->>'type') as nombre_DeuxRoues
from abonne a,JSON_ARRAY_ELEMENTS(a.vehicule) v
where v->>'type'='Deux roues'
--nombre de vehicule de type "Camion" pour les abonnes
select count(v->>'type') as nombre_Camion
from abonne a,JSON_ARRAY_ELEMENTS(a.vehicule) v
where v->>'type'='Camion'
--nombre de vehicule de type "Vehicule simple" pour les abonnes
select count(v->>'type') as nombre_vehiculeSimple
from abonne a,JSON_ARRAY_ELEMENTS(a.vehicule) v
where v->>'type'='Vehicule simple'
--nombre de vehicule de type "deux roues" pour les occasionnels
select count(v->>'type') as nombre_DeuxRoues
from abonne a,JSON_ARRAY_ELEMENTS(a.vehicule) v
where v->>'type'='Deux roues'
--nombre de vehicule de type "Camion" pour les occasionnels
select count(v->>'type') as nombre_Camion
from occasionnel a,JSON_ARRAY_ELEMENTS(a.vehicule) v
where v->>'type'='Camion'
--nombre de vehicule de type "Vehicule simple" pour les occasionnels
select count(v->>'type') as nombre_vehiculeSimple
from occasionnel a,JSON_ARRAY_ELEMENTS(a.vehicule) v
where v->>'type'='Vehicule simple'

--l'occasionnel avec max de vehicules
