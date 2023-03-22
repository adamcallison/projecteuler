# https://projecteuler.net/problem=19
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

def count_sundays():
    month_days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    month_days = {j : x for j, x in enumerate(month_days)}
    day = 365 % 7 # day of first day of century (where Monday = 0)
    count = 1 if day == 7 else 0
    for year in range(1901, 2001):
        for month in range(12):
            day = (day + month_days[month]) % 7
            if ((year % 4) == 0) and (month == 1): day = (day + 1) % 7
            if day == 6: count += 1
    if day == 6: count -= 1 # in case 01/01/2001 is a Sunday
    return count

if __name__ == '__main__':
    print(count_sundays())


