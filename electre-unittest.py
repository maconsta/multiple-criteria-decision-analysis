import unittest
from methods.topsis import Electre
from core.core import Criterion, Alternative, DecisionMatrix


class ElectreTest(unittest.TestCase):
    def runTest(self):
        c1 = Criterion("c1", "max")
        c2 = Criterion("c2", "max")
        c3 = Criterion("c3", "max")
        c4 = Criterion("c4", "max")
        c5 = Criterion("c5", "max")
        c6 = Criterion("c6", "max")
        criteria = [c1, c2, c3, c4, c5, c6]

        a1 = Alternative("a1", [1350, 1850, 7.5, 2.58, 93.5, 0.045])
        a2 = Alternative("a2", [1680, 1650, 8.5, 3.75, 95.3, 0.068])
        a3 = Alternative("a3", [1560, 1950, 6.5, 4.86, 88.6, 0.095])
        a4 = Alternative("a4", [1470, 1850, 9.5, 3.16, 98.4, 0.072])
        alternatives = [a1, a2, a3, a4]

        dm = DecisionMatrix(criteria, alternatives)
        weights = [0.2336, 0.1652, 0.3355, 0.1021, 0.0424, 0.1212]

        el = Electre(dm, weights)

        #ADD TESTS 
