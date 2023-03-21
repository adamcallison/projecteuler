# https://projecteuler.net/problem=17
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

def num_letters_up_to_1000():
    units_up_to_9 = 3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4
    from_11_to_19 = 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8
    ten, twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety = 3, 6, 6, 5, 5, 5, 7, 6, 6
    hundred = 7
    and_ = 3

    total = units_up_to_9
    total *= 9 # 1 to 9 for each ten except the 'teens'
    total += from_11_to_19 # add in the 'teens'
    total += ten+((twenty+thirty+forty+fifty+sixty+seventy+eighty+ninety)*10)# all up to 99
    total *= 10 # 1 to 99 for each hundred (no 'and's yet)
    total += units_up_to_9*100 # for the X in "X hundred and..."
    total += hundred*900
    total += and_*(900-9) # up to 999
    total += 3 + 8 # one thousand

    return total

if __name__ == '__main__':
    print(num_letters_up_to_1000())


