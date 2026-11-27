line1 = input('Line 1: ')#Gets all 3 user inputs
line2 = input('Line 2: ')
line3 = input('Line 3: ')

if line1 != line2 and line1 != line3: #checks if line 1 is equal to
                                      #line 2 and 3
    print(line1)

if line2 != line1 and line2 != line3:#checks if line 2 is equal to
                                     #line 1 and 3
   print(line2)

if line3 != line2 and line3 != line1:#checks if line 3 is equal to
                                     #line 1 and 2
    print(line3)

else: #if all the lines are different comes here
    print('All are different')
