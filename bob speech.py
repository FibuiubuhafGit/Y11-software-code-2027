##Testcase1
##input yarr harr
##output
##
##test case 2
##ahoy m'hearties
##yo ho ho and a bottle of rrrum
##tharr be th' treasure
##output 2
##
##test case 3
##input: ˙˙©¨ƒ¥∂†ƒ˙∫∫çµ∂ß´¢∫†√•µ•ª˙¨˜√•†¶
##output: 0
##
##test case 4
##input: hello how are you?
##output: 0
bob_speak = input('What did Bob say? (leave blank to end) ')
bob_list = []
bob_list.append(bob_speak)
while bob_speak != '':
    bob_speak = input('What did Bob say? (leave blank to end) ')
    bob_list.append(bob_speak)
rrcount = 0 
if 'rr' in bob_list:
    rrcount += 1


    
