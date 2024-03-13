from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime , func , Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime , date
import matplotlib.pyplot as plt
from enum import Enum as PythonEnum

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
    source = Column(String)
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
                new_income = Income(amount=x, source=y , date =z , type_of_income =q)
                session.add(new_income)
                session.commit()
def show_expense():
            # Преглед на всички разходи
                session = Session()
                expenses = session.query(Expense).all()
                for expense in expenses:
                    print(f"Expense: {expense.description}, Amount: {expense.amount}, Date: {expense.date} ,Type :{expense.type_of_expense}")
def show_income():
            # Преглед на всички приходи
                session = Session()
                incomes = session.query(Income).all()
                for income in incomes:
                    print(f"Income: {income.source}, Amount: {income.amount}, Date: {income.date} , Type :{income.type_of_income}")
def balance():
            session = Session()
            total_income = session.query(func.sum(Income.amount)).scalar() or 0
            total_expense = session.query(func.sum(Expense.amount)).scalar() or 0
            balance = total_income - total_expense
            print(f"Balance: {balance}")
            session.commit()
def visualize_income_expense():
    session = Session()
    incomes = session.query(Income.date, func.sum(Income.amount)).group_by(Income.date).all()
    expenses = session.query(Expense.date, func.sum(Expense.amount)).group_by(Expense.date).all()

    income_dates, income_amounts = zip(*incomes)
    expense_dates, expense_amounts = zip(*expenses)

    plt.figure(figsize=(10, 5))

    # Създаване на кръгов график за приходите
    plt.subplot(1, 2, 1)
    plt.pie(income_amounts, autopct='%1.1f%%', startangle=140)
    plt.title('Приходи по дата')

    # Създаване на кръгов график за разходите
    plt.subplot(1, 2, 2)
    plt.pie(expense_amounts,  autopct='%1.1f%%', startangle=140)
    plt.title('Разходи по дата')

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



if __name__ == "__main__":
    while True :
        menu_direction = input('Menu : \n 1)Check ballans \n 2)Add income \n 3)Add expense \n 4)Statistics of your wallet \n 9)Exit')
        if menu_direction == '1':
                 balance()
        elif menu_direction =='2':
                amount_add = input('Enter amount of income:')
                source_add = input('Enter a source of income :') 
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
                        visualize_income_expense()
                    elif menu_direction_4 == '4':
                           daily_expence = float(input('Add daily expence'))
                           find_expense_count_daily(daily_expence)                   
                    else:
                           break    
       


        elif menu_direction == '9':
                break        
                