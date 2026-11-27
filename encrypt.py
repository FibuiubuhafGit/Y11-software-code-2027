line = input('Enter the plain text: ')
line = line.replace('o', 'E')
line = line.replace('e', 'O')
line = line.replace('ray', 'YAR')
line = line.replace('yar', 'RAY')
split = len(line)//2
print(line[split:]+line[:split])
