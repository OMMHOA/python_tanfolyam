# video link: https://www.youtube.com/watch?v=hE1ZJZAdPik&list=PLeCGdhCeJ1Ulh-kGUMsc6ok-IPJyCMO9j&index=12
# codeskulptor link: https://py3.codeskulptor.org/#user301_OEgi628KiQ_1.py

def list_average(list):
    print("A lista amit atlagolok: %s" % list)
    return sum(list) / len(list)

mylist = [2, 3]
average = list_average(mylist)
print(average)

def manipulate(extra, list, extra2 = None):
    print(extra2)
    list.append(4)
    
manipulate(list = mylist, extra = None)
print(mylist)

manipulate(list = mylist, extra = None, extra2 = "manipulalas")
print(mylist)

def unite_string(original, *rest):
    for i in rest:
        original += i
    return original

united = unite_string('Repa, ', 'retek, ', 'mogyoro. ')
print(united)
united = unite_string(united, 'Koran reggel ', 'ritkan ', 'rikkant a rigo.')
print(united)

osszeg = lambda a, b = 4: a + b
print(osszeg(2, 3))
print(osszeg(2))

