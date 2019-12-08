import unittest 
from BookRentalShop.main.routes import totalCharge  

class TotalCharge(unittest.TestCase): 
  
    # Returns True or False.  
    def test_total_charge_duration5(self):
    	duration = 5
    	expected = 5
    	tc = totalCharge(duration)
    	self.assertEqual(expected, tc) 

    def test_total_charge_duration3(self):
    	duration = 3
    	expected = 3
    	tc = totalCharge(duration)
    	self.assertEqual(expected, tc)

    def test_total_charge_duration30(self):
    	duration = 30
    	expected = 30
    	tc = totalCharge(duration)
    	self.assertEqual(expected, tc)