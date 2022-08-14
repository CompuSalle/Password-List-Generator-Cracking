# @Copyright
# Created by :
# Waseem Adel Alaa-Iddin
# Can be used in your project. A name maintaining will be nice.
# >> >> >> Ethical Use Only! << << << 

import itertools
import string
import time



#to run the while loops and stop it without any errors 
Run_The_Server = 1

first_section = 1
section_one_one = 1

Task_4B_loop = 1

User_Password = ''
User_Combination = ''
mainCombination = ''


Min_length_of_Pass = ''
Max_Length_of_Pass = ''

#Creating a list that contaies all symbols 
symbols = '@#$%=:?,./|~>*()<'


#(Password combination)
#only lower or upper or number (one type)
only_numbers = string.digits
only_lowercase = string.ascii_lowercase
only_uppercase = string.ascii_uppercase
only_symbols = symbols

#(Two combination)

"""
[
    numbers = 1
    lowercase = 2 
    uppercase = 3
    symbols = 4
    The Combinatiion
    1 2
    1 3
    1 4

    2 3
    2 4

    4 3 
] """

numbers_with_Lowercase = string.digits + string.ascii_lowercase 
numbers_with_uppercase = string.digits + string.ascii_uppercase 
numbers_with_symbols =  string.digits + symbols

Lowercase_with_uppercase = string.ascii_lowercase + string.ascii_uppercase 
Lowercase_with_symbols = string.ascii_lowercase + symbols

uppercase_with_symbols = string.ascii_uppercase + symbols

#(Three combination)

"""
[
    numbers = 1
    lowercase = 2 
    uppercase = 3
    symbols = 4
    The combinatiion
    1 2 3
    1 2 4
    2 1 4
    3 1 4 
]

"""
numbers_with_Lowercase_uppercase = string.digits + string.ascii_lowercase + string.ascii_uppercase
numbers_with_uppercase_symbols = string.digits + string.ascii_uppercase  + symbols
numbers_with_Lowercase_symbols = string.digits + string.ascii_lowercase + symbols

uppercase_with_Lowercase_symbols = string.ascii_uppercase +string.ascii_lowercase + symbols

#(All Combined)

All_combination = string.ascii_uppercase +string.ascii_lowercase + string.digits + symbols 



#Creating the main function of this program
def Password_table_generator():

    try :
    #Making some variable global to be reached  
        global Run_The_Server,first_section , Min_length_of_Pass, Max_Length_of_Pass, section_one_one
        
        #Start the loop
        while Run_The_Server ==1:
            

            #Asking the user about his preference before creating his list.
            print('\nThis program creates a rainbow table that may contain\n[Numbers - Lowercase - Uppercase - Symbols]\n')
            User_Combination = input("Would you like to create a rainbow table of \nA - 1 password combination\nB - 2 Password combination\nC - 3 Password combination\nD - 4 Password combination\n>>> ").lower()
            start_time = time.time()
            if User_Combination == 'a':

                while first_section == 1:
                    
                    print('\nOne combination has been chosen')
                    mainCombination = input('Would you like to create one combination of \nA- Numbers\nB- Lowercase\nC- uppercase\nD- Symbols\n>>> ').lower()
                    if mainCombination == 'a':
                        
                        #print(only_numbers) #If uncommented it will show the used values to create the pass (for test only)
                        attempts = 0
                        
                        while section_one_one ==1:
                            try :
                                table =  open('RainbowTable.txt', 'w')
                                print('\nOnly Numbers')
                                print("\nNote That A MAX of 4 means the highest digit is (****) - AKA four values ")
                                Min_length_of_Pass = int(input('\nEnter the Minimum length of the password >> '))
                                Max_length_of_Pass = int(input('Enter the Maximum length of the password >> '))
                                if Max_length_of_Pass > Min_length_of_Pass:
                                    x = int(Min_length_of_Pass)
                                    y = int(Max_length_of_Pass)
                                    y = y + 1
                                    for password_length in range(x, y):
                                        
                                        for guess in itertools.product(only_numbers, repeat=password_length):
                                            attempts += 1
                                            guess = ''.join(guess)
                                            table.write(guess)
                                            table.write('\n')
                                            print(f'{guess} the pass number is  {attempts}')
                                            section_one_one = 0
                                    
                                else:
                                    print('\n[!] Minimum can not be greater than Maximum')
                                    continue

                            except ValueError:
                                print('\n[!] Only numbers please')
                        first_section = 0
                        

                    elif mainCombination =='b':
                        #print(only_lowercase) #If uncommented it will show the used values to create the pass (for test only)
                        attempts = 0
                        
                        while section_one_one == 1:
                            try :
                                table =  open('RainbowTable.txt', 'w')
                                print('\nOnly Lowercase')
                                print("\nNote That A MAX of 4 means the highest digit is (****) - AKA four values ")
                                Min_length_of_Pass = int(input('\nEnter the Minimum length of the password >> '))
                                Max_length_of_Pass = int(input('Enter the Maximum length of the password >> '))
                                if Max_length_of_Pass > Min_length_of_Pass:
                                    x = int(Min_length_of_Pass)
                                    y = int(Max_length_of_Pass)
                                    y = y + 1
                                    for password_length in range(x, y):
                                        
                                        for guess in itertools.product(only_lowercase, repeat=password_length):
                                            attempts += 1
                                            guess = ''.join(guess)
                                            table.write(guess)
                                            table.write('\n')
                                            print(f'{guess} the pass number is  {attempts}')
                                            section_one_one = 0
                                    
                                else:
                                    print('\n[!] Minimum can not be greater than Maximum')
                                    continue

                            except ValueError:
                                print('\n[!] Only numbers please')
                        first_section = 0

                    elif mainCombination =='c':
                        print('\nOnly Uppercase')
                        #print(only_uppercase) #If uncommented it will show the used values to create the pass (for test only)
                        attempts = 0
                        
                        while section_one_one == 1:
                            try :
                                table =  open('RainbowTable.txt', 'w')
                                print("\nNote That A MAX of 4 means the highest digit is (****) - AKA four values ")
                                Min_length_of_Pass = int(input('\nEnter the Minimum length of the password >> '))
                                Max_length_of_Pass = int(input('Enter the Maximum length of the password >> '))
                                if Max_length_of_Pass > Min_length_of_Pass:
                                    x = int(Min_length_of_Pass)
                                    y = int(Max_length_of_Pass)
                                    y = y + 1
                                    for password_length in range(x, y):
                                        
                                        for guess in itertools.product(only_uppercase, repeat=password_length):
                                            attempts += 1
                                            guess = ''.join(guess)
                                            table.write(guess)
                                            table.write('\n')
                                            print(f'{guess} the Maximum number is  {attempts}')
                                            section_one_one = 0
                                    
                                else:
                                    print('\n[!] Minimum can not be pass than Maximum')
                                    continue

                            except ValueError:
                                print('\n[!] Only numbers please')
                        first_section = 0

                    elif mainCombination =='d':
                        print('\nOnly Symbols')
                        #print(only_symbols) #If uncommented it will show the used values to create the pass (for test only)
                        attempts = 0
                        
                        while section_one_one == 1:
                            try :
                                table =  open('RainbowTable.txt', 'w')
                                print("\nNote That A MAX of 4 means the highest digit is (****) - AKA four values ")
                                Min_length_of_Pass = int(input('\nEnter the Minimum length of the password >> '))
                                Max_length_of_Pass = int(input('Enter the Maximum length of the password >> '))
                                if Max_length_of_Pass > Min_length_of_Pass:
                                    x = int(Min_length_of_Pass)
                                    y = int(Max_length_of_Pass)
                                    y = y + 1
                                    for password_length in range(x, y):
                                        
                                        for guess in itertools.product(only_symbols, repeat=password_length):
                                            attempts += 1
                                            guess = ''.join(guess)
                                            table.write(guess)
                                            table.write('\n')
                                            print(f'{guess} the pass number is  {attempts}')
                                            section_one_one = 0
                                    
                                else:
                                    print('\n[!] Minimum can not be greater than Maximum')
                                    continue

                            except ValueError:
                                print('\n[!] Only numbers please')
                        first_section = 0
                    else:
                        print('Enter [A or B or C or D]')
                        continue

                Run_The_Server = 0


            #if the user wants two combination 
            elif User_Combination == 'b':
                while first_section == 1:
                    
                    print('\nYou have chosen two password combination')
                    mainCombination = input('You want a Two combintaion of \nA - Numbers & Lowercase \nB - Numbers & Uppercase\nC - Numbers & Symbols\nD - Lowercasr & Uppercase\nE - Lowercasr & Symbols\n\nF - Uppercase & Symbols\n>>> ').lower()
                    if mainCombination == 'a':
                        print('\nNumbers & Lowercase has been chosen')
                        #print(numbers_with_Lowercase) #If uncommented it will show the used values to create the pass (for testing)
                        attempts = 0
                        
                        while section_one_one ==1:
                            try :
                                table =  open('RainbowTable.txt', 'w')
                                print("\nNote That A MAX of 4 means the highest digit is (****) - AKA four values ")
                                Min_length_of_Pass = int(input('\nEnter the Minimum length of the password >> '))
                                Max_length_of_Pass = int(input('Enter the Maximum length of the password >> '))
                                if Max_length_of_Pass > Min_length_of_Pass:
                                    x = int(Min_length_of_Pass)
                                    y = int(Max_length_of_Pass)
                                    y = y + 1
                                    for password_length in range(x, y):
                                        
                                        for guess in itertools.product(numbers_with_Lowercase, repeat=password_length):
                                            attempts += 1
                                            guess = ''.join(guess)
                                            table.write(guess)
                                            table.write('\n')
                                            print(f'{guess} the pass number is  {attempts}')
                                            section_one_one = 0
                                    
                                else:
                                    print('\n[!] Minimum can not be greater than Maximum')
                                    continue

                            except ValueError:
                                print('\n[!] Only numbers please')
                        first_section = 0
                        

                    elif mainCombination =='b':
                        print('\nNumbers & Uppercase has been chosen')
                        #print(numbers_with_uppercase) #If uncommented it will show the used values to create the pass (for testing)
                        attempts = 0
                        
                        while section_one_one == 1:
                            try :
                                table =  open('RainbowTable.txt', 'w')
                                print("\nNote That A MAX of 4 means the highest digit is (****) - AKA four values ")
                                Min_length_of_Pass = int(input('\nEnter the Minimum length of the password >> '))
                                Max_length_of_Pass = int(input('Enter the Maximum length of the password >> '))
                                if Max_length_of_Pass > Min_length_of_Pass:
                                    x = int(Min_length_of_Pass)
                                    y = int(Max_length_of_Pass)
                                    y = y + 1
                                    for password_length in range(x, y):
                                        
                                        for guess in itertools.product(numbers_with_uppercase, repeat=password_length):
                                            attempts += 1
                                            guess = ''.join(guess)
                                            table.write(guess)
                                            table.write('\n')
                                            print(f'{guess} the pass number is  {attempts}')
                                            section_one_one = 0
                                    
                                else:
                                    print('\n[!] Minimum can not be greater than Maximum')
                                    continue

                            except ValueError:
                                print('\n[!] Only numbers please')
                        first_section = 0

                    elif mainCombination =='c':
                        print('\nNumbers & Symbols has been chosen')
                        #print(numbers_with_symbols) #If uncommented it will show the used values to create the pass (for testing)
                        attempts = 0
                        
                        while section_one_one == 1:
                            try :
                                table =  open('RainbowTable.txt', 'w')
                                print("\nNote That A MAX of 4 means the highest digit is (****) - AKA four values ")
                                Min_length_of_Pass = int(input('\nEnter the Minimum length of the password >> '))
                                Max_length_of_Pass = int(input('Enter the Maximum length of the password >> '))
                                if Max_length_of_Pass > Min_length_of_Pass:
                                    x = int(Min_length_of_Pass)
                                    y = int(Max_length_of_Pass)
                                    y = y + 1
                                    for password_length in range(x, y):
                                        
                                        for guess in itertools.product(numbers_with_symbols, repeat=password_length):
                                            attempts += 1
                                            guess = ''.join(guess)
                                            table.write(guess)
                                            table.write('\n')
                                            print(f'{guess} the pass number is  {attempts}')
                                            section_one_one = 0
                                    
                                else:
                                    print('\n[!] Minimum can not be greater than Maximum')
                                    continue

                            except ValueError:
                                print('\n[!] Only numbers please')
                        first_section = 0

                    elif mainCombination =='d':
                        print('\nLowercase & Uppercase has been chosen')
                        #print(Lowercase_with_uppercase) #If uncommented it will show the used values to create the pass (for testing)
                        attempts = 0
                        
                        while section_one_one == 1:
                            try :
                                table =  open('RainbowTable.txt', 'w')
                                print("\nNote That A MAX of 4 means the highest digit is (****) - AKA four values ")
                                Min_length_of_Pass = int(input('\nEnter the Minimum length of the password >> '))
                                Max_length_of_Pass = int(input('Enter the Maximum length of the password >> '))
                                if Max_length_of_Pass > Min_length_of_Pass:
                                    x = int(Min_length_of_Pass)
                                    y = int(Max_length_of_Pass)
                                    y = y + 1
                                    for password_length in range(x, y):
                                        
                                        for guess in itertools.product(Lowercase_with_uppercase, repeat=password_length):
                                            attempts += 1
                                            guess = ''.join(guess)
                                            table.write(guess)
                                            table.write('\n')
                                            print(f'{guess} the pass number is  {attempts}')
                                            section_one_one = 0
                                    
                                else:
                                    print('\n[!] Minimum can not be greater than Maximum')
                                    continue

                            except ValueError:
                                print('\n[!] Only numbers please')
                        first_section = 0
                    elif mainCombination =='e':
                        print('\nLowercase & Symbols has been chosen')
                        #print(Lowercase_with_symbols) #If uncommented it will show the used values to create the pass (for testing)
                        attempts = 0
                        
                        while section_one_one == 1:
                            try :
                                table =  open('RainbowTable.txt', 'w')
                                print("\nNote That A MAX of 4 means the highest digit is (****) - AKA four values ")
                                Min_length_of_Pass = int(input('\nEnter the Minimum length of the password >> '))
                                Max_length_of_Pass = int(input('Enter the Maximum length of the password >> '))
                                if Max_length_of_Pass > Min_length_of_Pass:
                                    x = int(Min_length_of_Pass)
                                    y = int(Max_length_of_Pass)
                                    y = y + 1
                                    for password_length in range(x, y):
                                        
                                        for guess in itertools.product(Lowercase_with_symbols, repeat=password_length):
                                            attempts += 1
                                            guess = ''.join(guess)
                                            table.write(guess)
                                            table.write('\n')
                                            print(f'{guess} the pass number is  {attempts}')
                                            section_one_one = 0
                                    
                                else:
                                    print('\n[!] Minimum can not be greater than Maximum')
                                    continue

                            except ValueError:
                                print('\n[!] Only numbers please')
                        first_section = 0

                    elif mainCombination =='f':
                        print('\nUppercase & Symbols has been chosen')
                        #print(uppercase_with_symbols) #If uncommented it will show the used values to create the pass (for testing)
                        attempts = 0
                        
                        while section_one_one == 1:
                            try :
                                table =  open('RainbowTable.txt', 'w')
                                print("\nNote That A MAX of 4 means the highest digit is (****) - AKA four values ")
                                Min_length_of_Pass = int(input('\nEnter the Minimum length of the password >> '))
                                Max_length_of_Pass = int(input('Enter the Maximum length of the password >> '))
                                if Max_length_of_Pass > Min_length_of_Pass:
                                    x = int(Min_length_of_Pass)
                                    y = int(Max_length_of_Pass)
                                    y = y + 1
                                    for password_length in range(x, y):
                                        
                                        for guess in itertools.product(uppercase_with_symbols, repeat=password_length):
                                            attempts += 1
                                            guess = ''.join(guess)
                                            table.write(guess)
                                            table.write('\n')
                                            print(f'{guess} the pass number is  {attempts}')
                                            section_one_one = 0
                                    
                                else:
                                    print('\n[!] Minimum can not be greater than Maximum')
                                    continue

                            except ValueError:
                                print('\n[!] Only numbers please')
                        first_section = 0
                    else:
                        print('Enter [A or B or C or D]')
                        continue

                Run_The_Server = 0

            elif User_Combination == 'c':
                while first_section == 1:
                    
                    print('\nThree pass combination has been chosen ')
                    mainCombination = input('You want a three combintaion of \nA - Numbers & Lowercase & Uppercase\nB - Numbers & Uppercase & Symbols \nC - Numbers & Lowercase & Symbols\nD - Uppercase & Lowercase & Symbols \n>>> ').lower()
                    if mainCombination == 'a':
                        print('\nNumbers & Lowercase & Uppercas has been chosen')
                        #print(numbers_with_Lowercase_uppercase) #If uncommented it will show the used values to create the pass (for testing)
                        attempts = 0
                        
                        while section_one_one ==1:
                            try :
                                table =  open('RainbowTable.txt', 'w')
                                print("\nNote That A MAX of 4 means the highest digit is (****) - AKA four values ")
                                Min_length_of_Pass = int(input('\nEnter the Minimum length of the password >> '))
                                Max_length_of_Pass = int(input('Enter the Maximum length of the password >> '))
                                if Max_length_of_Pass > Min_length_of_Pass:
                                    x = int(Min_length_of_Pass)
                                    y = int(Max_length_of_Pass)
                                    y = y + 1
                                    for password_length in range(x, y):
                                        
                                        for guess in itertools.product(numbers_with_Lowercase_uppercase, repeat=password_length):
                                            attempts += 1
                                            guess = ''.join(guess)
                                            table.write(guess)
                                            table.write('\n')
                                            print(f'{guess} the pass number is  {attempts}')
                                            section_one_one = 0
                                    
                                else:
                                    print('\n[!] Minimum can not be greater than Maximum')
                                    continue

                            except ValueError:
                                print('\n[!] Only numbers please')
                        first_section = 0
                        

                    elif mainCombination =='b':
                        print('\nNumbers & Uppercase & Symbols has been chosen')
                        #print(numbers_with_uppercase_symbols) #If uncommented it will show the used values to create the pass (for testing)
                        attempts = 0
                        
                        while section_one_one == 1:
                            try :
                                table =  open('RainbowTable.txt', 'w')
                                print("\nNote That A MAX of 4 means the highest digit is (****) - AKA four values ")
                                Min_length_of_Pass = int(input('\nEnter the Minimum length of the password >> '))
                                Max_length_of_Pass = int(input('Enter the Maximum length of the password >> '))
                                if Max_length_of_Pass > Min_length_of_Pass:
                                    x = int(Min_length_of_Pass)
                                    y = int(Max_length_of_Pass)
                                    y = y + 1
                                    for password_length in range(x, y):
                                        
                                        for guess in itertools.product(numbers_with_uppercase_symbols, repeat=password_length):
                                            attempts += 1
                                            guess = ''.join(guess)
                                            table.write(guess)
                                            table.write('\n')
                                            print(f'{guess} the pass number is  {attempts}')
                                            section_one_one = 0
                                    
                                else:
                                    print('\n[!] Minimum can not be greater than Maximum')
                                    continue

                            except ValueError:
                                print('\n[!] Only numbers please')
                        first_section = 0

                    elif mainCombination =='c':
                        print('\nNumbers & Lowercase & Symbols has been chosen')
                        #print(numbers_with_Lowercase_symbols) #If uncommented it will show the used values to create the pass (for testing)
                        attempts = 0
                        
                        while section_one_one == 1:
                            try :
                                table =  open('RainbowTable.txt', 'w')
                                print("\nNote That A MAX of 4 means the highest digit is (****) - AKA four values ")
                                Min_length_of_Pass = int(input('\nEnter the Minimum length of the password >> '))
                                Max_length_of_Pass = int(input('Enter the Maximum length of the password >> '))
                                if Max_length_of_Pass > Min_length_of_Pass:
                                    x = int(Min_length_of_Pass)
                                    y = int(Max_length_of_Pass)
                                    y = y + 1
                                    for password_length in range(x, y):
                                        
                                        for guess in itertools.product(numbers_with_Lowercase_symbols, repeat=password_length):
                                            attempts += 1
                                            guess = ''.join(guess)
                                            table.write(guess)
                                            table.write('\n')
                                            print(f'{guess} the pass number is  {attempts}')
                                            section_one_one = 0
                                    
                                else:
                                    print('\n[!] Minimum can not be greater than Maximum')
                                    continue

                            except ValueError:
                                print('\n[!] Only numbers please has been chosen')
                        first_section = 0

                    elif mainCombination =='d':
                        print('\nUppercase & Lowercase & Symbols has been chosen')
                        #print(uppercase_with_Lowercase_symbols) #If uncommented it will show the used values to create the pass (for testing)
                        attempts = 0
                        
                        while section_one_one == 1:
                            try :
                                table =  open('RainbowTable.txt', 'w')
                                print("\nNote That A MAX of 4 means the highest digit is (****) - AKA four values ")
                                Min_length_of_Pass = int(input('\nEnter the Minimum length of the password >> '))
                                Max_length_of_Pass = int(input('Enter the Maximum length of the password >> '))
                                if Max_length_of_Pass > Min_length_of_Pass:
                                    x = int(Min_length_of_Pass)
                                    y = int(Max_length_of_Pass)
                                    y = y + 1
                                    for password_length in range(x, y):
                                        
                                        for guess in itertools.product(uppercase_with_Lowercase_symbols, repeat=password_length):
                                            attempts += 1
                                            guess = ''.join(guess)
                                            table.write(guess)
                                            table.write('\n')
                                            print(f'{guess} the pass number is  {attempts}')
                                            section_one_one = 0
                                    
                                else:
                                    print('\n[!] Minimum can not be greater than Maximum')
                                    continue

                            except ValueError:
                                print('\n[!] Only numbers please')
                        first_section = 0
                    else:
                        print('Enter [A or B or C or D]')
                        continue

                Run_The_Server = 0

            elif User_Combination == 'd':
                while first_section == 1:
                    
                    print('\nAll combination has been chosen ')
                    print('A password combination of Numbers, Lowercase, Uppercase & Symbols will be generated')
                    mainCombination = 'a'
                    if mainCombination == 'a':
                        #print(All_combination) #If uncommented it will show the used values to create the pass (for testing)
                        attempts = 0
                        
                        while section_one_one ==1:
                            try :
                                table =  open('RainbowTable.txt', 'w')
                                print("\nNote That A MAX of 4 means the highest digit is (****) - AKA four values ")
                                Min_length_of_Pass = int(input('\nEnter the Minimum length of the password >> '))
                                Max_length_of_Pass = int(input('Enter the Maximum length of the password >> '))
                                if Max_length_of_Pass > Min_length_of_Pass:
                                    x = int(Min_length_of_Pass)
                                    y = int(Max_length_of_Pass)
                                    y = y + 1
                                    for password_length in range(x, y):
                                        
                                        for guess in itertools.product(All_combination, repeat=password_length):
                                            attempts += 1
                                            guess = ''.join(guess)
                                            table.write(guess)
                                            table.write('\n')
                                            print(f'{guess} the pass number is  {attempts}')
                                            section_one_one = 0
                                    
                                else:
                                    print('\n[!] Minimum can not be greater than Maximum')
                                    continue

                            except ValueError:
                                print('\n[!] Only numbers please')
                        first_section = 0       
                    else:
                        print('[!] Unknown Error')
                        continue
                Run_The_Server = 0
            else :
                print('\n---')
                print('please enter [A or B or C or D] only ')
                continue 
        print("\n\nRainbow table has been ganarated.")
        print("\n\nThe Pass has been ganarated in ---- %s seconds ----" % (time.time() - start_time)) 
        print('[-] stoped .. ')
    except KeyboardInterrupt:
        print('[!] Keyboard Interrupt detected... shutting down')


def brute_pass_using_table():
    try :
        global User_Password, Task_4B_loop
        while Task_4B_loop == 1:
            
            User_Password = input('Please provide a password to be brute-forced >> ')
            Rainbow_table_file_location = input('Please provide the location of the rainbow table...\n[!] Note >> please put the rainbow table.txt in same directory for easy access \n[+] example (RainbowTable.txt)\nEnter file location >>')
            start_time = time.time()
            Rainbow_table = open(Rainbow_table_file_location, 'r')
            Lines = Rainbow_table.readlines()
            count = 0
            for line in Lines:
                count += 1
                print("Password number {} : {} ".format(count, line.strip()))
                if User_Password == line.strip():
                    print('[+] Password has been found')
                    Task_4B_loop = 0
                    print("\n\nThe Pass has been cracked in ---- %s seconds ----" % (time.time() - start_time)) 
                    break
                elif User_Password != line.strip():
                    print('Not This Pass :(\n')
            else:
                again_try = input('Try again ? (y/N)').lower()
                if again_try == 'y':
                    continue
                elif again_try == 'n':
                    print('[-] Program will stop')
                    Task_4B_loop = 0
                    break
                else:
                    print('[-] y/N ? ')
                    continue
                
            print('[-] Program will stop now')
            Task_4B_loop = 0
    except KeyboardInterrupt:
        print('[!] Keyboard Interrupt detected... shutting down')
    

print('[!] Users are required to enter the min pass length and the max password length for the program to generate ,therefore')
print('[!] Note that ...  using bigger numbers may effect your CPU ... \n')

time.sleep(2)
print('[+] Starting...')


which_task_to_solve = input('[+] Please Choose > > \nA - (Creating Rainbow Table) \nB -  (Brutefores a password using a pre-build rainbow table)\n>> ').lower()

if which_task_to_solve == 'a':
    print('\n[+] Task A has been chosen ')
    time.sleep(1)
    Password_table_generator()
elif which_task_to_solve == 'b':
    print('\n[+]Task B has been chosen ')
    time.sleep(1)
    brute_pass_using_table()

else:
    print('[!] Error... please Re-run the program')
