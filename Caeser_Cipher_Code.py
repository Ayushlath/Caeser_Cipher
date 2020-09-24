import random

alphabet = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
special_characters = '!@#$%&*?><'
newmessage = ''
newmessages = ''
key = 3

character = input('Enter a character:')

for words in character:

    if words in alphabet:
        position = alphabet.find(words)
        newposition = (position+key)%26
        newcharacter = alphabet[newposition]
        newmessage += newcharacter

    if words in ALPHABET:
        position = ALPHABET.find(words)
        newposition = (position+key) % 26
        newcharacter = ALPHABET[newposition]
        newmessage += newcharacter

    if words in numbers:
        position = numbers.find(words)
        newposition = (position + key) % 10
        newcharacter = numbers[newposition]
        newmessage += newcharacter

    if words in special_characters:
        position = special_characters.find(words)
        newposition = (position + key) % 10
        newcharacter = special_characters[newposition]
        newmessage += newcharacter

print('Encoded characters are:', newmessage)

# to decode the message

key_input = int(input('Enter key to decode message:'))

if key_input == key:
   print('Decoded message is', character)
# if the key is wrong then it will generate another random message
else:
    for words in character:

        if words in alphabet:
            position = alphabet.find(words)
            newposition = (position + random.randint(1, 27)) % 26
            newcharacter = alphabet[newposition]
            newmessages += newcharacter

        if words in ALPHABET:
            position = ALPHABET.find(words)
            newposition = (position + random.randint(1, 27)) % 26
            newcharacter = ALPHABET[newposition]
            newmessages += newcharacter

        if words in numbers:
            position = numbers.find(words)
            newposition = (position + random.randint(0, 10)) % 10
            newcharacter = numbers[newposition]
            newmessages += newcharacter

        if words in special_characters:
            position = special_characters.find(words)
            newposition = (position + random.randint(1, 10)) % 10
            newcharacter = special_characters[newposition]
            newmessages += newcharacter

    print('Decoded message is', newmessages)
