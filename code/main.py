import json
import tkinter as tk
# from functions_my import *
# from classes_my import *
# for now commenting out the imports until I figure out how to import them from other files. Copy pasting
# the functions and classes here for now.

# from classes_my import *


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

class Human:
    def __init__(self, name, age, password):
        self.name = name
        self.age = age
        self.skills = {}
        self.pw = password
        self.total_exp = 0

    def add_skill(self, skill, exp=0):
        self.skills[skill] = exp

    def update_total_exp(self):
        for skill in self.skills:
            self.total_exp += self.skills[skill]
        return self.total_exp

    def display_as_dict(self):
        pass


class Skill:
    def __init__(self, skill, level=0, exp=0):
        self.skill = skill # the skill name like reading
        self.level = level
        self.exp = exp

    def add_exp(self, amount=1):
        self.exp += amount
        return self.exp

    def add_level(self, amount=1):
        self.level += amount
        return self.level

    def _change_skill_name(self, new_name):
        self.skill = new_name






main_database = {}
# CONSTANTS ##################
LIGHT_ORANGE = "#ffbc5c"
WHITE = "#ffffff"

AFTER_Q = "\n\t-"
# CONSTANTS ##############




if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1000x800")
    root.config(bg=WHITE)
    root.title("RPGLife.exe")
    canvas = tk.Canvas(root, width=800, height=600, bg=LIGHT_ORANGE)
    canvas.pack()
    

    root.mainloop()
    


    # canvas.quit()
    # app_running = True
    app_running = False
    while app_running:
        # makes sure the user is logged in or registered
        with open("./database_main.json", mode="r+") as file:
            temp_database = json.load(file) # python object
            logged_in, updated_database = register_or_create_account(database=temp_database, end_question=AFTER_Q)
            # work out how to update the database later, too confusing now
            ###############################################################################################
            #### the database gets accessed once at the beginning to get the current info. And then it gets
            #### accessed again at the end of the session, to update any changes that have happened. That's it.
            ###############################################################################################
            # json.dump(updated_database, file)
        # will need to set up a system that would update the current main_database to the new that comes out
        # if a new user registers OR the user adds any skills or exp or anything.
        # now we have selected a person
        app_running = False





# using a website builder is a no-go, I end up wasting too much time trying to figure them out.
# I think i might have to use canvas after all and stay with python
