import os
from cryptography.fernet import Fernet

# Get key from GitHub Secret
key = os.environ.get("FERNET_KEY")

if not key:
    raise Exception("FERNET_KEY not found in environment variables")

key = key.encode()

fernet = Fernet(key)

# Encrypt
message = b"Secret message from Atelier 1"
encrypted = fernet.encrypt(message)

print("Encrypted:", encrypted)

# Decrypt
decrypted = fernet.decrypt(encrypted)

print("Decrypted:", decrypted.decode())
