# video link: https://www.youtube.com/watch?v=lmXbYfv3m2Y&list=PLeCGdhCeJ1Ulh-kGUMsc6ok-IPJyCMO9j&index=11
# codeskulptor link: https://py3.codeskulptor.org/#user301_tJSju9OdKr_0.py

import random

hand_to_value = {'ko': 0, 'papir': 1, 'ollo': 2}
delta_to_result = {0: 'egyenlo', 1: 'felhasznalo nyert', 2: 'gep nyert'}

user_hand = raw_input('A te kezed: ')
user_value = hand_to_value[user_hand]

cpu_hand = random.choice(hand_to_value.keys())
cpu_value = hand_to_value[cpu_hand]

print('A te kezed {}, a gep keze {}.'.format(user_hand, cpu_hand))

delta = (user_value - cpu_value) % 3
print('Az eredmeny: ' + delta_to_result[delta])

