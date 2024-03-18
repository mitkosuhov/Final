import unittest
from datetime import datetime
from Finalproject import (
    add_expense,
    add_income,
    show_expense,
    show_income,
    balance,
    visualize_income_expense,
    find_expense_count_daily,
    update_income,
    update_expense,
    delete_income,
    delete_expense,
    visualize_income_expense1,Expense,Session,Income
)
from unittest.mock import patch ,  Mock
from io import StringIO
import tempfile
import os

class TestFinanceFunctions(unittest.TestCase):


        
    def test_add_expense(self):
    # Тестове за функцията add_expense
        amount = 100.0
        description = "Test expense"
        date = datetime.now()
        type_of_expense = "Test type"

        # Извикваме функцията за добавяне на разход
        add_expense(amount, description, date, type_of_expense)

        # Проверяваме дали разходът е добавен успешно към базата данни
        session = Session()  # Предполагаме, че имате променлива Session за връзка с базата данни
        added_expense = session.query(Expense).filter_by(description=description).first()
        self.assertIsNotNone(added_expense)


    def test_add_income(self):
        # Тестове за функцията add_income
        amount = 100.0
        description = "Test expense"
        date = datetime.now()
        type_of_income = "Test type"

        # Извикваме функцията за добавяне на разход
        add_income(amount, description, date, type_of_income)

        # Проверяваме дали разходът е добавен успешно към базата данни
        session = Session()  # Предполагаме, че имате променлива Session за връзка с базата данни
        added_income = session.query(Income).filter_by(description=description).first()
        self.assertIsNotNone(added_income)
        
    def test_show_income(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            show_income()

    # Проверка на изхода
        expected_output = "Expected output here"  # Предполагаме, че имате очакван изход
        self.assertEqual(fake_out.getvalue().strip(), expected_output)

    def test_balance(self):
        expected_balance = 10  # или някаква друга положителна стойност
        actual_balance = balance()
        self.assertGreater(actual_balance, expected_balance)
        

    def test_find_expense_count_daily(self):
        expected_days = 7600 // 100
        actual_days = find_expense_count_daily(100)
        self.assertEqual(actual_days, expected_days)

    def test_update_income(self):
        income_id = 1
        amount = 100.0
        description = "New Description"
        date = datetime.now().date()
        type_of_income = "New Type"

        update_income(income_id, amount, description, date, type_of_income)

        self.assertTrue(True)

    def test_update_expense(self):
        expense_id = 1
        amount = 100.0
        description = "New Description"
        date = datetime.now().date()
        type_of_expense = "New Type"

        update_expense(expense_id, amount, description, date, type_of_expense)
        
    def test_delete_income(self):
        
        income_id_to_delete = 1  
        delete_income(income_id_to_delete)

    def test_delete_expense(self):
        
        expense_id_to_delete = 1  
        delete_expense(expense_id_to_delete)

    def test_visualize_income_expense1(self):
        with patch('matplotlib.pyplot.show') as mock_show:
            visualize_income_expense1()
            # Проверяваме дали функцията show на pyplot е била извикана
            mock_show.assert_called_once()

    
        


if __name__ == '__main__':
    unittest.main()