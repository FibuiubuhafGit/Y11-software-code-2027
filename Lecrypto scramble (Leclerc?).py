code_list = []
code = input('Code? ')
code_list.append(code)
while code != '':
    code = input('Code? ')
    code_list.append(code)
num = int(input('Number? '))
for word in code_list:
    print(code[-num] + code[0:len(code)-num])
