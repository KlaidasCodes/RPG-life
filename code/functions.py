from classes import *


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



