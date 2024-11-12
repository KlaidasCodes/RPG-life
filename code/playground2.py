import os
import binascii
import hashlib
import json


def byte_to_hex(string_in_bytes):
    string_hex = binascii.hexlify(string_in_bytes).decode()
    return string_hex

def hex_to_byte(string_in_hex):
    """takes a hex formatted string and converts it to bytes"""
    string_bytes = binascii.unhexlify(string_in_hex)
    return string_bytes

def hashing_function(password, salt=None):
    """Takes a password as input and hashes it either with a default salt which would be random 16-bytes
    or use a custom salt which could be extracted from the password we're comparing this hashed pw to.
    Returns BYTES salt+hashed password as one output to be stored"""
    if salt == None:
        salt = os.urandom(16)
    elif len(salt) != 16:
        raise ValueError("The salt must be 16 bytes long")
    hashed_password_byte = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100000)
    return salt+hashed_password_byte

def compare_hashed_passwords(username, password, database):
    """takes user's username and password. Finds the username, hashes the password with SHA-256 (using existing salt). 
    Compares hashed inputted password with the hashed password in the database. Returns bool True if match."""
    if username not in database:
        print("The user does not exist, try again.")
    else:
        password_from_database_hex = database[username]["password"]
        print(password_from_database_hex)

    # this password is already hashed, now we need to convert the inputted password and compare.
    # we need to extract the first 16 bytes (the salt) from the database pw and use it to hash the inputted pw
    # the password will be in hex form in the json, so we can convert it to bytes and extract the first 16 bytes
    hashed_password_byte = hex_to_byte(password_from_database_hex)
    salt_extracted_byte = hashed_password_byte[0:16]
    # and now we hash the inputted password with this salt
    hashed_inputted_password_byte = hashing_function(password, salt_extracted_byte)
    return hashed_inputted_password_byte == hashed_password_byte


with open("./database_main.json", mode="r+") as file:
            temp_database = json.load(file)



passwords_match = compare_hashed_passwords("Charlie", "pass789", temp_database)
print(passwords_match)
