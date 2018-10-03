from datetime import date


def count_sundays():
    count = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            d = date(year, month, 1)
            if d.weekday() == 6:
                count += 1
    return count

if __name__ == '__main__':
    print(count_sundays())
