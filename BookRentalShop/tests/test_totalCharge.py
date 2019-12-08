import unittest 
from BookRentalShop.main.routes import totalCharge

class TotalCharge(unittest.TestCase): 
  
    # Returns Total bill in decimal value
    
    def test_total_charge_duration_1_type_regular(self):
        duration = 1
        bookType = "regular"
        expected = 2
        tc = totalCharge(duration,bookType)
        self.assertEqual(expected, tc)

    def test_total_charge_duration_2_type_regular(self):
        duration = 2
        bookType = "RegUlar"
        expected = 2
        tc = totalCharge(duration,bookType)
        self.assertEqual(expected, tc)
    
    def test_total_charge_duration_3_type_regular(self):
        duration = 3
        bookType = "regular"
        expected = 3.5
        tc = totalCharge(duration,bookType)
        self.assertEqual(expected, tc)

    def test_total_charge_duration_1_type_novel(self):
        duration = 1
        bookType = "novel"
        expected = 4.5
        tc = totalCharge(duration,bookType)
        self.assertEqual(expected, tc)

    def test_total_charge_duration_2_type_novel(self):
        duration = 2
        bookType = "novel"
        expected = 4.5
        tc = totalCharge(duration,bookType)
        self.assertEqual(expected, tc)

    def test_total_charge_duration_3_type_novel(self):
        duration = 3
        bookType = "novel"
        expected = 6
        tc = totalCharge(duration,bookType)
        self.assertEqual(expected, tc)

    def test_total_charge_duration_56_type_novel(self):
        duration = 56
        bookType = "novel"
        expected = 85.5
        tc = totalCharge(duration,bookType)
        self.assertEqual(expected, tc)

    def test_total_charge_duration_1_type_fiction(self):
        duration = 1
        bookType = "fiction"
        expected = 3
        tc = totalCharge(duration,bookType)
        self.assertEqual(expected, tc)

    def test_total_charge_duration_1_type_fiction(self):
        duration = 10
        bookType = "fiction"
        expected = 30
        tc = totalCharge(duration,bookType)
        self.assertEqual(expected, tc)