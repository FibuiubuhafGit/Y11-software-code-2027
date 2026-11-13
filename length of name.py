word = input("What's the word? ")
if word == "":
    print('Please enter a word')
    print("What's the word? ")

total = len(word)

print(f'{word} has {total} characters.')
