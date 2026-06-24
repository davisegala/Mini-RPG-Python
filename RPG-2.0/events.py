import functions as f

def background_choise():
    rejection_count = 0
    valid_choice = False

    while not valid_choice:
        backstory_input = input('''
        Your choice will determine your history. Pick a background story:\n
        - [1] \033[1mMagic Apprentice\033[0m – You study under a grumpy wizard who never says "good job".\n
        - [2] \033[1mCity Guard\033[0m – You protect the gates, but dream of exploring beyond them.\n
        - [3] \033[1mCursed Merchant\033[0m – You sell goods by day, but turn into a shadow at night.\n
        ''').strip().lower()

        if backstory_input == '1':
            print("\nAs a Magic Apprentice, you grab your spellbook and head out to prove your grumpy master wrong.")
            f.player_status['src'] += 2
            valid_choice = True
            
        elif backstory_input == '2': 
            print("\nAs a City Guard, you quietly leave your post, ready to finally explore the world beyond the gates.")
            f.player_status['str'] += 2
            valid_choice = True
            
        elif backstory_input == '3':
            print("\nAs a Cursed Merchant, you close your shop for the night and feel the shadow within you stir.")
            f.player_status['src'] += 1
            f.player_status['str'] += 1
            valid_choice = True
            
        # Rejection
        elif backstory_input in ["i'm reject the past", "i am reject the past", "reject", "im reject the past"]:
            rejection_count += 1
            if rejection_count >= 3:
                print('\nDo you need to reject your past? HAHAHAHA! How arrogant! I wish you luck... You will need it...')
                f.player_status['difficult'] = 0.5 
                valid_choice = True
            if valid_choice != True:
                print("\nInvalid option. Choose a number")
        else:
            print("\nInvalid option. Choose a number")
            rejection_count += 1