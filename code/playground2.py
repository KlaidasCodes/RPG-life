import os
import binascii
import hashlib
import json
from tkinter import *
from PIL import Image, ImageTk


LIGHT_ORANGE = "#ffbc5c"
LIGHTER_ORANGE = "#EBDDC9"

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



with open("./database_main.json", mode="r+") as file:
            main_database = json.load(file)

main_window = Tk()

main_window.config(width=800, height=600, bg=LIGHT_ORANGE)
main_window.minsize(width=800, height=600)
for i in range(20):
    main_window.columnconfigure(i, weight=1)
    main_window.rowconfigure(i, weight=1)

corner = Canvas(main_window, width=1, height=1, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
corner.grid(column=0, row=0)

main_left_big_rectangle_canvas = Canvas(main_window, width=300, height=420, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
main_left_big_rectangle_canvas.grid(column=1, columnspan=8, row=3, rowspan=14, sticky="w", padx=20)
main_left_big_rectangle_canvas_rectangle = draw_rounded_rectangle(main_left_big_rectangle_canvas, 0, 0, 300, 420, fill=LIGHTER_ORANGE)

main_left_small_rectangle_canvas = Canvas(main_window, width=300, height=60, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
main_left_small_rectangle_canvas.grid(column=1, columnspan=8, row=17, rowspan=2, sticky="nw", padx=20, pady=20)
main_left_small_rectangle_canvas_rectangle = draw_rounded_rectangle(main_left_small_rectangle_canvas, 0, 0, 300, 60, radius=15, fill=LIGHTER_ORANGE)

main_right_big_rectangle_canvas = Canvas(main_window, width=420, height=420, bg=LIGHT_ORANGE, bd=0, highlightthickness=0)
main_right_big_rectangle_canvas.grid(column=9, columnspan=11, row=3, rowspan=14, sticky="e", padx=20)
main_right_big_rectangle_canvas_rectangle = draw_rounded_rectangle(main_right_big_rectangle_canvas, 0, 0, 420, 420, fill=LIGHTER_ORANGE)

main_name_canvas = Canvas(main_window, width=200, height=60, bg=LIGHTER_ORANGE, bd=0, highlightthickness=0)
main_name_canvas.grid(column=2, columnspan=6, row=14, rowspan=2)
main_name_canvas.create_text(100, 30, text="Maximus", font=("Futura Display", 44))






main_window.after(2000, lambda: close_window(main_window))
mainloop()
