import os
import hashlib
import time
import stat
import sys

# Use raw string to handle backslashes in Windows path
dirpath = sys.argv[1]
print(dirpath)
hash_dict = dict()


for root, dirs, files in os.walk(dirpath):
    for file in files:
        filepath = os.path.join(root,file)
        os.chmod(filepath, stat.S_IWRITE)
        #print(filepath)
        hash_file = hashlib.md5()
        with open(filepath,"rb") as filehandle:
            while chunk := filehandle.read(4096):
                hash_file.update(chunk)
        final_hash = hash_file.hexdigest()
        if final_hash in hash_dict:
            print(f"{filepath} which has {os.path.getsize(filepath)} bytes already exist in {hash_dict[final_hash]}")
            try:
                print("removing duplicates.........")
                time.sleep(2)
                os.remove(filepath)
                print("File removed")
            except Exception as e:
                print(e)
        else: 
            hash_dict[final_hash] = filepath
        