from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime , func , Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime , date
import matplotlib.pyplot as plt
from enum import Enum as PythonEnum
import numpy as np

# Създаване на връзка към базата данни SQLite
engine = create_engine('sqlite:///finance.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)

# Дефиниране на модел за приходи
class Income(Base):
    __tablename__ = 'incomes'
    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    date = Column(DateTime, default=datetime.now)
    description  = Column(String)
    type_of_income = Column(String)

# Дефиниране на модел за разходи
class Expense(Base):
    __tablename__ = 'expenses'
    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    date = Column(DateTime, default=datetime.now)
    description = Column(String)
    type_of_expense = Column(String)
     
# Създаване на таблиците в базата данни
Base.metadata.create_all(engine)

def add_expense(x,y,z,q):
                # Добавяне на разход
                session = Session()
                new_expense = Expense(amount=x , description=y , date=z ,type_of_expense =q)
                session.add(new_expense)
                session.commit()

def add_income(x,y,z,q):
            # Добавяне на приход
                session = Session()
                new_income = Income(amount=x, description=y , date =z , type_of_income =q)
                session.add(new_income)
                session.commit()

def show_expense():
            # Преглед на всички разходи
                session = Session()
                expenses = session.query(Expense).all()
                for expense in expenses:
                    print(f"ID:{expense.id} Expense: {expense.description}, Amount: {expense.amount}, Date: {expense.date} ,Type :{expense.type_of_expense}")
def show_income():
            # Преглед на всички приходи
                session = Session()
                incomes = session.query(Income).all()
                for income in incomes:
                    print(f"ID:{income.id}  Income: {income.description}, Amount: {income.amount}, Date: {income.date} , Type :{income.type_of_income}")
def balance():
            session = Session()
            total_income = session.query(func.sum(Income.amount)).scalar() or 0
            total_expense = session.query(func.sum(Expense.amount)).scalar() or 0
            balance = total_income - total_expense
            print(f"Balance: {balance}")
            session.commit()

def visualize_income_expense():
    session = Session()

    # Групиране на приходите по месеци и години
    income_data = session.query(func.strftime("%Y-%m", Income.date), func.sum(Income.amount)).group_by(func.strftime("%Y-%m", Income.date)).all()
    income_months, income_amounts = zip(*income_data)

    # Групиране на разходите по месеци и години
    expense_data = session.query(func.strftime("%Y-%m", Expense.date), func.sum(Expense.amount)).group_by(func.strftime("%Y-%m", Expense.date)).all()
    expense_months, expense_amounts = zip(*expense_data)

    plt.figure(figsize=(10, 5))

    # Създаване на стълбова диаграма за приходите
    plt.subplot(1, 2, 1)
    x = np.arange(len(income_months))
    plt.bar(x, income_amounts)
    plt.xticks(x, income_months, rotation=45)
    plt.xlabel('Месец и година')
    plt.ylabel('Сума на приходите')
    plt.title('Приходи по месеци')

    # Създаване на стълбова диаграма за разходите
    plt.subplot(1, 2, 2)
    x = np.arange(len(expense_months))
    plt.bar(x, expense_amounts)
    plt.xticks(x, expense_months, rotation=45)
    plt.xlabel('Месец и година')
    plt.ylabel('Сума на разходите')
    plt.title('Разходи по месеци')

    plt.tight_layout()
    plt.show()

def find_expense_count_daily(x):
    session = Session()
    total_income = session.query(func.sum(Income.amount)).scalar() or 0
    total_expense = session.query(func.sum(Expense.amount)).scalar() or 0
    balance = total_income - total_expense
    days_left = balance // x
    print(f"Вашия биджет {x} ще стигне за {days_left} дена")
    session.commit()
def update_income(income_id, amount=None, description=None, date=None, type_of_income=None):
    session = Session()
    income = session.query(Income).filter_by(id=income_id).first()
    if income:
        if amount is not None:
            income.amount = amount
        if source:
            income.description = description
        if date:
            income.date = date
        if type_of_income:
            income.type_of_income = type_of_income
        session.commit()
        print("Income updated successfully!")
    else:
        print("Income with the specified ID not found.")
        return
def update_expense(expense_id, amount=None, description=None, date=None, type_of_expense=None):
    session = Session()
    expense = session.query(Expense).filter_by(id=expense_id).first()
    if expense:
        if amount is not None:
            expense.amount = amount
        if description:
            expense.description = description
        if date:
            expense.date = date
        if type_of_expense:
            expense.type_of_expense = type_of_expense
        session.commit()
        print("Expense updated successfully!")
    else:
        print("Expense with the specified ID not found.")
        return
def delete_income(income_id):
    session = Session()
    income = session.query(Income).filter_by(id=income_id).first()
    if income:
        session.delete(income)
        session.commit()
        print("Income deleted successfully!")
    else:
        print("Income with the specified ID not found.")
        return
def delete_expense(expense_id):
    session = Session()
    expense = session.query(Expense).filter_by(id=expense_id).first()
    if expense:
        session.delete(expense)
        session.commit()
        print("Expense deleted successfully!")
    else:
        print("Expense with the specified ID not found.")
        return
def visualize_income_expense1():
    session = Session()
    
    # Групиране на приходите по тип
    income_data = session.query(Income.type_of_income, func.sum(Income.amount)).group_by(Income.type_of_income).all()
    income_types, income_amounts = zip(*income_data)
    
    # Групиране на разходите по тип
    expense_data = session.query(Expense.type_of_expense, func.sum(Expense.amount)).group_by(Expense.type_of_expense).all()
    expense_types, expense_amounts = zip(*expense_data)
    
    # Създаване на кръгов график за разходите
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.pie(expense_amounts, labels=expense_types, autopct='%1.1f%%', startangle=140)
    plt.title('Разходи по тип')
    
    # Създаване на кръгов график за приходите
    plt.subplot(1, 2, 2)
    plt.pie(income_amounts, labels=income_types, autopct='%1.1f%%', startangle=140)
    plt.title('Приходи по тип')

    plt.tight_layout()
    plt.show()



if __name__ == "__main__":
    while True :
        menu_direction = input('Menu : \n 1)Check ballans \n 2)Add income \n 3)Add expense \n 4)Statistics of your wallet \n 5)Edit or delete \n 9)Exit')
        if menu_direction == '1':
                 balance()
        elif menu_direction =='2':
                amount_add = input('Enter amount of income:')
                source_add = input('Enter a description of the income :') 
                date_add = input("Enter a data of income in format  'DD-MM-YYYY': ")
                date_ = None
                add_type_of_income = input('Enter a type of income :')
                try:
                    date_ = datetime.strptime(date_add, '%d-%m-%Y').date()
                    amount_add = float(amount_add)
                    
                except ValueError:
                        print(f'Wrong format')      
                isinstance(amount_add, float) and isinstance(source_add, str) and isinstance(add_type_of_income, str)
                add_income(amount_add,source_add,date_,add_type_of_income)
                    
        elif menu_direction =='3':
                expense_add = input('Enter amount of expense:') 
                source_add = input('Enter a source of expense :') 
                date_add = input("Enter a date of expense in fomrat 'DD-MM-YYYY': ")
                date_ = None      
                add_type_of_expense = input('Enter a type of expense :')           
                try:
                    date_ = datetime.strptime(date_add, '%d-%m-%Y').date()
                    expense_add = float(expense_add)
                except ValueError:
                    print('Wrong format')  

                if isinstance(expense_add, float) and isinstance(source_add, str) and isinstance(add_type_of_expense, str) :
                    add_expense(expense_add, source_add, date_ ,add_type_of_expense)       
                
        elif menu_direction == '4':
                while True :
                    menu_direction_4  = input('1)See your incoms\n 2)See your expenses\n 3)See grapic of your wallet\n 4)Calculate funchio')
                    if menu_direction_4 == '1':
                        show_income()
                    elif menu_direction_4 =='2':
                            show_expense()
                    elif menu_direction_4 == '3':        
                        visualize_income_expense1()
                    elif menu_direction_4 == '4':
                           daily_expence = float(input('Add daily expence'))
                           find_expense_count_daily(daily_expence)    
                    elif menu_direction_4 =='5':
                          visualize_income_expense()
                                                
                    else:
                           break    
        elif menu_direction =='5':
              while True :
                    menu_direction_5 = input('1) Edit income\n 2)Edint Expense \n3)Delete income \n 4)Delete expense')
                    if menu_direction_5 =="1":
                          show_income()
                          income_id = int(input("Enter the ID of the income you want to edit: "))
                          amount = float(input("Enter the new amount: "))
                          source = input("Enter the new source: ")
                          date_str = input("Enter the new date (format: DD-MM-YYYY): ")
                          date_income = datetime.strptime(date_str, '%d-%m-%Y').date()
                          type_of_income = input("Enter the new type of income: ")
                          update_income(income_id, amount, source, date_income, type_of_income)

                    elif menu_direction_5 =='2':
                          show_expense()                        
                          expense_id = int(input("Enter the ID of the expense you want to edit: "))
                          amount = float(input("Enter the new amount: "))
                          description = input("Enter the new description: ")
                          date_str = input("Enter the new date (format: DD-MM-YYYY): ")
                          date_expense = datetime.strptime(date_str, '%d-%m-%Y').date()
                          type_of_expense = input("Enter the new type of expense: ")
                          update_expense(expense_id, amount, description, date_expense, type_of_expense)
                    elif menu_direction_5 =='3':
                          show_income()
                          income_id = int(input("Enter the ID of the income you want to delete: "))
                          delete_income(income_id)

                    elif menu_direction_5=='4':
                          show_expense()  
                          expense_id = int(input("Enter the ID of the expense you want to delete: ")) 
                          delete_expense(expense_id)         
                    else:
                          print('Error')
                          break      
                                
                          

        elif menu_direction == '9':
                break        
                