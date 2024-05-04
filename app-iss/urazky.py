import  requests
from tkinter import *

# Okno
window = Tk()
window.minsize(300, 300)
window.resizable(False, False)
window.title("Aplikace na urazky")
window.config(bg = "#042940")

# Function
def insult_me():
    user_language = drop_down_lang.get()
    my_parameters = {
        "lang": user_language,
        "type": "json"
    }

    response = requests.get("https://evilinsult.com/generate_insult.php", params = my_parameters)
    response.raise_for_status()
    data = response.json()
    insult_label.config(text = data["insult"])

# Roletka - jazyk urazek
drop_down_lang = StringVar(window)
drop_down_lang.set("cs")
drop_down_lang_options = OptionMenu(window, drop_down_lang, "en", "es", "fr", "cs", "ru")
drop_down_lang_options.config(bg = "#005C53", fg = "#D6D58E", font = ("Arial", 12))
drop_down_lang_options.pack(pady = 10)

# Button
insult_button = Button(text = "Chci urazit", command = insult_me, bg = "#005C53", fg = "#D6D58E", font = ("Arial", 12))
insult_button.pack(pady = 10)

# Label
insult_label = Label(wraplength = 250, bg = "#042940", fg = "#D6D58E", font = ("Arial", 14))
insult_label.pack()


window.mainloop()
