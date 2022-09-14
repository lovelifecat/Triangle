import unittest
import triangle

class TestTriangle(unittest.TestCase):
    def test_classify_Scalene(self):
        a = 3
        b = 4
        c = 5
        self.assertEqual(triangle.classify(a, b, c), 'scalene')


    def test_classify_isosceles(self):
        a = 3
        b = 3
        c = 4
        self.assertEqual(triangle.classify(a, b, c), 'isosceles')


    def test_classify_Equilateral(self):
        a = 3
        b = 3
        c = 3
        self.assertEqual(triangle.classify(a, b, c), 'Equilateral')

    def test_classify_none(self):
        a = 1
        b = 2
        c = 5
        self.assertEqual(triangle.classify(a, b, c), 'none')



if __name__ == "__main__":
        unittest.main()