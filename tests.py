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
        # Тестове за функцията show_income
        pass

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
        
        pass

    def test_delete_expense(self):
        
        pass

    def test_visualize_income_expense1(self):
    
        pass

if __name__ == '__main__':
    unittest.main()