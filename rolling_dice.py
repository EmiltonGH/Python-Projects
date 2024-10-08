import random

roll_count = 0
while True:
    choice = input("Are you ready to roll the dice? (y/n): ").lower()
    if choice == 'y':
        number_of_dice = int(input('How many dice would you like to roll?: '))
        dice_rolls = [random.randint(1,6) for _ in range(number_of_dice)]
        print(f'You rolled {dice_rolls}')
        roll_count += 1
    elif choice == 'n':
        print(f'Thanks for playing! You rolled the dice {roll_count} times.')
        break
    else:
        print('Invalid choice!')
