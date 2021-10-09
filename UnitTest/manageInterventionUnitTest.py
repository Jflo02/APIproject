import unittest
from Domain.manageIntervention import ManageIntervention

class ManageInterventionTest(unittest.TestCase):
    def test_recupererInterventions(self):
        inter1=ManageIntervention("../Database/EasySav.db")
        self.assertTrue(inter1.recupererInterventions())

    def test_interventionRecupererById(self):
        inter1=ManageIntervention("../Database/EasySav.db")
        self.assertEqual(inter1.interventionRecupererById(1),{1: {'Lieu': None,'dateIntervention': '20/05/1999','numeroEmploye': 1,'numeroSerie': 'C7890'}})

if __name__ == '__main__':
    unittest.main()
