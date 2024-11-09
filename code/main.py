import json
import tkinter as tk
from functions_my import *
from classes_my import *
# for now commenting out the imports until I figure out how to import them from other files. Copy pasting
# the functions and classes here for now.

# from classes_my import *



# WHEN APP STARTS, IT PRINTS "HELLO WORLD" TWICE FOR SOME REASON, COMING FROM
# SOME RANDOM FILE FROM THE OUTSIDE


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
