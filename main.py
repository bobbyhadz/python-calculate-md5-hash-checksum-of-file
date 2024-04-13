# Python: How to calculate the MD5 Hash of a File

import hashlib

file_name = 'example.txt'

with open(file_name, 'rb') as file_obj:
    file_contents = file_obj.read()

    md5_hash = hashlib.md5(file_contents).hexdigest()

    # 👇️ cfd2db7dd4ffe42ce26e0b57e7e8b342
    print(md5_hash)