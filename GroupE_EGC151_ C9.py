import sys
import random
cart = {}
# Nested dictionary
categories = {
    "Drinks (CD10)": {
        "N32": {"name": "Neo’s Green Tea", "price": 3.00},
        "M13": {"name": "Melo Chocolate Malt Drink", "price": 2.85},
        "V76": {"name": "Very-Fair Full Cream Milk", "price": 3.50},
        "N14": {"name": "Nirigold UHT Milk", "price": 4.15}
    },
    "Beer (CB20)": {
        "L11": {"name": "Lion (24 x 320 ml)", "price": 52.00},
        "P21": {"name": "Panda (24 x 320 ml)", "price": 78.00},
        "A54": {"name": "Axe (24 x 320 ml)", "price": 58.00},
        "H91": {"name": "Henekan (24 x 320 ml)", "price": 68.00}
    },
    "Frozen (CF30)": {
        "E11": {"name": "Edker Ristorante Pizza 355g", "price": 6.95},
        "F43": {"name": "Fazzler Frozen Soup 500g", "price": 5.15},
        "CP31": {"name": "CP Frozen Ready Meal 250g", "price": 4.12},
        "D72": {"name": "Duitoni Cheese 270g", "price": 5.60}
    },
    "Household (CH40)": {
        "FP76": {"name": "FP Facial Tissues", "price": 9.50},
        "FP32": {"name": "FP Premium Kitchen Towel", "price": 5.85},
        "K22": {"name": "Klinex Toilet Tissue Rolls", "price": 7.50},
        "D14": {"name": "Danny Softener", "price": 9.85}
    },
    "Snacks (CS50)": {
        "SS93": {"name": "Singshort Seaweed", "price": 3.10},
        "MC14": {"name": "Mei Crab Cracker", "price": 2.05},
        "R35": {"name": "Reo Pokemon Cookie", "price": 4.80},
        "HS11": {"name": "Huat Seng Crackers", "price": 3.55}
    }
}
gst = 0.09

def mainMenu():
    while True:
        print(f'\n{"="*50}\nWelcome to the Grocery Store!\n{"="*50}')
        print('''
[Categories:]        
[1] Drinks(CD10)    
[2] Beer(CB20)      
[3] Frozen(CF30)    
[4] Household(CH40) 
[5] Snacks(CS50)    

[Others:]            
[6] View Cart 
[7] Delete items in cart      
[8] Clear Cart
[9] Checkout        
[10] Exit            
''')

        selection = input('Select number (1-9): ')

        if selection == '1' or selection == '2' or selection == '3' or selection == '4' or selection == '5':
            displayCategory(selection)  # selection = input('Select number (1-8): ') pass into function
            while True:  # loop forever
                addItem()
                nextadd = input('\nAdd more items: \'y\', go back : \'b\':').strip().lower()
                while nextadd not in ['y', 'b']:
                    nextadd = input('\nInvalid input, Please type either \'y\' to add more items or \'b\' to go back:').strip().lower()   # loops the input till gets desired input
                if nextadd == 'y':
                    displayCategory(selection)  # call function
                elif nextadd == 'b':
                    break   # break from this function

        elif selection == '6':
            checkItem()
        elif selection == '7':
            removeItem()
        elif selection == '8':
            clearCart()
        elif selection == '9':
            checkout()
        elif selection == '10':
            print('Goodbye, See you again!')
            sys.exit()  # module sys
        else:
            print('Invalid Input, Type 1-10 to make a selection.')

def luckydraw():
    luckynumbers = random.randint(0, 1000)  # generate random number from 0 - 1000
    while True:
        try:
            luckyguess = int(input('Enter a number from 0 to 1000: '))
            while luckyguess not in range(0,1001):  # starts from 0 ends 1000 (indexing rule)
                luckyguess = int(input('Invalid range, Enter a number from 0 to 1000: '))

        except ValueError:
            print('Invalid input. Please enter a valid number.')
            continue  # repeat the while loop


        if luckyguess == luckynumbers:
            print('Congratulations,you have won a $500 voucher!\nProceed to any counters to claim them! ')
            break
        else:
            print('You did not guess the right number. '
                  'Thank you for participating in the lucky draw, Better luck next time!')
            break



def displayCategory(selection):
    category_keys = list(categories.keys())  # create a new list from the catergoies dictionary. catergory keys ['beer','drinks'...]
    categorykeylist = category_keys[int(selection) - 1] # list starts from 0 - so o, if user types 1, code will -1 to make it 0 to access the list.
    print(f'{"=" * 56}\n{categorykeylist:^56}\n{"=" * 56}')
    print(f'{"Code":<10} | {"Name":<30} | {"Price":<9}|')
    print(f'{"-" * 10}-|{"-" * 31}-|{"-" * 10}|')

    for code,food in categories[categorykeylist].items():
        print(f'{code:<10} | {food["name"]:<30} | ${food["price"]:<8.2f}|')

def addItem():
    while True:
        itemcode = input('\nEnter the item code to add into cart, type \'B\' to go back: ').strip().upper()
        validation = False  # starts from false
        if itemcode == 'B':
            mainMenu()
            return  # exit function
        else:
            for category,values in categories.items():
                if itemcode in values:
                    validation = True  # changes to True if item code exists
                    break  # if inputed code exist, break from loop
            if validation == False:  # remains false hence meaning its invalid
                print('Invalid Item code. Please enter an existing item code.')
                continue

            howmany = 0
            while True:
                try:
                    howmany = int(input('Enter quantity: '))
                    if howmany <= 0:
                        print('Quantity must be greater than zero.')
                        continue
                    break
                except ValueError:
                    print('Invalid input. You did not enter the a whole number.')
                    continue

        for typecate, detailfood in categories.items():
            if itemcode in detailfood:
                if itemcode in cart:
                    cart[itemcode]['quantity'] += howmany
                else:
                    cart[itemcode] = {"name": detailfood[itemcode]['name'], "price": detailfood[itemcode]['price'], "quantity": howmany}  # Cart dictionary stores {"name": item , "price": item , "quantity": item}
                print(f'\n{howmany}x {detailfood[itemcode]["name"]} has been added to your cart.')
                return
        print('Item code does not exist, Type again.')


def removeItem():
    total6 = 0.0
    quant = 0
    if not cart:
        print("Your cart is empty, returning to main menu...")
        return  # exit from the function is cart dictionary is empty
    print(f'\n{"="*92}\n{"Your Cart":^92}\n{"="*92}')
    print(f'{"Quantity":<10} | Code-{"Name":<45} | {"Unit Price":<12}|{"Total Price":<12}|')
    print(f'{"-" * 11}|{"-" * 52}|{"-" * 13}|{"-" * 12}|')
    for codeitem, codevalue in cart.items():
        name = codevalue['name']  # stores name retrieved dictionary cart
        code = codeitem
        price = codevalue['price']  # stores price retrieved dictionary cart
        quantity = codevalue['quantity']  # stores quantity retrieved dictionary cart
        total6 = total6 + (price * quantity)
        quant = quant + quantity
        print(f'{quantity:<10} | {code}-{name:<46} | ${price:<10.2f} |${price * quantity:<10.2f} |')

    while True:
        item_code = input('\nEnter the item code you wish to remove from the shopping list or press \'b\' to go back: ').strip().upper()
        if item_code == 'b':
            return

        if item_code in cart:
            while True:
                try:
                    numberofitem = int(input('Enter the number of items you want to remove: '))
                    if numberofitem <= 0:
                        print('Invalid quantity')
                        continue

                    if numberofitem == cart[item_code]['quantity']:
                        item_name = cart[item_code]['name']
                        item_no = cart[item_code]['quantity']
                        del cart[item_code]  # delete item from cart dictionary
                        print(f'All {item_no} of {item_name} removed from the cart.')
                        break
                    elif numberofitem < cart[item_code]['quantity']:
                        cart[item_code]['quantity'] -= numberofitem   # subtract number inputed with the quantity in cart if inputted number is lesser than what is in the cart
                        print(f'{numberofitem}x {cart[item_code]["name"]} removed from the cart.')
                        break
                    else:
                        print(f'You cannot remove more than {cart[item_code]["quantity"]} {cart[item_code]["name"]} items. You have inputted {numberofitem} quantity to remove ')
                    continue
                except ValueError:
                    print('Invalid input. Please enter a whole number.')
            break
        else:
            print('Item code not found in the cart.')
            continue








def checkItem():
    total6 = 0.0
    quant = 0
    if not cart:
        print("Your cart is empty, returning to main menu...")
        return
    print(f'\n{"="*92}\n{"Your Cart":^92}\n{"="*92}')
    print(f'{"Quantity":<10} | {"Name":<50} | {"Unit Price":<12}|{"Total Price":<12}|')
    print(f'{"-" * 11}|{"-" * 52}|{"-" * 13}|{"-" * 12}|')
    for codeitem, codevalue in cart.items():
        name = codevalue['name']
        price = codevalue['price']
        quantity = codevalue['quantity']
        total6 = total6 + (price * quantity)
        quant = quant + quantity
        print(f'{quantity:<10} | {name:<50} | ${price:<10.2f} |${price * quantity:<10.2f} |')

    print(f'{"-"*78}|${total6:<11.2f}|')
    print(f'[ {quant} items in your cart. ]')

    input('Press any key to continue...')  # allows user to see items in cart before moving on
    return

def clearCart():
    cart.clear()
    print('Cart Cleared')


discounts = {
    '1': {'type': 'Seniors', 'rate': 0.10},
    '2': {'type': 'Members', 'rate': 0.08},
    '3': {'type': 'NS Men', 'rate': 0.05},
    '0': {'type': 'None', 'rate': 0.00}
}
def discounter():
    print(f'''
{'='*50}
{'Discounts available:':>25}
{'='*50}
1. Seniors: 10% (60 years and above)
2. Members: 8%  
3. NS Men: 5%
0. None
''')

def checkout():
    if not cart:
        print('\n~Your cart is empty.Returning to main menu')
        mainMenu()
    total = 0.0

    print(f'\n{"="*92}\n{"BILL":^92}\n{"="*92}')
    print(f'{"Quantity":<10} | {"Name":<50} | {"Unit Price":<12}|{"Total Price":<12}|')
    print(f'{"-" * 11}|{"-" * 52}|{"-" * 13}|{"-" * 12}|')

    for codeitem, codevalue in cart.items():
        pricing = codevalue['price']
        quantity = codevalue['quantity']
        name = codevalue['name']
        total += pricing * quantity
        print(f'{quantity:<10} | {name:<50} | ${pricing:<10.2f} |${pricing * quantity:<10.2f} |')
    print(f'{"-" * 78}|${total:<11.2f}|\n{"|":>92}\n{"|":>92}\n{"="*92}')


    goback = input('\nDo you want still wish to make any changes to your cart before you proceeding with payment? Enter (y/n): ').strip().lower()
    while goback not in ['n', 'y']:
        goback = input('Invalid input.Do you want to make any changes to your cart before you proceed to payment? (y/n): ').strip().lower()
    if goback == 'y':
        mainMenu()
    else:
        discounter()

###############################################################################################################################################################################################
    discountsinpt = input("\nAre you eligible for any discount? (1: Seniors, 2: Members, 3: NS Men, 0: Not eligible): ")
    while discountsinpt not in ['1','2','3','0']:
        discountsinpt = input('Invalid input. Select discount (1: Seniors, 2: Members, 3: NS Men, 0: Not eligible): ')

    # getting the disc
    disctype = discounts.get(discountsinpt)
    disc_type = disctype['type']
    disc = discounts.get(discountsinpt)
    disc_rate = disc['rate']
    discount_amt = total * disc_rate
    subtotalaftdisc = total - discount_amt
    aftgst = subtotalaftdisc * gst
    grand_total = subtotalaftdisc + aftgst
###############################################################################################################################################################################################

    # Reciept
    total = 0.0
    print(f'\n{"="*92}\n{"BILL":^92}\n{"="*92}')
    print(f'{"Quantity":<10} | {"Name":<50} | {"Unit Price":<12}|{"Total Price":<12}|')
    print(f'{"-" * 11}|{"-" * 52}|{"-" * 13}|{"-" * 12}|')
    for codeitem, codevalue in cart.items():
        pricing = codevalue['price']
        quantity = codevalue['quantity']
        name = codevalue['name']
        total += pricing * quantity
        print(f'{quantity:<10} | {name:<50} | ${pricing:<10.2f} |${pricing * quantity:<10.2f} |')
    print(f'''
Subtotal: ${total:.2f}
Discount ({disc_type}): -${discount_amt:.2f}
GST: +${aftgst:.2f}
Grand Total: ${grand_total:.2f}
{'='*92}
''')

###############################################################################################################################################################################################

    confirm = input("Confirm payment? (y/n): ").strip().lower()
    while confirm not in ['y', 'n']:
        confirm = input("Invalid input. Confirm payment? (y/n): ").strip().lower()
    if confirm == 'y':
        print('\n~Payment successful!~\n')
        cart.clear()
        while True:
            timetoplay = input('Would you like to participate in a lucky draw and stand a chance to win a $500 voucher? Enter (y/n):').strip().lower()
            if timetoplay not in ['y', 'n']:
                timetoplay = input('Invalid Input, Enter (y/n):').strip().lower()
            elif timetoplay == 'y':
                luckydraw()
                sys.exit()
            else:
                print('Thank you for shopping with us, Goodbye!')
                sys.exit()
    else:
        print("Bill cancelled. Returning to main menu.")
        mainMenu()

mainMenu()