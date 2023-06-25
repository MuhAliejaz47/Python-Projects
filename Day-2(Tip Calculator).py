print ("Welcome to the tip Calculator!")
bill = input("What was the total bill: ")
people = input("How many people to split the bill: ")
tip = input("What percentage tip would you like to give: 10, 12 or 15? ")


if (int(tip) == 12):
    bill_for_each = float(bill) + (12*float(bill))/100
    if (int(tip) == 10):
        bill_for_each = float(bill) + (10*float(bill))/100
        if(int(tip) == 15):
         bill_for_each = float(bill) + (15*float(bill))/100

bill_for_each = float(bill_for_each) / float(people)
print (f"Each person should pay {bill_for_each}" )

