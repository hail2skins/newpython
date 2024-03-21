
# Get details of loan
money_owed = float(input('How much money do you owe, in dollars?\n')) # e.g. 50,000
apr = float(input('What is the annual percentage rate?\n')) # e.g. 3.0
payment = float(input('What will your monthly payment be, in dollars?\n')) # e.g. 1,000
months = int(input('How many months do you want to see results for?\n')) # e.g. 24

monthly_rate = apr / 100 / 12

for i in range(months):

    interest_paid = money_owed*monthly_rate

    money_owed = money_owed + interest_paid
    
    if (money_owed - payment < 0):
        print('The last payment is', money_owed)
        print('You paid off the loan in', i+1, 'months')
        break

    money_owed = money_owed - payment

    print('Paid $', payment, 'of which', interest_paid, 'was interest.', end = '')
    print('Now I owe $', money_owed)