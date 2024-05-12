import base64
import zlib

# Nacteni textovuch dat ze souboru
with open('compressed.txt', 'r') as file:
    compressed_data_base64 = file.read()

# Dekodovani dat x base64 zpet na byte
compressed_data = base64.b64decode(compressed_data_base64)

# Dekomprese dat zpet na puvodni format byte
decompressed_data_bytes = zlib.decompress(compressed_data)

# Prevod dekomprimovanych bajtovych dat zpet na retezec
decompressed_data = decompressed_data_bytes.decode('utf-8')

with open('decompressed.txt', 'w') as decompressed_file:
    decompressed_file.write(decompressed_data)