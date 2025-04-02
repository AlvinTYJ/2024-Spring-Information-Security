from Crypto.Cipher import AES
import base64
import itertools
import string

def unpad(text):
    # Remove zero padding
    return text.rstrip('\x00')

def decrypt_aes_ecb(ciphertext_b64, key):
    # Decode the Base64 encoded ciphertext
    ciphertext = base64.b64decode(ciphertext_b64)

    # Create AES cipher in ECB mode
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)

    # Decrypt the ciphertext
    decrypted = cipher.decrypt(ciphertext)

    # Remove padding and return the plaintext
    try:
        return unpad(decrypted.decode('utf-8'))
    except UnicodeDecodeError:
        # Handle the error and return an empty string or None
        return None

# Key template
key_template = '*-?5Q*E*qeDe*%Bs'
ciphertext_b64 = 'IZ7J32pjWOR0zpJeQbj1Z+Mu0cRftohz6imCF3+2k1w='  # Provided ciphertext

# Extract positions of '*' in the key template
stars_indices = [i for i, char in enumerate(key_template) if char == '*']
num_stars = len(stars_indices)

# Printable characters
printable_chars = string.printable

# Iterate over all combinations of printable characters for the '*' positions
for replacement in itertools.product(printable_chars, repeat=num_stars):
    # Create a new key by replacing '*' with the current combination
    key = list(key_template)
    for index, char in zip(stars_indices, replacement):
        key[index] = char
    key = ''.join(key).ljust(16, '\x00')  # Pad to 16 bytes

    # Decrypt with the generated key
    plaintext = decrypt_aes_ecb(ciphertext_b64, key)

    # Output the result if the decryption was successful
    if plaintext is not None:
        print("Decrypted plaintext:", plaintext)
        print("Key used:", key)

print("All possible keys have been processed.")
