import unittest

from Domain.manageTechnicien import ManageTechnicien


class ManageTechnicienTest(unittest.TestCase):


    def test_recupererInterventionsByTechnicienn(self):
        tech1=ManageTechnicien("../Database/EasySav.db")
        self.assertEqual(tech1.recupererInterventionsByTechnicien(2),{5: {'compteRendu': 'zAAAA',
     'dateIntervention': '16/01/2021',
     'lieu': 'Wambrechies',
     'nomEmploye': 'Jaulin',
     'numeroEmploye': None,
     'numeroSerie': 'LV1234',
     'prenomEmploye': 'Florimond',
     'reussiteIntervention': None,
     'tempsIntervention': None,
     'type': '1'}})

    def test_modifierInformations(self):

        tech1=ManageTechnicien("../Database/EasySav.db")
        recupInfo=tech1.recupererInterventionsByTechnicien(2)
        recupApresModif =tech1.modifierInformations(numeroEmploye=2,numeroTelephone="0600000031")
        self.assertNotEqual(recupInfo,recupApresModif)



if __name__ == '__main__':
    unittest.main()
