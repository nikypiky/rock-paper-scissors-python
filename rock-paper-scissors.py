import random


choices = ['rock', 'paper', 'scissors']
user_points = 0
computer_points = 0

while user_points < 5 and computer_points < 5:


    user_choice = input('Please select rock/paper/scissors: ').lower()
    if user_choice not in (choices):
        print('Please choose again')
        continue

    computer_choice = random.choice(choices)
    print(computer_choice)

    if user_choice == computer_choice:
        print('It\'s a tie!')
    elif (user_choice == 'rock' and computer_choice == 'paper') or (user_choice == 'paper' and computer_choice == 'scissors') or (user_choice == 'scissors' and computer_choice == 'rocke'):
        print('You loose!!')
        computer_points = computer_points + 1
    else: 
        print('You win!!')
        user_points = user_points + 1

    print('The score is: ' + str(user_points) + ' : ' + str(computer_points))
    
    print(user_points, computer_points)

print(user_points, computer_points)

if user_points > computer_points:
    print('You win!!')
else:
    print('You looser!!')