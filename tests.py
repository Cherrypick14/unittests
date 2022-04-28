import unittest

from sum import sum_numbers


class TestStringMethods(unittest.TestCase):

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_upper(self):
        self.assertEqual('foo'.upper(),'FOO')

    def test_split(self):
        s= 'Hello skaehub'
        self.assertEqual(s.split(), ['Hello','skaehub'])
        with self.assertRaises(TypeError):
            s.split(4)
    def test_sum(self):
        self.assertTrue(sum_numbers(3,4), 7)
        self.assertTrue(sum_numbers(5.0,2), 7)
        self.assertTrue(sum_numbers(6,-4), 2)
       

if __name__ =='__main__':
    unittest.main()