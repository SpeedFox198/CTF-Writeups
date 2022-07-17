import time 
import random

print('''

██╗░░██╗░██████╗░██╗░░░██╗███████╗░██████╗░██████╗███████╗██████╗░
╚██╗██╔╝██╔════╝░██║░░░██║██╔════╝██╔════╝██╔════╝██╔════╝██╔══██╗
░╚███╔╝░██║░░██╗░██║░░░██║█████╗░░╚█████╗░╚█████╗░█████╗░░██████╔╝
░██╔██╗░██║░░╚██╗██║░░░██║██╔══╝░░░╚═══██╗░╚═══██╗██╔══╝░░██╔══██╗
██╔╝╚██╗╚██████╔╝╚██████╔╝███████╗██████╔╝██████╔╝███████╗██║░░██║
╚═╝░░╚═╝░╚═════╝░░╚═════╝░╚══════╝╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝
''')
print('Hello! Help me create a deck of cards to calculate a random product!')

count = 0
cards = []
print('''
        1. Add a card
        2. Generate random product and guess
    ''')
t = 0
while count < 1000:
    choice = input('> ')
    if choice == '1':
        num = int(input("What number is the card? "))
        start = time.time()
        cards.append(num)
        end = time.time()
        t += end - start
    elif choice == '2':
        start = time.time()
        n = cards[random.randint(0, len(cards) - 1)] * cards[random.randint(0, len(cards) - 1)]
        for i in cards:
            for j in cards:
                if i * j == n:
                    print(f'Guessed it! {i} * {j} = {n}')
        end = time.time()
        t += end - start
    print(t)
    count += 1

if t > 20:
    print("FLAG{REDACTED}")
