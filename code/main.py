import json
from functions import *
from classes import *


main_database = {}


AFTER_Q = "\n\t-"

if __name__ == "__main__":
    app_running = True
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





