def kik_rik(age):
    if age < 18:
        return "Вы еще несовершенолетний"
    elif 18 <= age <= 65:
        return "Вы взрослый"
    else:
        return "Вы пенсионер"
    
age = 20
print(kik_rik(age))