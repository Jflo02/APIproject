import unittest

from Domain.manageIntervention import ManageIntervention


class ManageInterventionTest(unittest.TestCase):
    def test_recupererInterventions(self):
        inter1 = ManageIntervention("../Database/EasySav.db")
        self.assertTrue(inter1.recupererInterventions())

    def test_interventionRecupererById(self):
        inter1 = ManageIntervention("../Database/EasySav.db")
        self.assertEqual(inter1.interventionRecupererById(2), {2: {'compteRendu': 'operation good',
                                                                   'dateIntervention': '10/11/2024',
                                                                   'lieu': 'Bondues',
                                                                   'nomEmploye': 'Ringeval',
                                                                   'numeroEmploye': 8,
                                                                   'numeroSerie': 'LV1234',
                                                                   'prenomEmploye': 'Thibault',
                                                                   'reussiteIntervention': None,
                                                                   'tempsIntervention': None,
                                                                   'type': 'Lave vaisselle'}})

    def test_interventionAjouter(self):
        # Arrange
        inter1 = ManageIntervention("../Database/EasySav.db")
        longueurTableInterventionAvantAjout = len(inter1.recupererInterventions())

        # Act
        inter1.interventionAjouter("25/05/2022", "Fake-City-For-Unit-test", "LV1234", 1)

        # Assert
        longueurTableInterventionApresAjout = len(inter1.recupererInterventions())
        self.assertGreater(longueurTableInterventionApresAjout, longueurTableInterventionAvantAjout)

    # def test_annulerIntervention(self):
    #     #Arrange
    #     inter1=ManageIntervention("../Database/EasySav.db")
    #     longueurTableInterventionAvantSupp = len(inter1.recupererInterventions())
    #
    #     #Act
    #     inter1.interventionSupprimer(1)
    #
    #     #Assert
    #     longueurTableInterventionApresSupp= len(inter1.recupererInterventions())
    #     self.assertLess(longueurTableInterventionApresSupp,longueurTableInterventionAvantSupp)

    def test_interventionModifierPatch(self):
        # Arrange
        inter1 = ManageIntervention("../Database/EasySav.db")
        interventionTest = inter1.interventionRecupererById(5)
        interventionTest = interventionTest[5]
        compteRenduAvantPatch = interventionTest["compteRendu"]
        nouveauCompteRendu = compteRenduAvantPatch + "A"

        # Act
        dict = {}
        dict["numeroIntervention"] = 5
        dict["compteRendu"] = nouveauCompteRendu
        inter1.interventionModifierPatch(dict)

        # Assert
        # on recupere le nouveau numero de serie pour le comparer
        interventionTest = inter1.interventionRecupererById(5)
        self.assertEqual(interventionTest[5]["compteRendu"], nouveauCompteRendu)


if __name__ == '__main__':
    unittest.main()
