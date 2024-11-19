import os
import binascii
import hashlib
import json
import tkinter as tk
from PIL import Image, ImageTk


LIGHT_ORANGE = "#ffbc5c"
LIGHTER_ORANGE = "#EBDDC9"
STAR_IMAGE_SRC = "./images/star2.png"
PLACEHOLDER_EXP = 125
PLACEHOLDER_PERSON = "Alice"


avatars = {
    "male": {
        "1": "./images/Avatars/Male/male1.png",
        "2-5": "./images/Avatars/Male/male2-5.png",
        "5-10": "./images/Avatars/Male/male5-10.png",
        "10-15": "./images/Avatars/Male/male10-15.png",
        "15-30": "./images/Avatars/Male/male15-30.png",
        "30+": "./images/Avatars/Male/male30+.png"
    },
    "female": {
        "1": "./images/Avatars/Female/female1.png",
        "2-5": "./images/Avatars/Female/female2-5.png",
        "5-10": "./images/Avatars/Female/female5-10.png",
        "10-15": "./images/Avatars/Female/female10-15.png",
        "15-30": "./images/Avatars/Female/female15-30.png",
        "30+": "./images/Avatars/Female/female30+.png"
    }
}

def pick_avatars_path(level, sex, avatar_dict):
    if level == 1:
        return avatar_dict[sex]["1"]
    elif 2 <= level < 5:
        return avatar_dict[sex]["2-5"]
    elif 5 <= level < 10:
        return avatar_dict[sex]["5-10"]
    elif 10 <= level < 15:
        return avatar_dict[sex]["10-15"]
    elif 15 <= level < 30:
        return avatar_dict[sex]["15-30"]
    else:
        return avatar_dict[sex]["30+"]


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


def close_window(window):
    window.quit()


PLACEHOLDER_LEVEL = 2
PLACEHOLDER_GENDER = "female"


with open("./database_main.json", mode="r+") as file:
            main_database = json.load(file)

person_logged_in = main_database["Alice"]

main_window = tk.Tk()

main_window.config(width=800, height=600, bg=LIGHT_ORANGE)
main_window.minsize(width=800, height=600)
for i in range(20):
    main_window.columnconfigure(i, weight=1)
    main_window.rowconfigure(i, weight=1)

corner = tk.Canvas(main_window, width=1, height=1, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
corner.grid(column=0, row=0)

main_left_big_rectangle_canvas = tk.Canvas(main_window, width=300, height=420, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
main_left_big_rectangle_canvas.grid(column=1, columnspan=8, row=3, rowspan=14, sticky="w", padx=20)
main_left_big_rectangle_canvas_rectangle = draw_rounded_rectangle(main_left_big_rectangle_canvas, 0, 0, 300, 420, fill=LIGHTER_ORANGE)


main_left_small_rectangle_canvas = tk.Canvas(main_window, width=300, height=60, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
main_left_small_rectangle_canvas.grid(column=1, columnspan=8, row=17, rowspan=2, sticky="nw", padx=20, pady=20)
main_left_small_rectangle_canvas_rectangle = draw_rounded_rectangle(main_left_small_rectangle_canvas, 0, 0, 300, 60, radius=15, fill=LIGHTER_ORANGE)

main_right_big_rectangle_canvas = tk.Canvas(main_window, width=420, height=420, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
main_right_big_rectangle_canvas.grid(column=9, columnspan=11, row=3, rowspan=14, sticky="e", padx=20)
main_right_big_rectangle_canvas_rectangle = draw_rounded_rectangle(main_right_big_rectangle_canvas, 0, 0, 420, 420, fill=LIGHTER_ORANGE)

main_name_canvas = tk.Canvas(main_window, width=200, height=60, bg=LIGHTER_ORANGE, bd=0, highlightthickness=0)
main_name_canvas.grid(column=2, columnspan=6, row=14, rowspan=2)
main_name_canvas.create_text(100, 30, text=PLACEHOLDER_PERSON, font=("Futura Display", 38))


main_left_top_small_rectangle_canvas = tk.Canvas(main_window, width=300, height=80, bg=LIGHT_ORANGE, 
                                                 bd=0, highlightthickness=0)
main_left_top_small_rectangle_canvas.grid(column=0, columnspan=8, row=0, rowspan=2)
star_image = Image.open(STAR_IMAGE_SRC)
star_image_smaller = star_image.resize((50, 50), Image.LANCZOS)
star_image_tk = ImageTk.PhotoImage(star_image_smaller)
main_left_top_small_rectangle_canvas.create_image(50, 50, image=star_image_tk)
main_left_top_small_rectangle_canvas.image = star_image_tk
main_left_top_small_rectangle_canvas.create_text(160, 50, text=f"Total Exp: {PLACEHOLDER_EXP}", font=("Futura Display", 24))


# pick avatar according to level and place it on the main left big rectangle
avatar_path = pick_avatars_path(PLACEHOLDER_LEVEL, PLACEHOLDER_GENDER, avatars)
avatar_semi = Image.open(avatar_path)
avatar_semi_resized = avatar_semi.resize((280, 340), Image.LANCZOS)
avatar_image = ImageTk.PhotoImage(avatar_semi_resized)
main_left_big_rectangle_canvas.create_image(150, 210, image=avatar_image)
main_left_big_rectangle_canvas.image = avatar_image





# main_window.after(2000, lambda: close_window(main_window))
tk.mainloop()
