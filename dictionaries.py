import sys
import time

# title
print('Product Storing App')
print('***************************************************************\n\n')
check1 = True  # Creating a flag variable
while check1:
    products = {}  # empty dictionary
    number_of_products = eval(input('Enter the number of products: '))  # taking the input of the user
    for i in range(number_of_products):  # using the input to iterate over the number of products to be entered
        key = input('Enter the Name of the product: ').capitalize()  # the key
        value = input('Enter the price of the product with no currency: ')  # the product
        products[key] = value
    print(products)
    print("************************************************************\n\n")
    time.sleep(1)

    check2 = True  # flag variable
    while check2:
        print('Make sure the product you are about to enter, is part of the list of products you added!')
        product_name = input('Enter your product name: ').capitalize()
        for key in products:
            if products[product_name] == products[key]:  # comparing user input to the dictionary list
                print(f' The price of {product_name} is {products[key]} Ghana cedis')
            else:
                print('You entered a product not available in the list')  # what happens if input is not equal to list
        print('*****************************************************************\n\n')
        time.sleep(1)
        print(f'Choose from the options below \nPress Enter to search for your product price \nPress 1 to return to '
              f'enter '
              f' a list of products \nPress 2 to exit the program')
        options = input('Make your choice')
        check3 = True
        while check3:
            if options == '':
                break
            elif options == '1':
                print("Let's start over again!")
                check2 = False
                check3 = False
            elif options == '2':
                print('Exiting........')
                time.sleep(1.5)
                sys.exit()
