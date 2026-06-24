import functions as f
import events
import time
import random as ran

if input('Do you want start the game? [Y/N]\n').lower() == 'y':
    time.sleep(0.5)
    print("\nLoading...\n")
    time.sleep(1)
else:
    exit()

time.sleep(1)
print('\nThis game is in development. Please keep this in your mind.')
time.sleep(1)

events.background_choise()

time.sleep(1)
print("\nLet's start...\n")
time.sleep(1)

while True:
    monster = f.monsters[1].copy()
    f.combat(monster)
    f.player_status['hp'] = f.player_status['max_hp']