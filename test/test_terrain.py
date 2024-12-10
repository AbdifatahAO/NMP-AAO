
import unittest
import xmlrunner

from Terrain import Terrain, Case

class TestTerrain(unittest.TestCase):

    def test_chargement(self):
        terrain = Terrain()
        ##terrain.charger("test_terrain.txt")

        self.assertEqual(terrain.largeur, 4)
        self.assertEqual(terrain.hauteur, 3)

        self.assertEqual(terrain.cases[0][0], Case.ENTREE)
        self.assertEqual(terrain.cases[0][1], Case.VIDE)
        self.assertEqual(terrain.cases[0][3], Case.CLIENT)
        self.assertEqual(terrain.cases[1][1], Case.OBSTACLE)
        self.assertEqual(terrain.cases[2][0], Case.CLIENT)
        self.assertEqual(terrain.cases[2][3], Case.ENTREE)


    def test_accesseur(self):
        t = Terrain()
        t.cases = [
                [Case.ENTREE, Case.VIDE, Case.VIDE],
                [Case.CLIENT, Case.CLIENT, Case.CLIENT],
        ]
        self.assertEqual(t[0][0], Case.ENTREE)
        self.assertEqual(t[0][1], Case.VIDE)
        self.assertEqual(t[1][2], Case.CLIENT)

if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="test-reports"))

