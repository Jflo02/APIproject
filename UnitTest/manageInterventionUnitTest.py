import unittest
from Domain.manageIntervention import ManageIntervention

class ManageInterventionTest(unittest.TestCase):
    def test_recupererInterventions(self):
        inter1=ManageIntervention("../Database/EasySav.db")
        self.assertTrue(inter1.recupererInterventions())

    def test_interventionRecupererById(self):
        inter1=ManageIntervention("../Database/EasySav.db")
        self.assertEqual(inter1.interventionRecupererById(1),{1: {'Lieu': None,'dateIntervention': '20/05/1999','numeroEmploye': 1,'numeroSerie': 'C7890'}})

    def test_interventionAjouter(self):
        #Arrange
        inter1=ManageIntervention("../Database/EasySav.db")
        longueurTableInterventionAvantAjout = len(inter1.recupererInterventions())

        #Act
        inter1.interventionAjouter("25/05/2022", "Fake-City-For-Unit-test", "AZERTY1234", 1)

        #Assert
        longueurTableInterventionApresAjout = len(inter1.recupererInterventions())
        self.assertGreater(longueurTableInterventionApresAjout, longueurTableInterventionAvantAjout)

    def test_annulerIntervention(self):
        #Arrange
        inter1=ManageIntervention("../Database/EasySav.db")
        longueurTableInterventionAvantSupp = len(inter1.recupererInterventions())

        #Act
        in
        self.assertTrue(inter1.interventionSupprimer(1))


if __name__ == '__main__':
    unittest.main()
