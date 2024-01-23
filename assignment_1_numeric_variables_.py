# -*- coding: utf-8 -*-
"""Assignment #1: Numeric Variables.

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1df_72OwxcQz7TpXgw58m3INBTMWwX_dS
"""

#this is a while loop so that the user can restart the program if they want
#if else statements are utilized to determine which section of the program to execute based on what the user chooses
while True:
    program_choice = input("Please enter which calculation you would like to perform. 'c' for change, 't' for temperature, or 's' to stop the program.\n ")

    #choice c is for the change calculator
    if program_choice == 'c':
        f_user_cost = float(input('Enter the total cost: \n'))
        i_user_cost = int(f_user_cost)
        f_tendered_amount = float(input('Enter the amount tendered: \n'))
        i_tendered_amount = int(f_tendered_amount)

        #this is to find the difference between the whole number amount(dollars) and the decimal amount(change)
        dollar_cost = (i_tendered_amount - i_user_cost)
        f_coin_cost = (f_tendered_amount - f_user_cost)
        coin_cost = float(dollar_cost - f_coin_cost)

        quarters = int(coin_cost // 0.25)
        coin_cost %= 0.25
        print(quarters, "quarters")

        dimes = int(coin_cost // 0.10)
        coin_cost %= 0.10
        print(dimes, "dimes")

        nickel = int(coin_cost // 0.05)
        coin_cost %= 0.05
        print(nickel, "nickels")

        pennies = int(coin_cost // 0.01)
        coin_cost %= 0.01
        print(pennies, "pennies")

        #to calculate the number of bills needed:
        hundred_dollar_bills = dollar_cost // 100
        dollar_cost %= 100
        print(hundred_dollar_bills, "hundred dollar bill")

        fifty_dollar_bills = dollar_cost // 50
        dollar_cost %= 50
        print(fifty_dollar_bills, "fifty dollar bill")

        twenty_dollar_bills = dollar_cost // 20
        dollar_cost %= 20
        print(twenty_dollar_bills, "twenty dollar bill ")

        ten_dollar_bills = dollar_cost // 10
        dollar_cost %= 10
        print(ten_dollar_bills, "ten dollar bill")

        five_dollar_bills = dollar_cost // 5
        dollar_cost %= 5
        print(five_dollar_bills, "five dollar bill")

        dollar_bills = dollar_cost // 1
        dollar_cost %= 1
        print(dollar_cost, "one dollar bill")

        # this is the condition for the while loop, so that the user can continue the calculations without exiting
        money_again = input("Would you like to perform another calculation? ('y' or 'n') \n")
        if money_again == 'y':
            break

    #chice #t is for the temperature converter
    elif program_choice == 't':

        print("\n\n Welcome to the temperature converter calculator.")

        starting_temp = float(input("Enter the temperature you would like to convert with: \n"))
        temp_scale = input("Enter the scale you are starting with: ('c' for Celsius, 'f' for Fahrenheit, 'k' for Kelvin)")

        #these are if else statements to preform calculations based on the user's starting scale and desired ending scales (order of opperations)
        if temp_scale == 'c':
            convert_scale = input("Enter the scale you would like to convert to: ")
            if convert_scale == 'f':
                c_convert = (starting_temp * 1.8 + 32)
                print(c_convert)
            elif convert_scale == 'k':
                c_convert = (starting_temp + 273)
                print(c_convert)

        elif temp_scale == 'f':
            convert_scale = input("Enter the scale you would like to convert to:")
            if convert_scale == 'c':
                f_convert = (starting_temp - 32) * (5/9)
                print(f_convert)
            elif convert_scale == 'k':
                f_convert = (starting_temp - 32) * (5/9) + 273
                print(f_convert)

        elif temp_scale == 'k':
            convert_scale = input("Enter the scale you would like to convert to:")
            if convert_scale == 'c':
                k_convert = starting_temp - 273
                print(k_convert)
            elif convert_scale == 'f':
                k_convert = (starting_temp - 273) * 1.8 + 32
                print(k_convert)

        #this is another while loop condition so that the user can continue with the temperature calculations without exiting
        temp_again = input("Would you like to make another calculation? ('y' or 'n')\n")
        if temp_again == 'y':
            break

    #if the user enters 's' this will exit the program entirely
    elif program_choice == 's':
        break

    #this is in case the user enters something other than 'c' 't' or 's'. they will then have to retart the program
    else:
        print("You have entered an invalid choice. Please try again.\n")
