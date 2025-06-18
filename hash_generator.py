from passlib.hash import sha512_crypt
import os

output_file = "../hashes/sample_hashes.txt"
passwords = ["pass123", "hello123", "admin", "qwerty"]

os.makedirs(os.path.dirname(output_file), exist_ok=True)

with open(output_file, "w") as f:
    for pwd in passwords:
        hashed = sha512_crypt.hash(pwd)
        f.write(f"user:{hashed}\n")

print(f"[+] Password hashes written to {output_file}")
