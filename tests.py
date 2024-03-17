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
from unittest.mock import patch
from io import StringIO
import tempfile
import os

class TestFinanceFunctions(unittest.TestCase):

    def setUp(self):
        # Инициализация на променливи или настройка на среда за тестовете, ако е необходимо
        self.maxDiff = None

    def tearDown(self):
        self.connection.close()
        

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
        
    # @patch('sys.stdout', new_callable=StringIO)
    # def test_show_expense(self, mock_stdout):
    #     # Тестове за функцията show_expense
    #     session = Session()  # Предполагаме, че имате променлива Session за връзка с базата данни
    #     expected_output = "ID:1 Expense: Test expense, Amount: 100.0, Date: 2024-03-17 ,Type :Test type\n"  # Променете съгласно вашите данни

    #     # Извикване на функцията, която ще тестваме
    #     show_expense()

    #     # Сравняване на очаквания изход със стойността, записана в mock_stdout
    #     self.assertIn(expected_output, mock_stdout.getvalue()) 

    def test_show_income(self):
        # Тестове за функцията show_income
        pass

    def test_balance(self):
        # Тестове за функцията balance
        pass

    def test_visualize_income_expense(self):
        # Тестове за функцията visualize_income_expense
        with tempfile.NamedTemporaryFile(suffix=".png") as tmpfile:
            # Извикваме функцията за визуализация
            visualize_income_expense(tmpfile.name)

            # Проверяваме дали временният файл съществува
            self.assertTrue(os.path.exists(tmpfile.name))

            # Проверяваме дали размерът на файла е ненулев
            self.assertGreater(os.path.getsize(tmpfile.name), 0)
        # Тестове за функцията visualize_income_expense
        

    def test_find_expense_count_daily(self):
        # Тестове за функцията find_expense_count_daily
        pass

    def test_update_income(self):
        # Тестове за функцията update_income
        pass

    def test_update_expense(self):
        # Тестове за функцията update_expense
        pass

    def test_delete_income(self):
        # Тестове за функцията delete_income
        pass

    def test_delete_expense(self):
        # Тестове за функцията delete_expense
        pass

    def test_visualize_income_expense1(self):
        # Тестове за функцията visualize_income_expense1
        pass

if __name__ == '__main__':
    unittest.main()