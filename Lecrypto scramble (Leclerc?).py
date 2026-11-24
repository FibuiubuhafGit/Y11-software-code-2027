##code_list = []
##code = input('Code? ')
##code_list.append(code)
##while code != '':
##    code = input('Code? ')
##    code_list.append(code)
##code_list.split()
##num = int(input('Number? '))
##for word in code_list:
##    print(code[-num] + code[0:len(code)-num])

def ScrambleIt(msg,key):
    c = msg[-key:] #grabs last x amount of letters
    out = c + msg[0:len(msg) - key]#Grabs c + first len letters - key
    return out #returns ScrambleIt as out

key = int(input('Number? '))
messages = []
msg = input('Code? ')

while msg != '':
    scram = ScrambleIt(msg,key)
    messages.append(scram)
    msg = input('Code? ')
print(key)
for word in messages:
    print(word)
