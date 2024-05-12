import base64
import zlib
from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('Komprese a Dekomprese souboru')
root.geometry('1000x500')
root.resizable(False, False)

# Functions
def upload_file():
    global select_file_path
    select_file_path = filedialog.askopenfilename()
    if select_file_path:
        # print(f'Vybervy soubor: {select_file_path}')
        # file_name_label['text'] = select_file_path
        file_name_label.config(text = f'{select_file_path}')

def compress_file():
    global select_file_path
    if select_file_path:
        try:
            # Nacteni tetxtovych dat ze souboru
            with open(select_file_path, 'r') as file:
                data = file.read()

            # Prevod textovych dat na bajty (byte)
            data_bytes = bytes(data, 'utf-8')

            # Komprese dat - vysledna data budou byte
            compressed_data = zlib.compress(data_bytes)

            # Zakodovani komprimonavych dat do formatu base64
            compressed_data_base64 = base64.b64encode(compressed_data)

            # moznost - zapsat data compressed_data_base64 do souboru jako text
            decoded_data = compressed_data_base64.decode('utf-8')
            with open('compressed.txt', 'w') as compressed_file:
                compressed_file.write(decoded_data)
        except Exception as error:
            print(f'Nastala chyba pri komprese souboru: {error}')
    else:
        print('Neni vybran soubor pro kompresi')


def decompress_file():
    global select_file_path
    if select_file_path:
        try:
            # Nacteni textovuch dat ze souboru
            with open(select_file_path, 'r') as file:
                compressed_data_base64 = file.read()

            # Dekodovani dat x base64 zpet na byte
            compressed_data = base64.b64decode(compressed_data_base64)

            # Dekomprese dat zpet na puvodni format byte
            decompressed_data_bytes = zlib.decompress(compressed_data)

            # Prevod dekomprimovanych bajtovych dat zpet na retezec
            decompressed_data = decompressed_data_bytes.decode('utf-8')

            with open('decompressed.txt', 'w') as decompressed_file:
                decompressed_file.write(decompressed_data)
        except Exception as error:
            print(f'Nastala chyba pri dekomprese souboru: {error}')
    else:
        print('Neni vybran soubor pro dekompresi')


# Upload button
upload_button = Button(text = 'Vyberte soubor', command = upload_file)
upload_button.grid(row = 0, column = 0)

# Label with file name
file_name_label = Label()
file_name_label.grid(row = 0, column = 1)

# Compresse button
compress_button = Button(text = 'Compressed', command = compress_file)
compress_button.grid(row = 1, column = 0)

# Compresse button
decompress_button = Button(text = 'Decompressed', command = decompress_file)
decompress_button.grid(row = 2, column = 0)



root.mainloop()