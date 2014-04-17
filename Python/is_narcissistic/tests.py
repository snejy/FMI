import unittest

from solution import is_narcissistic
class TestNarcissistic(unittest.TestCase):

    def test_is_narcissistic(self):
        self.assertFalse(is_narcissistic('10'))

        self.assertTrue(is_narcissistic('223', 4))

        self.assertTrue(is_narcissistic('0'))

        self.assertTrue(is_narcissistic('1'))

        self.assertTrue(is_narcissistic('54748'))

        self.assertTrue(is_narcissistic('5A07C', 16))

        self.assertTrue(is_narcissistic('13579', 16))

        self.assertTrue(is_narcissistic('124030', 5))

        self.assertTrue(is_narcissistic('570', 9))

        self.assertFalse(is_narcissistic('103'))

        self.assertTrue(is_narcissistic('122', 3))

    def test_is_narcissistic2(self):
 
        self.assertFalse(is_narcissistic('999'))
 
        self.assertTrue(is_narcissistic('0'))
 
        self.assertTrue(is_narcissistic('407'))
 
        self.assertFalse(is_narcissistic('470'))
 
        self.assertFalse(is_narcissistic('ZZF02', 36))
 
        self.assertTrue(is_narcissistic('223', 4))
 
        self.assertTrue(is_narcissistic('115132219018763992565095597973971522400'))
 
        self.assertTrue(is_narcissistic('122', 3))
 
        self.assertTrue(is_narcissistic('124031', 5))
 
        self.assertTrue(is_narcissistic('12205', 7))
 
        self.assertTrue(is_narcissistic('45', 9))
 
        self.assertTrue(is_narcissistic('12344AA12A721803422912A8AA4963568083A268456A4', 11))
 
        self.assertTrue(is_narcissistic('15079346A6B3B14BB56B395898B96629A8B01515344B4B0714B', 12))

if __name__ == '__main__':
    unittest.main()