from gtts import gTTS # google tetx to speech
import os
from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Konvertor testu na rec')
root.geometry('350x350')
root.resizable(False, False)

# Functions
def translate_text(entry, language, audio_file_name):
    try:
        text_to_audio = entry
        output = gTTS(text = text_to_audio, lang = language, slow = False)
        output.save(f'{audio_file_name}.mp3')
        os.system(f'start {audio_file_name}.mp3')
    except Exception as error:
        print(f'Nastala chyba: {error}')

# Main lable 
main_label = Label(text = 'Konvertor')
main_label.grid(row = 0, column = 1)

# Language section
language_lable = Label(text = 'Vybertejazyk: ')
language_lable.grid(row = 1, column = 0)

language_drop_down = ttk.Combobox(
    state = 'readonly',
    values = ['cs', 'en'],
    width = 25
)
language_drop_down.grid(row = 1, column = 1)

# Text section 
text_label = Label(text = 'Vlozte text: ')
text_label.grid(row = 2, column = 0)

text_entry = Entry(width = 25)
text_entry.grid(row = 2, column = 1)

# Audio file name section
audio_label = Label(text = 'Nazev souboru: ')
audio_label.grid(row = 3, column = 0)

audio_entry = Entry(width = 25)
audio_entry.grid(row = 3, column = 1)

# Button section
translate_button = Button(text = 'Prelozit', command = lambda:translate_text(text_entry.get(), language_drop_down.get(), audio_entry.get()))
translate_button.grid(row = 4, column = 1)

root.mainloop()