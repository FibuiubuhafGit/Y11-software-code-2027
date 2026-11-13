# my solution

##a = input('First string? ')
##b = input('Second string? ')
##c = input('Third string? ')
##
##longest = ''
##
##al = len(a)
##bl = len(b)
##cl = len(c)
##
##if al >= bl:
##    longest = a
##if cl > bl:
##    longest = c
##else:
##    longest = b
##
##print(f'The longest line was: {longest}')


#Classroom (OUR) solution
a = input('First string? ')
b = input('Second string? ')
c = input('Third string? ')

longest = a
if len(b) > len(longest):
    longest = b
if len(c) > len(longest):
    longest = c
Print('The longest line was', longest)
