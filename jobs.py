# Name: Alex Janssens
# Prog Purpose: This program finds the amount someone is paid for hours worked
# Cashier pay: $16.50
# Stocker pay: $15.75
# Janitor pay: $15.75
# Maintenance pay: $19.50
# Cashier pay: $16.50
# Stocker pay: $15.75
# Janitor pay: $15.75
# Maintenance pay: $19.50
# Federal income tax rate: 12%
# State income tax rate: 3%
# Social Security tax rate: 6.2%
# Medicare tax rate: 1.45%

import datetime

#define pay and deductions
C = 16.5
S = 15.75
J = 15.75
M = 19.5
FED_TAX = .12
STATE_TAX = .03
SS_TAX = .062
MED_TAX = .0145

#define global variables
num_hours = 0
emp_code = 0
pay_rate = 0
fedtax = 0
statetax = 0
ss_tax = 0
med_tax = 0
ded_total = 0
gross_pay = 0
net_pay = 0

# define program functions
def main():
    another_emp = True
    while another_emp:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like to enter another employee (Y/N): ")
        if yesno.upper() !="Y":
            another_emp = False
            
def get_user_data():
    global emp_code, num_hours
    emp_code = int(input("Enter 1 for Cashier, 2 for Stocker, 3 for Janitor, 4 for Maintenance:  "))
    num_hours = int(input("Number of hours worked: "))
    
def perform_calculations():
    global pay_total, ded_total, fedtax, statetax, ss_tax, med_tax, num_hours, gross_pay, net_pay
    if emp_code == 1:
        gross_pay = num_hours * C

    elif emp_code == 2 :
        gross_pay = num_hours * S
 
    elif emp_code == 3 :
        gross_pay = num_hours * J

    else:
        gross_pay = num_hours * M


    fedtax = gross_pay * FED_TAX
    statetax = gross_pay * STATE_TAX
    ss_tax = gross_pay * SS_TAX
    med_tax = gross_pay * MED_TAX
    ded_total = fedtax + statetax + ss_tax + med_tax
    net_pay = gross_pay - ded_total    

def display_results():
    print('\n--------------Fresh Food Market Place--------------')
    print('\n---------------------------------------------------')
    print('Hours worked : ' + format(num_hours,'10,.2f'))
    print('-----------------------------------------------------')
    print('Gross Pay             $ ' + format(gross_pay,'10,.2f'))
    print('Total deductions      $ ' + format(ded_total,'10,.2f'))
    print('Federal tax           $ ' + format(fedtax,'10,.2f'))
    print('State tax             $ ' + format(statetax,'10,.2f'))
    print('Social Security Tax   $ ' + format(ss_tax,'10,.2f'))
    print('Medicare Tax          $ ' + format(med_tax,'10,.2f'))
    print('-----------------------------------------------------')
    print('Amount paid           $ ' + format(net_pay,'10,.2f'))
    print('-----------------------------------------------------')
    print(str(datetime.datetime.now()))

main()

