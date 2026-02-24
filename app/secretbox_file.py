from nacl.secret import SecretBox
from nacl.utils import random

# Generate key
key = random(SecretBox.KEY_SIZE)

box = SecretBox(key)

# Read file
with open("secret.txt", "rb") as f:
    data = f.read()

# Encrypt
encrypted = box.encrypt(data)

with open("secret.enc", "wb") as f:
    f.write(encrypted)

print("File encrypted")

# Decrypt
with open("secret.enc", "rb") as f:
    encrypted_data = f.read()

decrypted = box.decrypt(encrypted_data)

with open("secret.dec.txt", "wb") as f:
    f.write(decrypted)

print("File decrypted")
