import tkinter as tk
from PIL import Image, ImageTk

PLACEHOLDER_LEVEL = 3
PLACEHOLDER_GENDER = "male"


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
    


root = tk.Tk()

avatar_path = pick_avatars_path(PLACEHOLDER_LEVEL, PLACEHOLDER_GENDER, avatars)

avatar = Image.open(avatar_path)
resized_avatar = avatar.resize((280, 340), Image.LANCZOS)
avatar_image = ImageTk.PhotoImage(resized_avatar)





canvas_test = tk.Canvas(width=800, height=800)
canvas_test.pack()

canvas_test.create_image(400, 400, image = avatar_image)
canvas_test.image = avatar_image






tk.mainloop()
