def bin():
    
    vaf = []
    
    for x in range(3):
        nap = input(f"Элемент {x + 1}: ")
        vaf.append(nap)
   
    vaf.append("Кролик")
    #Второй вариант:
    #v = ("Кролик" ,)
    #vaf += v
        
    print(vaf)
    
bin()   