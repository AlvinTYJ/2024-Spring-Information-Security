#by 陳奕嘉 E94115011
from Crypto.Cipher import AES
import base64

def unpad(text):
    return text.rstrip('\x00')

def decrypt_aes_ecb(ciphertext_b64, key):
    ciphertext = base64.b64decode(ciphertext_b64)
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    decrypted = cipher.decrypt(ciphertext)
    return unpad(decrypted.decode('utf-8'))


key = '~-?5QzEfqeDe@%Bs'
key = key.ljust(16, '\x00')

ciphertext_b64 = 'IZ7J32pjWOR0zpJeQbj1Z+Mu0cRftohz6imCF3+2k1w='

plaintext = decrypt_aes_ecb(ciphertext_b64, key)

print("Decryption successful! The plaintext is:", plaintext)