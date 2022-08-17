




from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

salt = b'\xd45\xac}\xaf\xccy\x94\xca\xbc\xc0\x12G~\xd7h\xd4!Y2\xb1F;\x90\x19Ur\xf0Bi\xdaM'
password = "mypassword"

key = PBKDF2(password, salt, dkLen=32)

with open('encrypted.bin', 'rb') as f:
    iv = f.read(16)
    decrypt_data = f.read()

cipher = AES.new(key, AES.MODE_CBC, iv=iv)
original = unpad(cipher.decrypt(decrypt_data), AES.block_size)
print(original)
