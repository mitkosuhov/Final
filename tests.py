import unittest
from datetime import datetime , date

from Finalproject import add_income, add_expense, balance, visualize_income_expense, find_expense_count_daily

class TestFinanceFunctions(unittest.TestCase):
    def test_add_income(self):
        test_amount = 100.0
        test_source = "Salary"
        test_date = datetime.now().date()
        test_type = "Regular"

        # Извикване на функцията за добавяне на приходи
        add_income(test_amount, test_source, test_date, test_type)
       

    def test_add_expense(self):
        test_amount = 100.0
        test_source = "Food"
        test_date = datetime.now().date()
        test_type = "Regular"

        # Извикване на функцията за добавяне на приходи
        add_expense(test_amount, test_source, test_date, test_type)
        

    def test_balance(self):
       
        test_amount = 100
        test_source = "Salary"
        test_date = datetime.now().date()
        test_type = "Regular"
        add_income(test_amount, test_source, test_date, test_type)

       
        result = balance()

   
        self.assertGreaterEqual(result, 0, "Error: Balance is negative")
        

    # def test_visualize_income_expense(self):
        

    # def test_find_expense_count_daily(self):
        

if __name__ == '__main__':
    unittest.main()





    



   