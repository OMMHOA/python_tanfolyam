# video link: https://www.youtube.com/watch?v=SMI7xAyTZZI&list=PLeCGdhCeJ1Ulh-kGUMsc6ok-IPJyCMO9j&index=9
# codeskulptor link: https://py2.codeskulptor.org/#user43_Nnh4S7m2JM_0.py

anna = "Anna", 19, True, ["Piros", "Kek"]

print anna
print "Szemely neve es eletkora: ", anna[0:2]
print "Infok szama szemelyrol: ", len(anna)

anna[3][0] = "Rozsaszin"
print anna[-1]

anna = (anna[0],) + (20,) + anna[2:4]
print anna[1]

gabor = ("Gabor",) + anna[1:4] + (False,)
print gabor

for i in gabor:
    print i

print False in gabor
    
del anna
#print anna

