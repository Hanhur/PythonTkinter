# Luhn algoritmus
card_number = '5011054488597827'

# list comprehension
numbres = [
    int(one_number)
    for one_number in card_number
]
# odd - liche
sum_odd_positions = sum(numbres[1::2])

# even - sude
sum_even_positions = sum(
    (one_number * 2) % 9
    if one_number != 9 else 9
    for one_number in numbres[::2]
)
# overeni, zda je soucet delitelny 10
is_valid = (sum_even_positions + sum_odd_positions) % 10 == 0
print('Karta je validni' if is_valid else 'Karta neni validni')