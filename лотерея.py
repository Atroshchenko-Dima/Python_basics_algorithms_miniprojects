from random import choice

def generator_ticket():
    ticket_alphabet = '0123456789ABCD'
    winner_ticker = [choice(ticket_alphabet) for _ in range(4)]
    print(f"Выйгрышный билет имеет номер {''.join(winner_ticker)}")
    

print(generator_ticket())



import random
 
number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", 'a', 'b', 'c', 'd', 'e', ]
 
my_ticket = ["3", "7", 'c', 'e']
print("Билет имеющий комбинацию", "".join(my_ticket), "является выигрышным!")
number_combinations = 0
while True:
    if my_ticket != random.sample(number, 4):
        number_combinations += 1
    if my_ticket == random.sample(number, 4):
        print("You win!")
        print(f"The winning combination was: {number_combinations}")
        break

