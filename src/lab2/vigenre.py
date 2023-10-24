"""
vignere cipher
"""

def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""

    if keyword.strip() == '': return plaintext

    # completing the keyword to plaintext length
    while len(keyword) < len(plaintext):
        keyword += keyword[:len(plaintext)-len(keyword)]

    # enctrypt
    for i in range(len(plaintext)):
        char  = plaintext[i]
        shift = (ord(keyword[i].lower()) - 97) % 26
        new_char = ord(char)+shift

        if char.isalpha() and char.islower():
            ciphertext += chr( new_char % 122 + 96 ) if new_char > 122 else chr(new_char)
        elif char.isalpha() and char.isupper():
            ciphertext += chr( new_char % 90 + 64 ) if new_char > 90 else chr(new_char)
        else:
            ciphertext += char

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""

    if keyword.strip() == '': return ciphertext

    # completing the keyword to plaintext length
    while len(keyword) < len(ciphertext):
        keyword += keyword[:len(ciphertext)-len(keyword)]

    # decrypt
    for i in range(len(ciphertext)):
        char  = ciphertext[i]
        shift = (ord(keyword[i].lower()) - 97) % 26
        new_char = ord(char) - shift

        if char.isalpha() and char.islower():
            plaintext += chr( new_char + 26 ) if new_char < 97 else chr(new_char)
        elif char.isalpha() and char.isupper():
            plaintext += chr( new_char + 26 ) if new_char < 65 else chr(new_char)
        else:
            plaintext += char

    return plaintext
