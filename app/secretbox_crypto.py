from nacl.secret import SecretBox
from nacl.utils import random
import base64

# Generate key (32 bytes)
key = random(SecretBox.KEY_SIZE)

# Save key in base64
print("Key (save this):", base64.b64encode(key).decode())

box = SecretBox(key)

# Message
message = b"Top secret message"

# Encrypt
encrypted = box.encrypt(message)

print("Encrypted:", encrypted)

# Decrypt
decrypted = box.decrypt(encrypted)

print("Decrypted:", decrypted.decode())
