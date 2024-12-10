import unittest
import xmlrunner
from Terrain import Terrain, Case
from Reseau import Reseau
from StrategieReseau import StrategieReseauAuto

class StrategieReseau:
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        return -1, {}, []

class StrategieReseauManuelle(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        # TODO
        return -1, {}, []

class StrategieReseauAuto(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        # TODO
        return -1, {}, []
#
class TestStrategiesReseau(unittest.TestCase):

    def test_config_auto(self):
        r = Reseau()
        r.set_strategie(StrategieReseauAuto())

        t = Terrain()
        t.charger("terrains/t1.txt")
        r.configurer(t)

        self.assertTrue(r.valider_reseau())
        self.assertTrue(r.valider_distribution(t))

        t.charger("terrains/t2.txt")
        r.configurer(t)

        self.assertTrue(r.valider_reseau())
        self.assertTrue(r.valider_distribution(t))



