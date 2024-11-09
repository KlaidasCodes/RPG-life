from tkinter import *
from tkinter import ttk

LIGHT_ORANGE = "#ffbc5c"
LIGHTER_ORANGE = "#EBDDC9"
WHITE = "#ffffff"
username = "Maximus"

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


def change_window(new_window, current_window):
    new_window.deiconify()
    current_window.withdraw()
    current_window = new_window
    return current_window

# when dislaying the separate skill window, we'll finally use the Skill class 
# to fill in the information in the skill-only window for that specific skill.
# that way it's reusable.
window_main = Tk()
current_window = window_main
window_main.title("RPGLife.exe/main_page")
window_main.config(width=1000, height=800)
window_main.minsize(width=800, height=600)

window_all_skills = Toplevel(window_main)
window_specific_skill = Toplevel(window_main)
window_all_skills.withdraw()
window_specific_skill.withdraw()
window_all_skills.config(width=1000, height=800)
window_all_skills.minsize(width=800, height=600)
window_specific_skill.config(width=1000, height=800)
window_specific_skill.minsize(width=800, height=600)



window_all_skills.title("RPGLife.exe/all_skills")
skill = "placeholder"
window_specific_skill.title(f"RPGLife.exe/{skill}_skill")



# create the orange background for the app and round it
orange_background_box = Canvas(window_main, bg=WHITE, width=800, height=600, highlightthickness=0, bd=0)
orange_bg_box_rounded = draw_rounded_rectangle(orange_background_box, 0, 0, 800, 600, fill=LIGHT_ORANGE)
orange_background_box.grid(column=11, row=11, columnspan=28, rowspan=18)




# big rounded rectangle on the left
canvas_main_left_big_rectangle = Canvas(window_main, width=300, height=420, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
canvas_main_left_big_rectangle.grid(column=8, row=10, columnspan=15, rowspan=20)
main_left_big_rectangle = draw_rounded_rectangle(canvas_main_left_big_rectangle, 0, 0, 300, 420, fill=LIGHTER_ORANGE)

# small rounded rectangle on the left
canvas_main_left_small_rectangle = Canvas(window_main, width=300, height=60, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
canvas_main_left_small_rectangle.grid(column=8, columnspan=15, row=26, rowspan=3)
main_left_small_rectangle = draw_rounded_rectangle(canvas_main_left_small_rectangle, 0, 0, 300, 60, radius=15, fill=LIGHTER_ORANGE)


# big rounded rectangle on the right

canvas_main_right_big_rectangle = Canvas(window_main, width=420, height=420, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
canvas_main_right_big_rectangle.grid(column=22, columnspan=17, row=10, rowspan=21)
main_right_big_rectangle = draw_rounded_rectangle(canvas_main_right_big_rectangle, 0, 0, 420, 420, fill=LIGHTER_ORANGE)


# player name
main_label_name = Label(window_main, text=username, font=("Futura Display", 36, "bold"), bg=LIGHTER_ORANGE)
main_label_name.grid(column=12, columnspan=10, row=24, rowspan=2)

# main page button to skills
def main_button_pressed():
    change_window(new_window=window_all_skills, current_window=current_window)
    window_main.quit() # temporaty, to stop the app from going into loops
    return print("I've been pressed")


main_button_image = PhotoImage(file="./images/button_main.png", width=243, height=105)
main_button_to_skills = Button(window_main, height=80, width=210, activebackground=LIGHT_ORANGE, image=main_button_image, command=main_button_pressed, bg=LIGHT_ORANGE, fg=LIGHT_ORANGE, bd=0, highlightthickness=0)
main_button_to_skills.grid(row=26, rowspan=3, column=27, columnspan=7)


# main page right side left small box
canvas_main_right_side_left_small_box = Canvas(window_main, width=100, height=180, bg=LIGHTER_ORANGE, bd=0, highlightthickness=0)
canvas_main_right_side_left_small_box.grid(column=23, columnspan=5, row=18, rowspan=10)
main_right_side_left_small_box = draw_rounded_rectangle(canvas_main_right_side_left_small_box, 0, 0, 100, 180, fill=WHITE)

# main page right side right small box
canvas_main_right_side_right_small_box = Canvas(window_main, width=100, height=180, bg=LIGHTER_ORANGE, bd=0, highlightthickness=0)
canvas_main_right_side_right_small_box.grid(column=33, columnspan=5, row=18, rowspan=10)
main_right_side_right_small_box = draw_rounded_rectangle(canvas_main_right_side_right_small_box, 0, 0, 100, 180, fill=WHITE)

# main page right side mid med box
canvas_main_right_side_mid_med_box = Canvas(window_main, width=140, height=240, bg=LIGHTER_ORANGE, bd=0, highlightthickness=0)
canvas_main_right_side_mid_med_box.grid(column=27, columnspan=7, row=15, rowspan=13)
main_right_side_mid_med_box = draw_rounded_rectangle(canvas_main_right_side_mid_med_box, 0, 0, 140, 240, fill=WHITE)



window_main.mainloop()
