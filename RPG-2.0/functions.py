import time
import random as ran

player_status = {
    'str':1,
    'src':1,
    'con':1,
    'level':1,
    'xp':0,
    'lun':100, #Xp for next level
    'hp':20,
    'max_hp':20,
    'def':0,
    'difficult':1,
}

monsters = [
    # Early game
    {'name': 'goblin', 'atk': 10, 'def': 3, 'hp': 20},
    {'name': 'slime', 'atk': 6, 'def': 1, 'hp': 15},
    {'name': 'wolf', 'atk': 12, 'def': 4, 'hp': 25},

    # Mid game
    {'name': 'skeleton', 'atk': 14, 'def': 5, 'hp': 30},
    {'name': 'bandit', 'atk': 16, 'def': 6, 'hp': 35},
    {'name': 'orc', 'atk': 20, 'def': 8, 'hp': 45},

    # Late game
    {'name': 'dark mage', 'atk': 22, 'def': 10, 'hp': 40},
    {'name': 'minotaur', 'atk': 28, 'def': 12, 'hp': 60},
    {'name': 'dragon whelp', 'atk': 35, 'def': 15, 'hp': 80},

    # Boss-tier
    {'name': 'ancient dragon', 'atk': 50, 'def': 20, 'hp': 150},
    {'name': 'lich king', 'atk': 45, 'def': 18, 'hp': 120}
]

def xp_gain():
    attribute_gain = 1 
    if player_status['difficult'] == 0.5:
        attribute_gain = 3
    
    while player_status['xp'] >= player_status['lun']:
        print(f"\nLeveled up to level {player_status['level'] + 1}!\n")
        player_status['level'] += 1
        player_status['xp'] -= player_status['lun']
        player_status['lun'] = int(player_status['lun'] * 1.3)

        for i in ['str', 'src', 'con']:
            player_status[i] += 1 * attribute_gain

        new_hp = 20 + player_status['con'] * 5
        player_status['max_hp'] = new_hp
        player_status['hp'] = new_hp

        print(f" Strength: {player_status['str']}, Magic: {player_status['src']}, Constitution: {player_status['con']}")
        print(f" XP: {player_status['xp']} | XP for next level: {player_status['lun']}\n")
        
def combat(monster):
    player_moveset = [
    {'name':'Lunge', 'damage': int(player_status['str'] * 2) + 4},
    {'name': 'Fire Ball', 'damage': int(player_status['src'] * 1.7) + 7},
    ]

    time.sleep(1)
    print('\nThe battle is starting...')
    time.sleep(1)
    print(f"\nYour opponent is a {monster['name']} with {monster['hp']} HP!\n")

    while monster['hp'] > 0 and player_status['hp'] > 0:

        print('Choise your move: \n')
        for i, move in enumerate(player_moveset, start=1):
            print(f"  [{i}] {move['name']} (Damage: {move['damage']})")
        try:
            choice = int(input("\nEnter the number of your move: ")) - 1
            if choice not in range(len(player_moveset)):
                print("Invalid choice! Try again.\n")
                continue
        except ValueError:
            print("Please enter a valid number!\n")
            continue
        player_move = player_moveset[choice]

        p_damage = max(player_move['damage'] - monster['def'], 0)
        m_damage = max(monster['atk'] - player_status['def'], 0)

        print(f'\nYou attack {monster['name']} with {player_move['name']}...')
        time.sleep(0.5)
        if ran.random() < 0.2:
            print('\nYour attack missed!')
        else:
            print(f'\nSuccessful hit! You dealt {p_damage} damage.')
            monster['hp'] -= p_damage
        
        time.sleep(0.5)
        
        if ran.random() < 0.2:
            print('\nYou missed!')
        else:
            print(f'\nYou received {m_damage} damage.')
            player_status['hp'] -= m_damage
        
        time.sleep(1)
        
        print(f"\nYour HP: {player_status['hp']} | {monster['name']} HP: {monster['hp']}\n")
       
        time.sleep(1)

    time.sleep(1)

    if player_status['hp'] <= 0:
        print('You were defeated...')
    else:
        print(f'You defeated {monster['name']}!')

    player_status['xp'] += (ran.randint(1, 30) + monster['atk'] * 1.5) * player_status['difficult']
    xp_gain()