def kik_rik(age, name):
    bim = "Цена на {1} состовляет {0}."
    return bim.format(age, name)
age = 150
name = "яблоки"
kik_rik = kik_rik(age, name)
print(kik_rik)
   