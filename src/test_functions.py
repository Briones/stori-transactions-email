import unittest
import os
from functions import *

class FunctionTest(unittest.TestCase):
    def test_file_exist(self):
        file_exists = os.path.exists('../data.csv')
        self.assertTrue(file_exists)
        
    def test_file_is_not_empty(self):
        file_size = os.path.getsize('../data.csv')
        assert file_size > 0
    
    def test_calculate_total_balance(self):
        debitAmounts = [-1,-3]
        creditAmounts = [2,5]
        totalBalance = calculate_total_balance(debitAmounts, creditAmounts)[0]
        debitAverage = calculate_total_balance(debitAmounts, creditAmounts)[1]
        creditAverage = calculate_total_balance(debitAmounts, creditAmounts)[2]

        assert totalBalance == 3

    def test_calculate_debit_average(self):
        debitAmounts = [-1,-3]
        creditAmounts = [2,5]        
        debitAverage = calculate_total_balance(debitAmounts, creditAmounts)[1] 
        
        assert debitAverage == -2.0


    def test_calculate_debit_average(self):
        debitAmounts = [-1,-3]
        creditAmounts = [2,5]        
        creditAverage = calculate_total_balance(debitAmounts, creditAmounts)[2] 
        print(creditAverage)
        assert creditAverage == 3.5
        
        
        

if __name__ == '__m ain__':
    unittest.main()