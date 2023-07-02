""" PowerBall Generator
Sets the play option to 'y' so the code will run automatically once. 
After, it'll ask the user each time to run. When it runs, it starts with 3 lists. 
The first is for the white balls from 1-69, the second is for the red balls from 1-25, 
and the last is an empty list to store 5 random numbers from the white ball list. 
Next, the power ball is picked at random. Then the for loop will repeat 5 times,
picking a random number from the white balls list, appending it to the empty ticket
numbers list, and removing the value so it doesn't get used again. Finally, we print the winning
numbers in a sorted order and ask them to play again. 
"""
import random
PLAY = 'y'

while PLAY == 'y':
    white_ball = list(range(1, 70))
    red_ball = list(range(1, 26))
    ticket_numbers = []
    powerball = random.choice(red_ball)

    for i in range(5):
        random_num = random.choice(white_ball)
        ticket_numbers.append(random_num)
        white_ball.remove(random_num)
    ticket_numbers = sorted(ticket_numbers)
    print(f"\nYour numbers are {', '.join(map(str, ticket_numbers))}", end=' ')
    print(f"and the PowerBall is {powerball}")

    PLAY = input('Do you want to PLAY again? Y/N ').lower()

print('Thanks for playing')
