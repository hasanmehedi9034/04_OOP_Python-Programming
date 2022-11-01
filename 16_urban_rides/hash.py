# Rtrams -> smart
# splkiyoanr -> lion


import hashlib

email = 'mdi@gmail.com'
pwd = 'ChariOnTable'

pwd_encode = pwd.encode()
pwd_hash = hashlib.md5(pwd_encode).hexdigest()

print(pwd)
print(pwd_hash)