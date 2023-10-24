"""
caesar cipher
"""

def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""

    shift %= 26

    for char in plaintext:
        new_char = ord(char) + shift
        if char.isalpha() and char.islower():
            ciphertext += chr( new_char % 122 + 96 ) if new_char > 122 else chr(new_char)
        elif char.isalpha() and char.isupper():
            ciphertext += chr( new_char % 90 + 64 ) if new_char > 90 else chr(new_char)
        else:
            ciphertext += char


    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    shift %= 26

    for char in ciphertext:
        new_char = ord(char) - shift
        if char.isalpha() and char.islower():
            plaintext += chr( new_char + 26 ) if new_char < 97 else chr(new_char)
        elif char.isalpha() and char.isupper():
            plaintext += chr( new_char + 26 ) if new_char < 65 else chr(new_char)
        else:
            plaintext += char


    return plaintext
