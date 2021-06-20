age: int = int(input("Your age: "))

drink = input("What would you like to drink? Beer or coke? ")

if drink == 'beer':
    print('beer')
    if age >= 18:
        print('HERE YOU ARE! YOUR BEER.')
    else:
        print('SORRY! I CANT SERVE BEER FOR YOU!')
elif drink == 'coke':
    print('Coke')
    if age > 60:
        print('CAFFEIN CAN RAISE YOUR BLOOD PRESSURE.')
    else:
        print('HERE YOU ARE! YOUR COKE!')
else:
    print('SORRY! WE DONT HAVE THAT DRINK!')