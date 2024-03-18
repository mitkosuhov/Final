def get_filtered_incomes(date=None, type_of_income=None, amount_min=None, amount_max=None):
    session = Session()
    query = session.query(Income)
    if date:
        query = query.filter(Income.date == date)
    if type_of_income:
        query = query.filter(Income.type_of_income == type_of_income)
    if amount_min is not None:
        query = query.filter(Income.amount >= amount_min)
    if amount_max is not None:
        query = query.filter(Income.amount <= amount_max)
    return query.all()

def get_filtered_expenses(date=None, type_of_expense=None, amount_min=None, amount_max=None):
    session = Session()
    query = session.query(Expense)
    if date:
        query = query.filter(Expense.date == date)
    if type_of_expense:
        query = query.filter(Expense.type_of_expense == type_of_expense)
    if amount_min is not None:
        query = query.filter(Expense.amount >= amount_min)
    if amount_max is not None:
        query = query.filter(Expense.amount <= amount_max)
    return query.all()
