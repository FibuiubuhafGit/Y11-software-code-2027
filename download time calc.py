bps = int(input('How many bytes were downloaded in the past second? '))
btg = int(input('How many bytes still to go? '))
t = int(btg/bps)
if t== 1:
    print('The download will take approximately 1 second.')
elif t >= 2:
    print(f'The download will take approimately {t} seconds')
    
