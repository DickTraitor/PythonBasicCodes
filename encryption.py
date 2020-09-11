import cryptography
from cyrptography.fernet import Fernet
key=Fernet.generate_key()
with open('key.key','wb') as f:
    f.write(key)
f.close()