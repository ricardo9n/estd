from unittest import *
#import unittest as u
from lista_nao_ordenada import *

class ListaNaoOrdenadaTest(TestCase):
	def test_lista1(self):
		l1 = ListaNaoOrdenada()
		self.assertEqual(l1.size(),0)
		self.assertTrue(l1.is_empty())
		
		l1.add(1)
		self.assertFalse(l1.is_empty())
		self.assertEqual(l1.size(),1)

	def test_lista2(self):
		l1 = ListaNaoOrdenada()
		self.assertEqual(l1.size(),0)
		self.assertTrue(l1.is_empty())
		
		l1.add(1)
		l1.add(2)
		l1.add(3)
		l1.add(5)
		l1.add(4)
		self.assertFalse(l1.is_empty())
		self.assertEqual(l1.size(),5)

		self.assertTrue(l1.search(1))
		l1.remove(1)
		self.assertFalse(l1.search(1))

		self.assertTrue(l1.search(3))
		l1.remove(3)
		self.assertFalse(l1.search(3))

		self.assertTrue(l1.search(4))
		l1.remove(4)
		self.assertFalse(l1.search(4))

		self.assertEqual(l1.size(),2)

	def runx(self):
		self.test_lista1()
		print('run...')

	def suite():
	    """ returns all the testcases in this module """
	    return TestLoader().loadTestsFromTestCase(ListaNaoOrdenadaTest)


if __name__ == '__main__':
	#TextTestRunner().run(ListaNaoOrdenadaTest.suite())
	TextTestRunner().run(TestLoader().loadTestsFromTestCase(ListaNaoOrdenadaTest))

