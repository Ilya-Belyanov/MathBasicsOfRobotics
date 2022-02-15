import unittest

from robobase.trianglealg import *
from src.support import drawTriangles


class TestTriangleIntersections(unittest.TestCase):
    def test_not_intersect(self):
        tr_one = Triangle([Point([0, 0]), Point([1, 0]), Point([0, 1])])
        tr_two = Triangle([Point([0.7, 1]), Point([1, 1]), Point([1, 0.7])])
        tr_third = Triangle([Point([1, 0.1]), Point([1, 0.5]), Point([0.8, 0.6])])

        self.assertEqual(tr_one.isIntersection(tr_two), False)
        self.assertEqual(tr_two.isIntersection(tr_one), False)
        self.assertEqual(tr_one.isIntersection(tr_third), False)
        self.assertEqual(tr_third.isIntersection(tr_one), False)
        self.assertEqual(tr_two.isIntersection(tr_third), False)
        self.assertEqual(tr_third.isIntersection(tr_two), False)

        drawTriangles(tr_one, tr_two, tr_third)

    def test_intersect(self):
        tr_one = Triangle([Point([0, 0]), Point([1, 0]), Point([0, 1])])
        tr_two = Triangle([Point([0, 1]), Point([1, 1]), Point([1, 0])])
        tr_third = Triangle([Point([0.25, 0.25]), Point([0.75, 0.75]), Point([0.6, 0.8])])

        self.assertEqual(tr_one.isIntersection(tr_two), True)
        self.assertEqual(tr_two.isIntersection(tr_one), True)
        self.assertEqual(tr_one.isIntersection(tr_third), True)
        self.assertEqual(tr_third.isIntersection(tr_one), True)
        self.assertEqual(tr_two.isIntersection(tr_third), True)
        self.assertEqual(tr_third.isIntersection(tr_two), True)

        drawTriangles(tr_one, tr_two, tr_third)


if __name__ == '__main__':
    unittest.main()
