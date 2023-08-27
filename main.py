from flat import Bill, Flatmate
from reports import PdfReport

        
#Gather the bill amount, period and bill payers detail
bill_amount = float(input("Hey user, enter the bill amount: "))
month = input("Enter the bill month: ")
year = input("Enter the current year: ")
period = month + " " + year
# print("Period: ", period)

#Gather Payer's details
payer1 = input("Enter the first person name: ")
payer2 = input("Enter the second person name: ")

payer1_days = int(input(f"Enter the total days {payer1} stayed in the house during the bill period: "))
payer2_days = int(input(f"Enter the total days {payer2} stayed in the house during the bill period: "))

#Create the object of Bill and Flatmate
the_bill = Bill(bill_amount, period)
person1 = Flatmate(payer1, payer1_days)
person2 = Flatmate(payer2, payer2_days)

#Display each person's due amount
print(f"Bill amount of {person1.name} for {period} is $ {round(person1.pays(the_bill, person2), 2)}")
print(f"Bill amount of {person2.name} for {period} is $ {round(person2.pays(the_bill, person1), 2)}")

#Generate a pdf file for the month's bill and user's share of the bill
pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(person1, person2, the_bill)
