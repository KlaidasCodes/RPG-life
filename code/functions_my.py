from classes_my import *
import os
import hashlib
import binascii
import string
import secrets


def update_database(database, name, pw, age):
    # initiate a human class
    new_human = Human(name, age, pw)
    # just for now, for testing, human gets random skills
    new_human.add_skill("reading", 46)
    new_human.add_skill("running", 13)
    new_human.add_skill("coding", 87)

    if new_human.name not in database:
        # later add a skills variable too. Not yet to save time.
        database[new_human.name] = {
            "password": new_human.pw,  # to be hashed in the future with a salt
            "age": new_human.age,
            # any other upcoming information like a new dictionary for skills
            "skills": new_human.skills
        }
        print(f"Database has been updated with a new player: {new_human.name}.\n")
        return database
    print("User with this name already exists. Try again.\n")
    return None


def register_or_create_account(database, end_question):
    logged_in: bool = False
    # prompt to either log in or create an account (for now store the data insecurely, doesn't
    # matter. Set up hashed password comparison system later
    while not logged_in:
        # later add handles. If a space is included, it crashes when tries to convert to int
        new_or_existing: int = int(input(f"Welcome! Do you already have an account or would you like to create "
                                         f"one? Type 1 or 2 (or 0 to close program):{end_question}"))

        if new_or_existing == 1:
            pass
        elif new_or_existing == 2:
            name_cap: str = input(f"What's your character's name?{end_question}").title()
            # pw: str = input(f"Set your password (more security under development):{end_question}")
            # age: int = int(input(f"How old is your character?{end_question}"))
            # name_cap = "Richard1"
            pw = "password123"
            age = "14"


            main_database = update_database(database, name=name_cap, pw=pw, age=age)
            if not main_database:
                break
            else:
                print(f"The main.py confirms that the database has been updated with new info. "
                      f"\n\n{main_database}.")
                logged_in = True
        elif not new_or_existing:
            break
        else:
            print(f"Input not understood. Try again.\n")

    return logged_in, database


def compare_hashed_passwords(username, password, database):
    """takes user's username and password. Hashes the password with SHA-256 (using existing salt that it extracts from the pw in DB). 
    Compares hashed inputted password with the hashed password in the database. Returns bool True if match."""
    password_from_database_hex = database[username]["password"]

    # this password is already hashed, now we need to convert the inputted password and compare.
    # we need to extract the first 16 bytes (the salt) from the database pw and use it to hash the inputted pw
    # the password will be in hex form in the json, so we can convert it to bytes and extract the first 16 bytes
    hashed_password_byte = hex_to_byte(password_from_database_hex)
    salt_extracted_byte = hashed_password_byte[0:16]
    # and now we hash the inputted password with this salt
    hashed_inputted_password_byte = hashing_function(password, salt_extracted_byte)
    return hashed_inputted_password_byte == hashed_password_byte



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


def hex_to_byte(string_in_hex):
    """takes a hex formatted string and converts it to bytes"""
    string_bytes = binascii.unhexlify(string_in_hex)
    return string_bytes



def byte_to_hex(string_in_bytes):
    string_hex = binascii.hexlify(string_in_bytes).decode()
    return string_hex


def current_level_and_exp(username, skill):
    """takes username and skill as input and returns the current level and exp"""
    pass

def exp_requirement_increment(current_exp_req: int):
    """takes current exp requirement as input and outputs next level's exp required"""
    return current_exp_req*1.3

def generate_random_pw():
    characters = string.digits + string.ascii_letters + string.punctuation
    generated_password = "".join(secrets.choice(characters) for i in range(16))
    return generated_password
