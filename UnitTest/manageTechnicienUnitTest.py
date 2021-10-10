import unittest

from Domain.manageTechnicien import ManageTechnicien


class ManageTechnicienTest(unittest.TestCase):


    def test_recupererInterventionsByTechnicienn(self):
        tech1=ManageTechnicien("../Database/EasySav.db")
        self.assertEqual(tech1.recupererInterventionsByTechnicien(1),{1: {'Lieu': None, 'dateIntervention': '20/05/1999', 'numeroSerie': 'C7890'}})



if __name__ == '__main__':
    unittest.main()
