factor = 0 #set factor
limit = 0 #set limit
while factor != '' or limit != '': #set inf loop
    factor = int(input('What is the factor? ')) #get factor
    limit = int(input('What is the limit? ')) #get limit
    counter = 0 #set counter
    if factor != 0 or limit != 0: #if limit or factor aren't equal to 0
        #run indented lines
        while counter != limit: #while counter is not equal to 0 run indented
            #lines
            counter += 1 #add one to the counter every loop
            print(f'{factor} x {counter} = {counter*factor}') #prints out the
            #actual timetable statement
    else:
        print('Anything times 0 = 0')
