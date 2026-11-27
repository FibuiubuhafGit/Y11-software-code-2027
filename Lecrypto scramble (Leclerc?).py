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

key = int(input('Number? ')) #get key for scramble
messages = [] #set messages as a list
msg = input('Code? ') #get message from agent

while msg != '': #if msg is not blank run the indented
    scram = ScrambleIt(msg,key) #Defined variable at top
    messages.append(scram) #adds the value of scram to the list
    msg = input('Code? ') #gets msg again
print(key) #prints the key for reference
for word in messages: # for very word in the list run the indented
    print(word) #Prints the word value
