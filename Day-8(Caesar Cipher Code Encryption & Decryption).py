def encrypt(text, shift):
    cipher_text = ''
    plain_text = text
    for letter in plain_text:
        index = alphabets.index(letter)
        new_index = (index + shift) % 26
        new_letter = alphabets[new_index]
        cipher_text = cipher_text + new_letter

    print(f'Plain Text is {plain_text}')
    print(f'Encoded Text is {cipher_text}')


def decrypt(text, shift):
    decipher_text = ''
    plain_text = text
    for letter in plain_text:
        index = alphabets.index(letter)
        new_index = (index - shift) % 26
        new_letter = alphabets[new_index]
        decipher_text = decipher_text + new_letter

    print(f'Plain Text is {plain_text}')
    print(f'Decoded Text is {decipher_text}')


alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

decision = 'y'

while decision == 'y':
    direction = input('Type "encode" to encrypt and "decode" to decrypt: \n')

    if direction == 'encode':
        text = input('Type your message: \n').lower()
        shift = int(input('Type the shift number: \n'))
        encrypt(text=text, shift=shift)
    elif direction == 'decode':
        text = input('Type your message: \n').lower()
        shift = int(input('Type the shift number: \n'))
        decrypt(text=text, shift=shift)
    else:
        print('Enter a valid command')

    decision = input('Do you want to go again? Type "y" for yes and "n" for no\n')
