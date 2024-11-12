from tkinter import *
import tkinter as ttk
from time import sleep
import string
import secrets

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

def exiting_user_clicked(event):
    print("Existing user button has been clicked!")
    new_or_existing_page.withdraw()
    # open the log in window
    log_in_window.deiconify()
    # temporarily - close window after 1s
    log_in_window.after(2000, lambda: close_window(log_in_window))

def new_user_clicked(event):
    print("New user button has been clicked!")
    new_or_existing_page.withdraw()
    # open the register window
    register_window.deiconify()
    # temporarily - close window after 1s
    register_window.after(2000, lambda: close_window(register_window))

def randomise_pw_clicked(event):
    print("Randomise password has been clicked!")
    new_pw = generate_random_pw()
    print(new_pw)
    # and then add this password in the password slot


main_window = Tk()
main_window.withdraw()


# NEW OR EXISTING USER WINDOW ###########################################################################
new_or_existing_page = Toplevel(main_window)
new_or_existing_page.title("New or existing user")
new_or_existing_page.config(width=1000, height=800, bg=LIGHT_ORANGE)
new_or_existing_page.minsize(width=800, height=600)


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
existing_user_canvas.bind("<Button-1>", exiting_user_clicked)

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
create_new_account_canvas.grid(row=0, rowspan=2, column=1, columnspan=3)
create_new_account_text = create_new_account_canvas.create_text(190, 50, text="Create a new account:", 
                                                                font=("Futura Display", 36))

username_text_canvas = Canvas(register_window, width=140, height=50, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
username_text_canvas.grid(column=0, row=3)
username_text_canvas.create_text(70, 25, text="Username", font=("Futura Display", 24))

password_text_canvas = Canvas(register_window, width=140, height=50, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
password_text_canvas.grid(column=0, row=4)
password_text_canvas.create_text(70, 25, text="Password", font=("Futura Display", 24))

age_text_canvas = Canvas(register_window, width=140, height=50, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
age_text_canvas.grid(column=0, row=5)
age_text_canvas.create_text(70, 25, text="Age", font=("Futura Display", 24), anchor="w")

username_input_canvas = Canvas(register_window, width=400, height=60, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
username_input_canvas.grid(row=3, column=1)
username_input_rectangle = draw_rounded_rectangle(username_input_canvas, 0, 0, 400, 60, fill=LIGHTER_ORANGE)


password_input_canvas = Canvas(register_window, width=400, height=60, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
password_input_canvas.grid(row=4, column=1)
password_input_rectangle = draw_rounded_rectangle(password_input_canvas, 0, 0, 400, 60, fill=LIGHTER_ORANGE)

age_input_canvas = Canvas(register_window, width=400, height=60, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
age_input_canvas.grid(row=5, column=1)
age_input_rectangle = draw_rounded_rectangle(age_input_canvas, 0, 0, 400, 60, fill=LIGHTER_ORANGE)

generate_random_password_canvas = Canvas(register_window, width=150, height=60, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
generate_random_password_canvas.grid(row=4, column=3, columnspan=2)
generate_random_password_rectangle = draw_rounded_rectangle(generate_random_password_canvas, 0, 0, 150, 60, fill=LIGHTER_ORANGE)
generate_random_password_canvas.create_text(75, 30, text="Randomise", font=("Futura Display", 18))
generate_random_password_canvas.bind("<Button-1>", randomise_pw_clicked)



# EXISTING USER WINDOW ###########################################################################
log_in_window = Toplevel(main_window)
log_in_window.config(width=1000, height=800, bg=LIGHT_ORANGE)
log_in_window.minsize(width=800, height=600)
log_in_window.withdraw()







# new_or_existing_page.after(4000, lambda: close_window(new_or_existing_page))
mainloop()





