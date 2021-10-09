class Intervention:
    def __init__(self, date, lieu, produitConcerne):
        self.date = date
        self.numeroIntervention = None
        self.lieu = lieu
        self.produitConcerne = produitConcerne
        self.compteRendu = None
        self.reussiteIntervention = None
        self.tempsIntervention = None
        self.piecesChangees = None

    def realiserCompteRendu(self):
        pass

    def __str__(self, ):
        pass

    def interventionRecupererAll(self):
        pass
