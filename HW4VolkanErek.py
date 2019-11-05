import pandas as pd
import os

df = os.getcwd() + "\\Plaza Coffee.txt"
df = pd.read_csv(df, sep=';')

companyNames = ["KPMG", "EY", "Deloite & Touche", "PWC"]
companyList = list(df['Company'])
paymentList = list(df['Payment'])
orderList = list(df['Order'])
quantityList = list(df['Quantity'])


for mycompany in companyNames:
    zipped = zip(companyList, paymentList, orderList, quantityList)
    dessertcash = 0
    dessertcredit = 0
    dailycash = 0
    dailycredit = 0
    coffeecash = 0
    coffeecredit = 0
    for company,payment,order,quantity in zipped:
        if(company == mycompany):
            if(order == 'Dessert' and payment == "Cash"):
                dessertcash += quantity
            if(order == 'Dessert' and payment == "Credit"):
                dessertcredit += quantity
            if(order == 'Daily Menu' and payment == "Cash"):
                dailycash += quantity
            if(order == 'Daily Menu' and payment == "Credit"):
                dailycredit += quantity
            if(order == 'Coffee' and payment == "Cash"):
                coffeecash += quantity
            if(order == 'Coffee' and payment == "Credit"):
                coffeecredit += quantity
    printstring = "Workers of " + mycompany
    if((dessertcash and dailycash) or (dailycash and coffeecash) or (dessertcash and coffeecash)):
        printstring = printstring + " have bought stuff with cash " + str(dessertcash + dailycash + coffeecash) + " times,"
    elif(dessertcash):
        printstring = printstring + " have bought Dessert with cash " + str(dessertcash) + " times,"
    elif(dailycash):
        printstring = printstring + " have bought Daily Menu with cash " + str(dessertcash) + " times,"
    elif(coffeecash):
        printstring = printstring + " have bought Coffee with cash " + str(dessertcash) + " times,"
    if((dessertcredit and dailycredit) or (dailycredit and coffeecredit) or (dessertcredit and coffeecredit)):
        printstring = printstring + " have bought stuff with credit " + str(dessertcredit + dailycredit + coffeecredit) + " times,"
    elif(dessertcredit):
        printstring = printstring + " have bought Dessert with credit " + str(dessertcredit) + " times,"
    elif(dailycredit):
        printstring = printstring + " have bought Daily Menu with credit " + str(dailycredit) + " times,"
    elif(coffeecredit):
        printstring = printstring + " have bought Coffee with credit " + str(coffeecredit) + " times,"
    print(printstring[:-1] + ".")
    
