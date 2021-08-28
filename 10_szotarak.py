# video link: https://www.youtube.com/watch?v=1oK_ZxTYi38&list=PLeCGdhCeJ1Ulh-kGUMsc6ok-IPJyCMO9j&index=10
# codeskulptor link: https://py3.codeskulptor.org/#user301_e12cJoHcnC_0.py

anna = {'nev': 'Kovacs Anna', 'kor': 16, 'osztaly': 3}
print(anna)
print(anna['nev'])

print('Annarol infok szama: %s' % len(anna))

anna['kor'] = 17
print(anna['kor'])


#print(anna['kedvenc_szinek'])
anna['kedvenc_szinek'] = ['Piros', 'Kek']
print(anna['kedvenc_szinek'])
print(anna)

szinek = anna['kedvenc_szinek']
szinek.append('Rozsaszin')
print(anna['kedvenc_szinek'][2])

nev = anna['nev']
nev = 'kiskutya'
print(anna['nev'])

print(anna.keys())
print(anna.values())

del anna['kedvenc_szinek']
#print(anna['kedvenc_szinek'])

anna.clear()
print(anna)

del anna
#print(anna)

