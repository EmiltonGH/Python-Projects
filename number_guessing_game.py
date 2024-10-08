import random

# Initialize the best score
best_score = float('inf')  # Start with infinity for comparison

while True:
    # Get the range from the user
    while True:
        try:
            min_value = int(input('Enter the minimum value for the range: '))
            max_value = int(input('Enter the maximum value for the range: '))
            if min_value < max_value:
                break
            else:
                print('The minimum value should be less than the maximum value. Try again.')
        except ValueError:
            print('Please enter valid numbers for the range.')

    # Allow the user to set the maximum number of attempts
    while True:
        try:
            max_attempts = int(input('Enter the maximum number of attempts: '))
            if max_attempts > 0:
                break
            else:
                print('Number of attempts should be greater than 0.')
        except ValueError:
            print('Please enter a valid number for attempts.')

    # Generate a random number within the specified range
    number_to_guess = random.randint(min_value, max_value)

    # Game loop with limited attempts
    attempts = 0
    while attempts < max_attempts:
        try:
            guess = int(input(f'Guess the number between {min_value} and {max_value} (Attempt {attempts + 1}/{max_attempts}): '))
            attempts += 1
            if guess < number_to_guess:
                print('Too low!')
            elif guess > number_to_guess:
                print('Too high!')
            else:
                print('Congratulations! You guessed the number.')
                break
        except ValueError:
            print('Please enter a valid number.')
    else:
        print(f'Sorry, you ran out of attempts. The correct number was {number_to_guess}.')

    # Update best score if necessary
    if attempts < best_score:
        best_score = attempts
        print(f'New best score: {best_score} attempts!')
    else:
        print(f'Best score remains: {best_score} attempts.')

    # Ask if the user wants to play again
    play_again = input('Do you want to play again? (yes/no): ').strip().lower()
    if play_again != 'yes':
        break

print('Thank you for playing!')
