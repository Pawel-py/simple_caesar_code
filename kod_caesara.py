import string


def generate_cipher(alphabet, key):
    cipher = ''
    for letter in alphabet:
        new_idx = (alphabet.index(letter) + key) % len(alphabet)
        cipher += alphabet[new_idx]
    return cipher


def encrypt(alphabet, message, key):
    cipher = generate_cipher(alphabet, key)
    result = ''
    for letter in message:
        if letter not in alphabet:
            result += letter
        else:
            result += cipher[alphabet.index(letter)]
    return result

def decrypt(alphabet,message,key):
    new_alphabet = generate_cipher(alphabet, key)
    result = ''
    for letter in message:
        if letter not in new_alphabet:
            result+=letter
        else:
            result+=alphabet[new_alphabet.index(letter)]
    return result


print(decrypt(string.ascii_uppercase, 'CVVCEM CV FCYP!', 2))