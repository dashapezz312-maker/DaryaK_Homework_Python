def is_year_leap(year):
    year = int(input("Введите год: "))
    if (year % 4 == 0):
        print("True")
    else:
        print("False")


is_year_leap(0)


def is_year_leap_2(year_2):
    if (year_2 % 4 == 0):
        return True
    else:
        return False


year_2 = 2020
result = is_year_leap_2(year_2)
print(f"год {year_2}: {result}")
