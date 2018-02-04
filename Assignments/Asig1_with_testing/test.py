from calcArea import calcArea
from find import find
from multiplication import multi
from dictionary import dic
from vow import vowels

import unittest

class TestAssignment(unittest.TestCase):

    def test_vowels(self):
        self.assertEqual(vowels('mobile'), 'mbl')

    def test_calcArea(self):
        self.assertEqual(calcArea("s",4), 16)

    def test_find(self):
        self.assertEqual(find('This is javaScript','i'), [2,5,15])


    def test_multi(self):
        self.assertEqual(multi(3), [[1],[2,4],[3,6,9]])


    def test_dic(self):
        l1 = ["ahmed", "fatma", "ibrahim"]
        d1 = {'a':['ahmed'], 'f':['fatma'],'i':['ibrahim']}
        self.assertEqual(dic(l1), d1)

if __name__ == '__main__':
    unittest.main()
