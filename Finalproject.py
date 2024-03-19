from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime , func 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime 
import matplotlib.pyplot as plt
import numpy as np
from sqlalchemy import desc
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
            return balance

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
    plt.xlabel('Month and year')
    plt.ylabel('Sum of incomes')
    plt.title('Incomes by month')

    # Създаване на стълбова диаграма за разходите
    plt.subplot(1, 2, 2)
    x = np.arange(len(expense_months))
    plt.bar(x, expense_amounts)
    plt.xticks(x, expense_months, rotation=45)
    plt.xlabel('Month and year')
    plt.ylabel('Sum of expense')
    plt.title('Expenses by month')

    plt.tight_layout()
    plt.show()

def find_expense_count_daily(x):
    session = Session()
    total_income = session.query(func.sum(Income.amount)).scalar() or 0
    total_expense = session.query(func.sum(Expense.amount)).scalar() or 0
    balance = total_income - total_expense
    days_left = balance // x
    print(f"Your budget {x} will be enough for {days_left} days")
    session.commit()
    return days_left
def update_income(income_id, amount=None, description=None, date=None, type_of_income=None):
    session = Session()
    income = session.query(Income).filter_by(id=income_id).first()
    if income:
        if amount is not None:
            income.amount = amount
        if description is not None:
            income.description = description
        if date is not None:
            income.date = date
        if type_of_income is not None:
            income.type_of_income = type_of_income
        session.commit()
        print("Income updated successfully!")
    else:
        print("Income with the specified ID not found.")


def update_expense(expense_id, amount=None, description=None, date=None, type_of_expense=None):
    session = Session()
    expense = session.query(Expense).filter_by(id=expense_id).first()
    if expense:
        if amount is not None:
            expense.amount = amount
        if description is not None:
            expense.description = description
        if date is not None:
            expense.date = date
        if type_of_expense is not None:
            expense.type_of_expense = type_of_expense
        session.commit()
        print("Expense updated successfully!")
    else:
        print("Expense with the specified ID not found.")

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
def visualize_income_expense_2():
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
    plt.title('Type of expense')
    
    # Създаване на кръгов график за приходите
    plt.subplot(1, 2, 2)
    plt.pie(income_amounts, labels=income_types, autopct='%1.1f%%', startangle=140)
    plt.title('Type of income')
    plt.tight_layout()
    plt.show()

def get_sorted_incomes(sort_by='date'):
    session = Session()
    query = session.query(Income)
    if sort_by == 'date':
        query = query.order_by(desc(Income.date))
    elif sort_by == 'amount':
        query = query.order_by(desc(Income.amount))
    elif sort_by == 'type':
        query = query.order_by(Income.type_of_income)
    return query.all()

def get_sorted_expenses(sort_by='date'):
    session = Session()
    query = session.query(Expense)
    if sort_by == 'date':
        query = query.order_by(desc(Expense.date))
    elif sort_by == 'amount':
        query = query.order_by(desc(Expense.amount))
    elif sort_by == 'type':
        query = query.order_by(Expense.type_of_expense)
    return query.all()



if __name__ == "__main__":
    while True :
        menu_direction = input('Menu : \n 1)Check ballans \n 2)Add transaction \n 3)Statistics of your wallet \n 4)Edit or delete \n 5)Sorted data \n 9)Exit')
        if menu_direction == '1':
                 balance()
        elif menu_direction =='2':
                while True :
                      menu_direction_2 = input('Add transaction: \n 1)Add income: \n 2)Add expense: \n 3)Exit')
                      if menu_direction_2=='1':
                        amount_input = input("Enter the amount : ").strip()
                        if amount_input:
                                try:
                                    amount = float(amount_input)
                                except ValueError:
                                    print("Invalid amount format. Please enter a valid number.")
                                    continue  # Продължаваме към следващата итерация от цикъла
                        else:
                                amount = None
                        source = input("Enter the source : ")
                        date_input = input("Enter a date (format: DD-MM-YYYY): ").strip()
                        if date_input:
                                try:
                                    date_income = datetime.strptime(date_input, '%d-%m-%Y').date()
                                except ValueError:
                                    print("Invalid date format. Please enter the date in the format: DD-MM-YYYY")
                                    continue  # Продължаваме към следващата итерация от цикъла
                        else:
                                date_income = None
                        type_of_income = input("Enter the type of income : ")

                        add_income(amount, source, date_income, type_of_income)

                      elif menu_direction_2=='2':
                        amount_input = input("Enter the amount : ").strip()
                        if amount_input:
                                try:
                                    amount = float(amount_input)
                                except ValueError:
                                    print("Invalid amount format. Please enter a valid number.")
                                    continue  # Продължаваме към следващата итерация от цикъла
                        else:
                                amount = None
                        source = input("Enter the source : ")
                        date_input = input("Enter a date (format: DD-MM-YYYY): ").strip()
                        if date_input:
                                try:
                                    date_expense = datetime.strptime(date_input, '%d-%m-%Y').date()
                                except ValueError:
                                    print("Invalid date format. Please enter the date in the format: DD-MM-YYYY")
                                    continue  # Продължаваме към следващата итерация от цикъла
                        else:
                                date_expense = None
                        type_of_expense = input("Enter the type of expense : ")

                        add_expense(amount, source, date_expense, type_of_expense)
                      elif menu_direction_2=='3':
                            break
                      else:
                            print('Error')
                            continue             
                
        elif menu_direction == '3':
                while True :
                    menu_direction_4  = input('Statistics : \n1)See your incoms\n 2)See your expenses\n 3)Grapic by types\n 4)Graphyc by date \n 5)Calculate funchio\n 6)Exit')
                    if menu_direction_4 == '1':
                        show_income()
                    elif menu_direction_4 =='2':
                            show_expense()
                    elif menu_direction_4 == '3':        
                        visualize_income_expense_2()
                    elif menu_direction_4 == '4':
                           visualize_income_expense()
                           daily_expence = float(input('Add daily expence'))
                           find_expense_count_daily(daily_expence)    
                    elif menu_direction_4 =='5':
                         daily_expence = float(input('Add your daily expense :'))
                         find_expense_count_daily(daily_expence) 
                                                      
                    elif menu_direction_4=='6':
                           break    
                    else:
                          print('Error')
                          continue
        elif menu_direction =='4':
              while True :
                    menu_direction_5 = input('Edit or Delete :\n 1)Edit income\n 2)Edint Expense\n 3)Delete income\n 4)Delete expense\n 5)Exit')
                    if menu_direction_5 == "1":
                            show_income()
                            income_id = int(input("Enter the ID of the income you want to edit: "))
                            amount_input = input("Enter the new amount (leave empty to keep the old value): ").strip()
                            if amount_input:
                                try:
                                    amount = float(amount_input)
                                except ValueError:
                                    print("Invalid amount format. Please enter a valid number.")
                                    continue  # Продължаваме към следващата итерация от цикъла
                            else:
                                amount = None
                            source = input("Enter the new source (leave empty to keep the old value): ")
                            date_input = input("Enter the new date (format: DD-MM-YYYY, leave empty to keep the old value): ").strip()
                            if date_input:
                                try:
                                    date_income = datetime.strptime(date_input, '%d-%m-%Y').date()
                                except ValueError:
                                    print("Invalid date format. Please enter the date in the format: DD-MM-YYYY")
                                    continue  # Продължаваме към следващата итерация от цикъла
                            else:
                                date_income = None
                            type_of_income = input("Enter the new type of income (leave empty to keep the old value): ")

                            update_income(income_id, amount, source, date_income, type_of_income)


                    elif menu_direction_5 =='2':
                        show_expense()
                        expense_id = int(input("Enter the ID of the expense you want to edit: "))
                        amount_input = input("Enter the new amount (leave empty to keep the old value): ").strip()
                        if amount_input:
                            try:
                                amount = float(amount_input)
                            except ValueError:
                                print("Invalid amount format. Please enter a valid number.")
                                continue  # Продължаваме към следващата итерация от цикъла
                        else:
                            amount = None
                        description = input("Enter the new description (leave empty to keep the old value): ")
                        date_input = input("Enter the new date (format: DD-MM-YYYY, leave empty to keep the old value): ").strip()
                        if date_input:
                            try:
                                date_expense = datetime.strptime(date_input, '%d-%m-%Y').date()
                            except ValueError:
                                print("Invalid date format. Please enter the date in the format: DD-MM-YYYY")
                                continue  
                        else:
                            date_expense = None
                        type_of_expense = input("Enter the new type of expense (leave empty to keep the old value): ")

                        update_expense(expense_id, amount, description, date_expense, type_of_expense)


                    elif menu_direction_5 =='3':
                          show_income()
                          income_id = int(input("Enter the ID of the income you want to delete: "))
                          delete_income(income_id)

                    elif menu_direction_5=='4':
                          show_expense()  
                          expense_id = int(input("Enter the ID of the expense you want to delete: ")) 
                          delete_expense(expense_id)         
                    elif menu_direction_5 =='5':
                          break      
                    else:
                          print('Error')
                          continue    
        elif menu_direction =='5':
            while True:
                menu_direction_6 = input('Sorted statistic:\n1) Filtered and sorted incomes\n2) Filtered and sorted expenses\n3) Exit')
                if menu_direction_6 == '1':
                    # Функция за филтриране и сортиране на приходите
                    filtered_sorted_incomes = get_sorted_incomes()
                    if filtered_sorted_incomes:
                        print("Filtered and sorted incomes:")
                        for income in filtered_sorted_incomes:
                            print(f"ID: {income.id}, Income: {income.description}, Amount: {income.amount}, Date: {income.date}, Type: {income.type_of_income}")
                    else:
                        print("No incomes found matching the criteria.")
                elif menu_direction_6 == '2':
                    # Функция за филтриране и сортиране на разходите
                    filtered_sorted_expenses = get_sorted_expenses()
                    if filtered_sorted_expenses:
                        print("Filtered and sorted expenses:")
                        for expense in filtered_sorted_expenses:
                            print(f"ID: {expense.id}, Expense: {expense.description}, Amount: {expense.amount}, Date: {expense.date}, Type: {expense.type_of_expense}")
                    else:
                        print("No expenses found matching the criteria.")
                elif menu_direction_6 == '3':
                    break
                else:
                    print('Error')
                    continue

                                        
                          
        elif menu_direction == '9':
                break        
        else:
              print('Error')
              continue        