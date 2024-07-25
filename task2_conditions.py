def kik_rik(year):
    if year % 4 == 0 and year % 100 !=  0 or year % 400 == 0:
        return "Является високосным годом"
    else:
        return "Не является високосным годом"
year = 2020
print(kik_rik(year))
       