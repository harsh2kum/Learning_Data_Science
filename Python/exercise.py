# Q - Find the minimum number of 3 given number
"""
num1 = int(input('enter the 1st number: '))
num2 = int(input('enter the 2st number: '))
num3 = int(input('enter the 3st number: '))

if num1<num2 and num1<num3:
    print(f'{num1} is minimum ')

elif num2<num1 and num2<num3:
    print(f'{num2} is minimum')

else:
    print(f'{num3} is minimum') 
    
"""


# Q- ATM Machine Menu
'''
1. Pin Change
2. Balance check
3. Withdraw
4. Deposit
5. Exit
'''

menu = input("""
Hi Welcome to Atm
Please choose,
1. Enter 1 for Pin Change
2. Enter 2 for Balance check
3. Enter 3 for Withdraw
4. Enter 4 for Deposit
5. Enter Anythings for Exit
""")
# print(menu)

if menu == '1':
    print('Pin Change')

elif menu == '2':
    print("Balance Check")
    
elif menu == '3':
    print('Withdraw')
    
elif menu == '4':
    print('Deposit')

else:
    print('Exit')
    
