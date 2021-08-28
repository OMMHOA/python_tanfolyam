# video link: https://www.youtube.com/watch?v=52mOiERzEKY&list=PLeCGdhCeJ1Ulh-kGUMsc6ok-IPJyCMO9j&index=4
# codeskulptor link: https://py2.codeskulptor.org/#user42_tNIulgnqpCqtDTs.py

import math

a = 1
b = 1
c = 1

delta = b * b - 4 * a * c
if delta >= 0:
    x1 = (-1 * b + math.sqrt(delta)) / 2 * a
    x2 = (-1 * b - math.sqrt(delta)) / 2 * a
    print "A megoldasok: %d %d" % (x1, x2)
else:
    print "Nincs valos megoldas!"

