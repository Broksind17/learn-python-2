def bas():
    sad = []
    
    for x in range(5):
        fad = int(input(f"Число {x + 1}:"))
        sad.append(fad)
    chisla = sum(1 for fad in sad if fad % 2 == 0)     
        
    
    print("Количество четных чисел:", chisla)
    
bas()    