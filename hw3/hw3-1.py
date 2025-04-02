from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
import binascii

def hex_to_bytes(hex_str):
    return binascii.unhexlify(hex_str)

def count_bit_differences(byte_str1, byte_str2):
    diff = int.from_bytes(byte_str1, byteorder='big') ^ int.from_bytes(byte_str2, byteorder='big')
    return bin(diff).count('1')

plaintext_hex = '0123456789ABCDEF'
plaintext_bytes = hex_to_bytes(plaintext_hex)

key1_hex = '133457799BBCDFF1'
key2_hex = '133457799BBCDFE2'
key1_bytes = hex_to_bytes(key1_hex)
key2_bytes = hex_to_bytes(key2_hex)

des1 = DES.new(key1_bytes, DES.MODE_ECB)
des2 = DES.new(key2_bytes, DES.MODE_ECB)

ciphertext1 = des1.encrypt(pad(plaintext_bytes, DES.block_size))
ciphertext2 = des2.encrypt(pad(plaintext_bytes, DES.block_size))

bit_difference = count_bit_differences(ciphertext1, ciphertext2)

ciphertext1_hex = binascii.hexlify(ciphertext1).decode()
ciphertext2_hex = binascii.hexlify(ciphertext2).decode()

print(f"密文 1: {ciphertext1_hex}")
print(f"密文 2: {ciphertext2_hex}")
print(f"密文之間的位元差異數: {bit_difference} 位")
print(f"密文差異比例: {(bit_difference / 64) * 100:.2f}%")