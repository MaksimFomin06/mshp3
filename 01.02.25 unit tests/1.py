import unittest

def summa(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Ожидается int или float.")
    
    return a + b


class FuncTest(unittest.TestCase):
    def test_true_addition(self):
        self.assertEqual(summa(6, 7), 13)
        self.assertEqual(summa(23, 56), 79)
        self.assertEqual(summa(2, 3), 5)
        self.assertEqual(summa(-2, 3), 1)
        self.assertEqual(summa(0, 0), 0)

    def test_entered_number(self):
        with self.assertRaises(TypeError):
            summa("sds", "ac")
        
        with self.assertRaises(TypeError):
            summa(None, "23")

        with self.assertRaises(TypeError):
            summa("0", 3)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(summa(a, b))
