import unittest
import math


class EqualityTest(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(equality(2, 3, 7), "NO")
        self.assertEqual(equality(0.1, 0.2, 0.3), "YES")
        self.assertEqual(equality(-2, 5, 3), "YES")
        self.assertEqual(equality(0, 0, 0), "YES")

    def test_validate(self):
        with self.assertRaises(TypeError):
            equality("a", 3, 5)

        with self.assertRaises(TypeError):
            equality(3, "b", 5)
        
        with self.assertRaises(TypeError):
            equality("2", 5, 7)


def equality(a, b, c):
    for i in a, b, c:
        if not isinstance(i, (int, float)):
            raise TypeError("Ожидается int или float.")
        
    return 'YES' if math.isclose(a + b, c, rel_tol=1e-8) else 'NO'


if __name__ == "__main__":
    a = float(input())
    b = float(input())
    c = float(input())
    
    print(equality(a, b, c))
   