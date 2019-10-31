import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
	
	def setUp(self):
		
		self.ted = Employee('ted', 'rogers', 100000)
		
	def test_give_default_raise(self):
		self.ted.give_raise()
		self.assertEqual(self.ted.salary, 105000)

	
	
	def test_give_custom_raise(self):
		self.ted.give_raise(10000)
		self.assertEqual(self.ted.salary, 110000)


unittest.main()
