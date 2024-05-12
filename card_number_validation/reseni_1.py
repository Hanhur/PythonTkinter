# Luhn algoritmus
card_number = '5011054488597827'

# priprava promennych pro soucty
sum_odd_numders = 0
sum_even_number = 0

for index, value in enumerate(card_number):
    value = int(value)
    if index % 2 != 0:
        sum_odd_numders += value
    else:
        value *= 2
        if value >= 10:
            value = str(value)
            first_number = int(value[0])
            second_number = int(value[1])
            sum_even_number += first_number + second_number
        else:
            sum_even_number += value

if (sum_even_number + sum_odd_numders) % 10 == 0:
    print('Karta je validni')
else:
    print('Karta neni validni')