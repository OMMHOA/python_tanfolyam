# video link: https://www.youtube.com/watch?v=-VVJUpxuCqc&list=PLeCGdhCeJ1Ulh-kGUMsc6ok-IPJyCMO9j&index=6
# codeskulptor link: https://py2.codeskulptor.org/#user43_3yfMRsRm3r_0.py

min = 0
max = 100
tipp = 50
vege = False

while not vege:
    valasz = raw_input("%d?" % tipp)
    if valasz == "nagyobb":
        min = tipp
    elif valasz == "kisebb":
        max = tipp
    elif valasz == "igen":
        print 'yaaay'
        vege = True
    tipp = (max - min) / 2 + min

