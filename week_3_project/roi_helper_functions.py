def get_income():
    income = 0
    try:
        rent = int(input("How much monthly rent do you receive for the property? "))
        income += rent
    except:
        pass
    try:
        laundry_machines = int(input("How much do you receive monthly from any on-site laundry machines? "))
        income += laundry_machines
    except:
        pass
    try:
        storage = int(input("How much do you receive monthly for any storage units on the property? "))
        income += storage
    except:
        pass
    try:
        misc = int(input("How much do you receive monthly as miscellaneous income from the property? "))
        income += misc
    except:
        pass
    return income

def get_expenses():
    expense = 0
    try:
        mortgage = int(input("Monthly cost of property mortgage: "))
        expense += mortgage
    except:
        pass
    try:
        tax = int(input("Monthly cost of property tax: "))
        expense += tax
    except:
        pass
    try:
        insurance = int(input("Monthly cost of property insurance: "))
        expense += insurance
    except:
        pass
    try:
        utilities = int(input("Monthly cost of property utilities (incl. electric, water, sewage, garbage, gas, etc.): "))
        expense += utilities
    except:
        pass
    try:
        hoa = int(input("Monthly cost of property Home Owner's Association fees: "))
        expense += hoa
    except:
        pass
    try:
        landscaping = int(input("Monthly cost of property landscaping: "))
        expense += landscaping
    except:
        pass
    try:
        repairs = int(input("Monthly cost of property repairs: "))
        expense += repairs
    except:
        pass
    try:
        cap_ex = int(input("Monthly cost of property renovations (e.g. replacing the roof, repaving driveway, etc.): "))
        expense += cap_ex
    except:
        pass
    try:
        property_management = int(input("Monthly cost of property management: "))
        expense += property_management
    except:
        pass
    try:
        future_vacancy = int(input("Monthly amount saved for future vacancy: "))
        expense += future_vacancy
    except:
        pass
    return expense

def get_investment():
    investment = 0
    try:
        down_payment = int(input("What was the property down payment? "))
        investment += down_payment
    except:
        pass
    try:
        closing_costs = int(input("What were the property closing costs? "))
        investment += closing_costs
    except:
        pass
    try:
        rehab = int(input("What was the cost to rehabilitate the property? "))
        investment += rehab
    except:
        pass
    try:
        misc = int(input("Enter total of any other miscellaneous investment costs: "))
        investment += misc
    except:
        pass
    return investment

def get_roi(inc, exp, inv):
    try:
        annual_cashflow = (inc - exp) * 12
        roi = float(annual_cashflow / inv) * 100
        return roi
    except:
        return 0