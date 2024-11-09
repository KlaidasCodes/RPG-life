import json
from functions import *
from classes import *

# app that would essentially make my life an RPG game.
# Different stats with exp points, i can add those points whenever i complete a task
# or something in it. The final version would probably be best on a phone, but
# first just build it on a computer.


main_database = {}

# to allow for multiple accounts (idk why), in the database the keys will be player names
# and then each of those keys will have one more dict or something as its value,
# containing skills and their exp points.

# main_database = { "Klaidas": {"reading: 18,
#                               "gym": 56},
#                   "Name2": {"skill1": 34,
#                             "skill2": 92} }
# essentially like this. Easy to store and navigate. Json format, probably.

# EACH PLAYER COULD BE A CLASS INSTEAD??? AND THE METHODS COULD BE SOMETHING LIKE
# KLAIDAS_PLAYER.ADD_EXP("READING"). VERY EASY TO STORE AND KEEP TRACK OF THIS WAY.


AFTER_Q = "\n\t-"
# TODO-1 Create a "create your character" page where we get the basic info on the user.
# Later add log in functionality too, practice that side of system set-up
# For now no animations or anything, just plain code with basic functionality


# prompt to either log in or create an account (for now store the data insecurely, doesn't
# matter. Set up hashed password comparison system later


# initialize function when program starts to register/log in a player:

if __name__ == "__main__":
    app_running = True
    while app_running:
        # makes sure the user is logged in or registered
        main_database, logged_in = register_or_create_account(database=main_database, end_question=AFTER_Q)
        # now we have selected a person







        app_running = False

