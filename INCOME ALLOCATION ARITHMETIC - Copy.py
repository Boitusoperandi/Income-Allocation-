num1 = input('Enter your INCOME Amount:')
num2 = input('Enter Percentage allocated to SAVINGS :')
num3 = input('Enter Percentage allocated to SPENDING:')
num4 = input('Enter Percentage allocated to INVESTMENTS:')

print('SAVINGS =', float(num1)* (float(num2)*.01))
print('SPENDING =', float(num1)* (float(num3)*.01))
print('INVESTMENTS =', float(num1)* (float(num4)*.01))
