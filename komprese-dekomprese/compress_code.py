import base64
import zlib

# Nacteni tetxtovych dat ze souboru
with open('text.txt', 'r') as file:
    data = file.read()

# Prevod textovych dat na bajty (byte)
data_bytes = bytes(data, 'utf-8')

# Komprese dat - vysledna data budou byte
compressed_data = zlib.compress(data_bytes)

# Zakodovani komprimonavych dat do formatu base64
compressed_data_base64 = base64.b64encode(compressed_data)

# 1. moznost - zapsat data compressed_data_base64 do souboru
# with open('covpresse.txt', 'wb') as compressed_file:
#     compressed_file.write(compressed_data_base64)

# 2. moznost - zapsat data compressed_data_base64 do souboru jako text
decoded_data = compressed_data_base64.decode('utf-8')
with open('compressed.txt', 'w') as compressed_file:
    compressed_file.write(decoded_data)