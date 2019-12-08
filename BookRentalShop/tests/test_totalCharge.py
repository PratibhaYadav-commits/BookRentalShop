import unittest 
from BookRentalShop.main.routes import totalCharge

class TotalCharge(unittest.TestCase): 
  
    # Returns Total bill in decimal value
    def test_total_charge_duration_1_type_regular(self):
        duration = 1
        bookType = "RegUlar"
        expected = 1.5
        tc = totalCharge(duration,bookType)
        self.assertEqual(expected, tc)

    def test_total_charge_duration_1_type_novel(self):
        duration = 1
        bookType = "Novel"
        expected = 1.5
        tc = totalCharge(duration,bookType)
        self.assertEqual(expected, tc)

    def test_total_charge_duration_1_type_fiction(self):
        duration = 1
        bookType = "Fiction"
        expected = 3
        tc = totalCharge(duration,bookType)
        self.assertEqual(expected, tc)

    def test_total_charge_duration_3_type_fiction(self):
        duration = 3
        bookType = "Fiction"
        expected = 9
        tc = totalCharge(duration,bookType)
        self.assertEqual(expected, tc)

    def test_total_charge_duration_10_type_novel(self):
        duration = 10
        bookType = "Novel"
        expected = 15
        tc = totalCharge(duration,bookType)
        self.assertEqual(expected, tc)