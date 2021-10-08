class TypeProduit:
    def __init__(self, type, codeBarre):
        self.type = type
        self.codeBarre = codeBarre
        self.produits = {} #clé -> numeroSerie, valeur -> Objet Produit
        self.pieces = {} #clé -> reference, valeur -> Objet Piece
