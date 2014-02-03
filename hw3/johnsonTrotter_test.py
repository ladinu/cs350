import unittest
from johnsonTrotter import *

class JohnsonTrotter(unittest.TestCase):

   def test_empty_Permutation(self):
      pl = Permutation()
      self.assertEqual(pl.array, [])
      self.assertEqual(pl.length, 0)

   def test_Permutation_push(self):
      pl = Permutation()
      self.assertEqual(pl.array, [])
      self.assertEqual(pl.length, 0)
      pl.push(Element(1, LEFT))
      self.assertEqual(pl.length, 1)

   def test_Permutation_isMobile_1(self):
      pl = Permutation()
      pl.push(Element(1, LEFT))
      self.assertFalse(pl.isMobile(0))

   def test_Permutation_isMobile_2(self):
      pl = Permutation()
      pl.push(Element(1, RIGHT))
      self.assertFalse(pl.isMobile(0))

   def test_Permutation_isMobile_3(self):
      pl = Permutation()
      pl.push(Element(1, RIGHT))
      pl.push(Element(2, LEFT))
      self.assertTrue(pl.isMobile(1))

   def test_Permutation_isMobile_4(self):
      pl = Permutation()
      pl.push(Element(1, RIGHT))
      pl.push(Element(2, RIGHT))
      self.assertFalse(pl.isMobile(1))

   def test_Permutation_largestMobile_empty(self):
      pl = Permutation()
      lm = pl.largestMobile()
      self.assertEqual(lm, -1)

   def test_Permutation_largestMobile_1(self):
      pl = Permutation()
      pl.push(Element(1, RIGHT))
      lm = pl.largestMobile()
      self.assertEqual(lm, -1)

   def test_Permutation_largestMobile_2(self):
      pl = Permutation()
      pl.push(Element(1, RIGHT))
      pl.push(Element(2, RIGHT))
      self.assertEqual(pl.largestMobile(), -1)

   def test_Permutation_swap(self):
      pl = Permutation()
      pl.push(Element(1, RIGHT))
      pl.push(Element(2, RIGHT))

      self.assertEqual(pl.get(1).value, 2)
      pl.swap(0, 1)
      self.assertEqual(pl.get(1).value, 1)

   def test_Permutation_reverse(self):
      pl = Permutation()
      pl.push(Element(1, RIGHT))
      pl.push(Element(2, RIGHT))
      pl.reverseElements(0)
      self.assertEqual(pl.get(1).direction, LEFT)

   def test_Permutation_hasMobileElement(self):
      pl = Permutation()
      pl.push(Element(1, RIGHT))
      pl.push(Element(2, LEFT))
      self.assertTrue(pl.hasMobileElement())
      pl.get(1).reverseDirection()
      self.assertFalse(pl.hasMobileElement())

   def test_Permutation_get(self):
      pl = Permutation()
      pl.push(Element(1, RIGHT))
      self.assertEqual(pl.get(0).value, 1)

   def test_Permutation_pushTo_empty(self):
      pl = Permutation()
      perms = []
      pl.pushTo(perms)
      self.assertEqual(perms[0], '')

   def test_Permutation_pushTo_1(self):
      pl = Permutation()
      pl.push(Element(1, RIGHT))
      perms = []
      pl.pushTo(perms)
      self.assertEqual(len(perms), 1)
      self.assertEqual(perms[0], '1')

   def test_Permutation_pushTo_2(self):
      pl = Permutation()
      perms = []
      pl.push(Element(1, RIGHT))
      pl.pushTo(perms)
      pl.push(Element(2, LEFT))
      pl.pushTo(perms)
      self.assertEqual(len(perms), 2)

      self.assertEqual(perms[0], '1')
      self.assertEqual(perms[1], '12')

   def test_Element(self):
      e = Element(1, LEFT)
      self.assertEqual(e.value, 1)
      e = Element(1, RIGHT)
      self.assertEqual(e.direction, RIGHT)

   def test_Element_reverse(self):
      e = Element(1, RIGHT)
      self.assertEqual(e.direction, RIGHT)
      e.reverseDirection()
      self.assertEqual(e.direction, LEFT)

   def test_initPerm_empty(self):
      pl = init_perm(0)
      self.assertEqual(pl.length, 0)

   def test_initPerm_one(self):
      pl = init_perm(1)
      self.assertEqual(pl.length, 1)

   def test_initPerm_two(self):
      pl = init_perm(2)
      self.assertEqual(pl.length, 2)

   def test_JohnsonTrotter_empty(self):
      permutations = johnsonTrotter(0)
      self.assertEqual(permutations, [''])
      permutations = johnsonTrotter(-1)
      self.assertEqual(permutations, [''])

   def test_JohnsonTrotter_1(self):
      permutations = johnsonTrotter(1)
      self.assertEqual(len(permutations), 1)

   def test_JohnsonTrotter_2(self):
      permutations = johnsonTrotter(2)
      self.assertEqual(len(permutations), 2)

   def test_JohnsonTrotter_3(self):
      permutations = johnsonTrotter(3)
      self.assertEqual(len(permutations), 6)

if __name__ == '__main__':
    unittest.main()
