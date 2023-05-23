print()
print("Вітаю натхненних математиків!")
print()
while True:
    spysok1 = []
    a = int (input ("Введіть початкове число масиву: "))
    b = int (input ("Введіть останнє число масиву: "))
    print ()
    c = range (a, b+1)
    for d in c:
        if d %2 !=0 and d %3 !=0 and d %5 !=0 and d %7 !=0:
            spysok1.append (int (d))#створили список (типу масив...)
    print ()        
    from functools import reduce
    print("Найбільше просте число від", a,"до",b, ":  ", reduce(max, spysok1))
    print ()
    print ("Головний масив  ",(spysok1)) # kontrol meessedge, Del bihaind final
    
print ()
