from manageSqlLite import ManageSqlLite

client = [
    {"nom": "Balavoine", "prenom": "Daniel", "numeroTelephone": "0600000001", "adresse": "12 avenue de l Aziza, 59000 Lille"},
    {"nom": "Brassens", "prenom": "Georges", "numeroTelephone": "0600000002", "adresse": "58 rue de l Auvergnat, 59000 Lille"},
    {"nom": "Brel", "prenom": "Jacques", "numeroTelephone": "0600000003", "adresse": "48 allé de Vesoul, 59000 Lille"},
]

technicien = [
    {"nom": "Petit", "prenom": "Remi", "numeroTelephone": "0600000011"},
    {"nom": "Jaulin", "prenom": "Florimond", "numeroTelephone": "0600000012"},
    {"nom": "Tahon", "prenom": "Nicolas", "numeroTelephone": "0600000013"},
    {"nom": "Staelen", "prenom": "Remi", "numeroTelephone": "0600000014"},
    {"nom": "Najare", "prenom": "Aya", "numeroTelephone": "0600000015"},
    {"nom": "Vanbelle", "prenom": "Aurelien", "numeroTelephone": "0600000016"},
    {"nom": "Tonneau", "prenom": "Loic", "numeroTelephone": "0600000017"},
    {"nom": "Ringeval", "prenom": "Thibault", "numeroTelephone": "0600000018"},
    {"nom": "Bammez", "prenom": "Paul", "numeroTelephone": "0600000019"},
    {"nom": "Niffels", "prenom": "Laurent", "numeroTelephone": "0600000020"},
]

piece = [
    {"reference": "XQM59412", "designation": "pompe à eau", "stock": "100"},
    {"reference": "ABD8546", "designation": "moteur 12V", "stock": "100"},
    {"reference": "PKJ6546", "designation": "haut parleur TV", "stock": "100"},
]

typeProduit = [
    {"codeBarre": "123456789", "type": "Lave vaisselle"},
    {"codeBarre": "987654321", "type": "TV samsung"},
    {"codeBarre": "654321987", "type": "Cafetiere"},
]

produit = [
    {"numeroSerie": "LV1234", "dateAchat": "15/08/2021", "codeBarre": "123456789", "numeroClient": "1"},
    {"numeroSerie": "TV4567", "dateAchat": "19/08/2021", "codeBarre": "987654321", "numeroClient": "2"},
    {"numeroSerie": "C7890", "dateAchat": "20/09/2021", "codeBarre": "123456789", "numeroClient": "3"},
]

pieceProduit = [
    {"codeBarre": "12345678", "reference": "LV1234"},
    {"codeBarre": "987654321", "reference": "TV4567"},
    {"codeBarre": "654321987", "reference": "C7890"},
]

sql=ManageSqlLite("EasySav.db")

for dict in client:
    cmd = f"INSERT INTO Client (nom, prenom, numeroTelephone, adresse) VALUES('{dict['nom']}', '{dict['prenom']}', '{dict['numeroTelephone']}', '{dict['adresse']}')"
    sql.executeSqlCommande(cmd)
    sql.commmit()

for dict in technicien:
    cmd = f"INSERT INTO Technicien (nom, prenom, numeroTelephone) VALUES('{dict['nom']}', '{dict['prenom']}', '{dict['numeroTelephone']}')"
    sql.executeSqlCommande(cmd)
    sql.commmit()

for dict in piece:
    cmd = f"INSERT INTO Piece (reference, designation, stock) VALUES('{dict['reference']}', '{dict['designation']}', '{dict['stock']}')"
    sql.executeSqlCommande(cmd)
    sql.commmit()

for dict in typeProduit:
    cmd = f"INSERT INTO TypeProduit (codeBarre, type) VALUES('{dict['codeBarre']}', '{dict['type']}')"
    sql.executeSqlCommande(cmd)
    sql.commmit()

for dict in produit:
    cmd = f"INSERT INTO Produit (numeroSerie, dateAchat, codeBarre, numeroClient) VALUES('{dict['numeroSerie']}', '{dict['dateAchat']}', '{dict['codeBarre']}', '{dict['numeroClient']}')"
    sql.executeSqlCommande(cmd)
    sql.commmit()

for dict in pieceProduit:
    cmd = f"INSERT INTO PieceProduit (codeBarre, reference) VALUES('{dict['codeBarre']}', '{dict['reference']}')"
    sql.executeSqlCommande(cmd)
    sql.commmit()


sql.closeConnection()