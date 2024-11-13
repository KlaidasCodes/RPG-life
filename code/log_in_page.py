from tkinter import *
import tkinter as ttk
from time import sleep
import string, secrets, json, binascii, os, hashlib

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


def draw_rounded_rectangle(canvas, x1, y1, x2, y2, radius=30, **kwargs):
    """takes input top left and bottom right corners (coordinates relative to parent's top left corner)
    and draws a rectangle with corners rounded to radius=30(by default). Can customize color and stuff."""
    canvas.create_arc(x1, y1, x1 + 2*radius, y1 + 2*radius, start=90, extent=90, outline="", style="pieslice", **kwargs)
    canvas.create_arc(x2 - 2*radius, y1, x2, y1 + 2*radius, start=0, extent=90, outline="", style="pieslice", **kwargs)
    canvas.create_arc(x1, y2 - 2*radius, x1 + 2*radius, y2, start=180, extent=90, outline="", style="pieslice", **kwargs)
    canvas.create_arc(x2 - 2*radius, y2 - 2*radius, x2, y2, start=270, extent=90, outline="", style="pieslice", **kwargs)

    # and now connect those arcs with actual sides of a rectangle
    canvas.create_rectangle(x1 + radius, y1, x2 - radius, y2, outline="", **kwargs)
    canvas.create_rectangle(x1, y1 + radius, x1 + radius, y2 - radius, outline="", **kwargs)
    canvas.create_rectangle(x2 - radius, y1 + radius, x2, y2 - radius, outline="", **kwargs)


def generate_random_pw():
    characters = string.digits + string.ascii_letters + string.punctuation
    generated_password = "".join(secrets.choice(characters) for i in range(16))
    return generated_password


# opening the database
with open("./database_main.json", mode="r+") as file:
            main_database = json.load(file)



def close_window(window):
    window.quit()
#consts
LIGHT_ORANGE = "#ffbc5c"
LIGHTER_ORANGE = "#EBDDC9"
WHITE = "#ffffff"
####



# 3 windows:
# 1) Asks if existing or new user
# 2) Log in window
# 3) Register window (could offer to generate a strong random password)

# needs adjusting slightly, the LIGHT_ORANGE background also has to have corner radius of 30deg instead of 0

def existing_user_clicked(event):
    print("Existing user button has been clicked!")
    new_or_existing_page.withdraw()
    # open the log in window
    log_in_window.deiconify()
    currently_open_window = log_in_window
    # temporarily - close window after 1s
    # log_in_window.after(2000, lambda: close_window(log_in_window))

def new_user_clicked(event):
    print("New user button has been clicked!")
    new_or_existing_page.withdraw()
    # open the register window
    register_window.deiconify()
    currently_open_window = register_window
    # temporarily - close window after 1s
    # register_window.after(2000, lambda: close_window(register_window))


def go_back_button_clicked(event):
    print("The go back button has been clicked!")
    # switch back to the existing or new user page
    register_window.withdraw()
    new_or_existing_page.deiconify()


def register_button_clicked(event):
    print("Register button has been clicked")
    # performs a few checks:
    # 1) do the password and repeated password match
    passwords_match_bool = password_entry.get() == repeat_password_entry.get()
    if not passwords_match_bool:
        print("Passwords must match.")
    # 2) are all the fields filled out
    all_fields_filled_bool = True
    if not password_entry.get() or not repeat_password_entry.get() or not username_entry.get() or not age_entry.get():
        all_fields_filled_bool = False
    if not all_fields_filled_bool:
        print("You must fill out all the questions before proceeding.") 
    # 3) if the username is not a duplicate
    username_unique_bool = True
    if username_entry.get() in main_database:
        username_unique_bool = False
        print("The username already exists!")
    # 4) if age only has numbers
    age_numeric_bool = True
    inputted_age_str = str(age_entry.get())
    for letter in (string.ascii_letters + string.punctuation + " "):
        if letter in inputted_age_str:
            age_numeric_bool = False
    if not age_numeric_bool:
        print("The age must be a number.")
    
    # and then we move onto adding the data into the database
    if age_numeric_bool and passwords_match_bool and username_unique_bool and all_fields_filled_bool:
        hashed_pw_byte = hashing_function(password_entry.get())
        hashed_pw_hex = byte_to_hex(hashed_pw_byte)
        main_database[username_entry.get()] = {
            "password": hashed_pw_hex,
            # for testing, later remove:
            "password_unhashed": password_entry.get(),
            "age": age_entry.get(),
            "skills": {}
        }
        print(main_database)

    # then the main database has to be updated. At the end of the session, replace current json with new json db

    # and then move on to the next page, which is the main page

    pass


def log_in_button_clicked(event):
    print("Log in button has been pressed!")
    # perform checks:
    # 1) are both fields filled
    log_in_fields_filled_bool = True
    if not log_in_username_entry.get() or not log_in_password_entry.get():
        log_in_fields_filled_bool = False
    if not log_in_fields_filled_bool:
        print("You must fill out all the questions before proceeding.") 
    # 2) does the username exist
    username_exists_bool = None
    if log_in_username_entry.get() in main_database:
        print("This user exists!")
        username_exists_bool = True
    if not username_exists_bool:
        print("User with this name does not exist.")
        username_exists_bool = False

    # if username exists, hash the password and check it against the one in the DB
    if username_exists_bool:
        pw_matches = compare_hashed_passwords(log_in_username_entry.get(), log_in_password_entry.get(), main_database)
        if not pw_matches:
            print("Inorrect password!")
        else:
            print("Correct password!")
            # move on to the main page.



def log_in_back_button_clicked(event):
    print("Back button has been pressed!")
    log_in_window.withdraw()
    new_or_existing_page.deiconify()


def randomise_pw_clicked(event):
    """when randomise button is clicked, generates 16digit pw, updates the clipboard and pastes it to 
    pw and repeat_pw fields."""
    print("Randomise password has been clicked!")
    new_pw = generate_random_pw()
    main_window.clipboard_clear()
    main_window.clipboard_append(new_pw)
    print(new_pw)
    # and then add this password in the password slot
    password_entry.delete(0, END)
    password_entry.insert(0, new_pw)
    repeat_password_entry.delete(0, END)
    repeat_password_entry.insert(0, new_pw)



main_window = Tk()
main_window.withdraw()


# NEW OR EXISTING USER WINDOW ###########################################################################
new_or_existing_page = Toplevel(main_window)
new_or_existing_page.title("New or existing user")
new_or_existing_page.config(width=1000, height=800, bg=LIGHT_ORANGE)
new_or_existing_page.minsize(width=800, height=600)
currently_open_window = new_or_existing_page


for i in range(3):
    new_or_existing_page.columnconfigure(i, weight=1)
    new_or_existing_page.rowconfigure(i, weight=1)


# top left of the grid
spacer = Canvas(new_or_existing_page, width=1, height=1, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
spacer.grid(column=0, row=0)

new_user_canvas = Canvas(new_or_existing_page, width=250, height=100, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
new_user_canvas.grid(column=0, row=2)
new_user = draw_rounded_rectangle(new_user_canvas, 0, 0, 250, 100, fill=LIGHTER_ORANGE)
new_user_canvas.create_text(125, 50, text="New User", font=("Futura Display", 32))
new_user_canvas.bind("<Button-1>", new_user_clicked)

existing_user_canvas = Canvas(new_or_existing_page, width=250, height=100, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
existing_user_canvas.grid(column=2, row=2)
existing_user = draw_rounded_rectangle(existing_user_canvas, 0, 0, 250, 100, fill=LIGHTER_ORANGE)
existing_user_canvas.create_text(125, 50, text="Existing User", font=("Futura Display", 32))
existing_user_canvas.bind("<Button-1>", existing_user_clicked)

welcome_text_canvas = Canvas(new_or_existing_page, width=350, height=100, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
welcome_text_canvas.grid(row=1, column=0, columnspan=3)
welcome_text_canvas.create_text(175, 50, text="Welcome!", font=("Futura Display", 74))




# NEW USER REGISTERING WINDOW ###########################################################################
register_window = Toplevel(main_window)
register_window.config(width=800, height=600, bg=LIGHT_ORANGE)
register_window.minsize(width=800, height=600)
register_window.withdraw()

#6 cols 10 rows
corner = Canvas(register_window, width=1, height=1, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
corner.grid(column=0, row=0)
for i in range(6):
    register_window.columnconfigure(i, weight=1)
for i in range(10):
    register_window.rowconfigure(i, weight=1)

create_new_account_canvas = Canvas(register_window, width=380, height=100, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
create_new_account_canvas.grid(row=0, rowspan=2, column=0, columnspan=4)
create_new_account_text = create_new_account_canvas.create_text(190, 50, text="Create a new account:", 
                                                                font=("Futura Display", 36))

username_text_canvas = Canvas(register_window, width=140, height=50, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
username_text_canvas.grid(column=0, row=3)
username_text_canvas.create_text(70, 25, text="Username", font=("Futura Display", 24))

password_text_canvas = Canvas(register_window, width=140, height=50, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
password_text_canvas.grid(column=0, row=4)
password_text_canvas.create_text(70, 25, text="Password", font=("Futura Display", 24))

repeat_password_text_canvas = Canvas(register_window, width=140, height=50, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
repeat_password_text_canvas.grid(column=0, row=5)
repeat_password_text_canvas.create_text(70, 25, text="Repeat pw", font=("Futura Display", 24))

age_text_canvas = Canvas(register_window, width=140, height=50, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
age_text_canvas.grid(column=0, row=6)
age_text_canvas.create_text(70, 25, text="Age", font=("Futura Display", 24), anchor="w")

username_input_canvas = Canvas(register_window, width=400, height=60, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
username_input_canvas.grid(row=3, column=1)
username_input_rectangle = draw_rounded_rectangle(username_input_canvas, 0, 0, 400, 60, fill=LIGHTER_ORANGE)
username_entry = Entry(register_window, font=("Futura Display", 24), bg=LIGHTER_ORANGE, bd=0, highlightthickness=0)
username_entry.grid(row=3, column=1)


password_input_canvas = Canvas(register_window, width=400, height=60, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
password_input_canvas.grid(row=4, column=1)
password_input_rectangle = draw_rounded_rectangle(password_input_canvas, 0, 0, 400, 60, fill=LIGHTER_ORANGE)
password_entry = Entry(register_window, font=("Futura Display", 24), bg=LIGHTER_ORANGE, bd=0, highlightthickness=0, show="*")
password_entry.grid(row=4, column=1)

repeat_password_input_canvas = Canvas(register_window, width=400, height=60, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
repeat_password_input_canvas.grid(row=5, column=1)
repeat_password_input_rectangle = draw_rounded_rectangle(repeat_password_input_canvas, 0, 0, 400, 60, fill=LIGHTER_ORANGE)
repeat_password_entry = Entry(register_window, font=("Futura Display", 24), bg=LIGHTER_ORANGE, bd=0, highlightthickness=0, show="*")
repeat_password_entry.grid(row=5, column=1)

age_input_canvas = Canvas(register_window, width=400, height=60, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
age_input_canvas.grid(row=6, column=1)
age_input_rectangle = draw_rounded_rectangle(age_input_canvas, 0, 0, 400, 60, fill=LIGHTER_ORANGE)
age_entry = Entry(register_window, font=("Futura Display", 24), bg=LIGHTER_ORANGE, bd=0, highlightthickness=0)
age_entry.grid(row=6, column=1)


generate_random_password_canvas = Canvas(register_window, width=150, height=60, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
generate_random_password_canvas.grid(row=4, column=3, columnspan=2)
generate_random_password_rectangle = draw_rounded_rectangle(generate_random_password_canvas, 0, 0, 150, 60, fill=LIGHTER_ORANGE)
generate_random_password_canvas.create_text(75, 30, text="Randomise", font=("Futura Display", 18))
generate_random_password_canvas.bind("<Button-1>", randomise_pw_clicked)

register_button_canvas = Canvas(register_window, width=160, height=120, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
register_button_canvas.grid(column=3, row=7, rowspan=2)
register_button_canvas_rectangle = draw_rounded_rectangle(register_button_canvas, 0, 0, 160, 120, fill=LIGHTER_ORANGE)
register_button_canvas.create_text(80, 60, text=">", font=("Futura Display", 70))
register_button_canvas.bind("<Button-1>", register_button_clicked)
register_window.bind("<Return>", register_button_clicked)

go_back_button_canvas = Canvas(register_window, width=160, height=120, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
go_back_button_canvas.grid(row=7, rowspan=2, column=0)
go_back_button_canvas_rectangle = draw_rounded_rectangle(go_back_button_canvas, 0, 0, 160, 120, fill=LIGHTER_ORANGE)
go_back_button_canvas.create_text(80, 60, text="<", font=("Futura Display", 70))
go_back_button_canvas.bind("<Button-1>", go_back_button_clicked)





# EXISTING USER WINDOW ###########################################################################
log_in_window = Toplevel(main_window)
log_in_window.config(width=1000, height=800, bg=LIGHT_ORANGE)
log_in_window.minsize(width=800, height=600)
log_in_window.withdraw()

corner2 = Canvas(log_in_window, width=1, height=1, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
corner2.grid(column=0, row=0)
for i in range(7):
    log_in_window.columnconfigure(i, weight=1)
for i in range(10):
    log_in_window.rowconfigure(i, weight=1)


log_in_canvas = Canvas(log_in_window, width=380, height=100, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
log_in_canvas.grid(row=0, rowspan=2, column=1, columnspan=5)
log_in_canvas.create_text(190, 50, text="Log in:", font=("Futura Display", 60))

log_in_username_text_canvas = Canvas(log_in_window, width=140, height=40, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
log_in_username_text_canvas.grid(column=1, columnspan=5, row=2)
log_in_username_text_canvas.create_text(70, 20, text="Username", font=("Futura Display", 24))

log_in_username_entry_canvas = Canvas(log_in_window, width=400, height=60, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
log_in_username_entry_canvas.grid(column=1, columnspan=5, row=3)
log_in_username_entry_canvas_rectangle = draw_rounded_rectangle(log_in_username_entry_canvas, 0, 0, 400, 60, fill=LIGHTER_ORANGE)
log_in_username_entry = Entry(log_in_window, font=("Futura Display", 24), bg=LIGHTER_ORANGE, bd=0, highlightthickness=0)
log_in_username_entry.grid(column=1, columnspan=5, row=3)

log_in_password_text_canvas = Canvas(log_in_window, width=140, height=40, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
log_in_password_text_canvas.grid(column=1, columnspan=5, row=4)
log_in_password_text_canvas.create_text(70, 20, text="Password", font=("Futura Display", 24))

log_in_password_entry_canvas = Canvas(log_in_window, width=400, height=60, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
log_in_password_entry_canvas.grid(column=1, columnspan=5, row=5)
log_in_password_entry_canvas_rectangle = draw_rounded_rectangle(log_in_password_entry_canvas, 0, 0, 400, 60, fill=LIGHTER_ORANGE)
log_in_password_entry = Entry(log_in_window, font=("Futura Display", 24), bg=LIGHTER_ORANGE, bd=0, highlightthickness=0, show="*")
log_in_password_entry.grid(column=1, columnspan=5, row=5)

log_in_button_canvas = Canvas(log_in_window, width=160, height=120, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
log_in_button_canvas.grid(column=4, row=6)
log_in_button_canvas_rectangle = draw_rounded_rectangle(log_in_button_canvas, 0, 0, 160, 120, fill=LIGHTER_ORANGE)
log_in_button_canvas.create_text(80, 60, text=">", font=("Futura Display", 70))
log_in_button_canvas.bind("<Button-1>", log_in_button_clicked)
log_in_window.bind("<Return>", log_in_button_clicked)

log_in_go_back_button_canvas = Canvas(log_in_window, width=160, height=120, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
log_in_go_back_button_canvas.grid(row=6, column=2)
log_in_go_back_button_canvas_rectangle = draw_rounded_rectangle(log_in_go_back_button_canvas, 0, 0, 160, 120, fill=LIGHTER_ORANGE)
log_in_go_back_button_canvas.create_text(80, 60, text="<", font=("Futura Display", 70))
log_in_go_back_button_canvas.bind("<Button-1>", log_in_back_button_clicked)



# new_or_existing_page.after(4000, lambda: close_window(new_or_existing_page))
mainloop()
