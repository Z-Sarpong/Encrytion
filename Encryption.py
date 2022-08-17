






from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

simple_key = get_random_bytes(32)
print(simple_key)
# Run this code first and then...

# Followup code
salt = b'\xd45\xac}\xaf\xccy\x94\xca\xbc\xc0\x12G~\xd7h\xd4!Y2\xb1F;\x90\x19Ur\xf0Bi\xdaM'
password = "mypassword"

key = PBKDF2(password, salt, dkLen=32)

message = b"Hellow Secret World"

cipher = AES.new(key, AES.MODE_CBC)
ciphered_data = cipher.encrypt(pad(message, AES.block_size))

with open('encrypted.bin', 'wb') as f:
    f.write(cipher.iv)
    f.write(ciphered_data)

with open('encrypted.bin', 'rb') as f:
    iv = f.read(16)
    decrypt_data = f.read()

cipher = AES.new(key, AES.MODE_CBC, iv=iv)
original = unpad(cipher.decrypt(decrypt_data), AES.block_size)
print(original)

with open('key.bin', 'wb') as f:
    f.write(cipher.iv)
    f.write(ciphered_data)
