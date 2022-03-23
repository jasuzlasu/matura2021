import unittest
from pierwsze import czy_jest_pierwsza


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(False, czy_jest_pierwsza(0))
        self.assertEqual(False, czy_jest_pierwsza(1))
        self.assertEqual(True, czy_jest_pierwsza(2))
        self.assertEqual(True, czy_jest_pierwsza(3))
        self.assertEqual(False, czy_jest_pierwsza(4))
        self.assertEqual(True, czy_jest_pierwsza(5))
        self.assertEqual(False, czy_jest_pierwsza(6))
        self.assertEqual(True, czy_jest_pierwsza(7))
        self.assertEqual(False, czy_jest_pierwsza(8))
        self.assertEqual(False, czy_jest_pierwsza(9))
        self.assertEqual(False, czy_jest_pierwsza(10))
        self.assertEqual(True, czy_jest_pierwsza(11))


if __name__ == '__main__':
    unittest.main()
