import random
print('a')
storage = 0
table = random.randint(1, 3)
joker = 2
queen = 6
king = 6
ace = 6
win = False
wins = 0
ai_deck = []
player_deck = []
user1_deck = []  # колода первого пользователя
user2_deck = []  # колода второго пользователя


# gets the cards back into your deck
def refil_deck(deck):
    global joker, ace, queen, king
    while len(deck) < 4 and (joker > 0 or queen > 0 or king > 0 or ace > 0):
        jjj = random.randint(1, 4)
        if jjj == 1 and ace > 0:
            deck.append('ace')
            ace -= 1
        if jjj == 2 and king > 0:
            deck.append('king')
            king -= 1
        if jjj == 3 and queen > 0:
            deck.append('queen')
            queen -= 1
        if jjj == 4 and joker > 0:
            deck.append(joker)
            joker -= 1


# allows you to throw cards and play the game
def choose_card_to_throw(deck):
    print('Your current deck: ', deck)
    while True:
        try:
            num_to_throw = int(input("How many card are you gonnq throw(1-3)"))
            if 1 <= num_to_throw <= 3 and num_to_throw <= len(deck):
                break
            else:
                print("Invalid input, Please choose and valid number and make sure that there are enough cards")
        except ValueError:
            print("Enter a valid number")
        thrown_cards = []
        for i in range(num_to_throw):
            while True:
                card = input(f'choose a card to throw from {deck}: ').strip().lower()
                if card in deck:
                    deck.remove(card)
                    break
                else:
                    print('card not in hand. try again.')
    return thrown_cards


# установка начального значения 'storage'
if table == 1:
    storage = "ace table"
    print(storage)
elif table == 2:
    storage = "king table"
    print(storage)
else:
    storage = "queens table"
    print(storage)

for user in range(1, 3):  # проход по двум пользователям
    a = 0
    while a < 4:
        if wins == 6:
            win = True
        a = 0
        while a < 4:
            jjj = random.randint(1, 4)
            if jjj == 1 and ace > 0:
                if user == 1:
                    user1_deck.append("ace")
                else:
                    user2_deck.append("ace")
                ace -= 1
                a += 1
            elif jjj == 2 and king > 0:
                if user == 1:
                    user1_deck.append("king")
                else:
                    user2_deck.append("king")
                king -= 1
                a += 1
            elif jjj == 3 and queen > 0:
                if user == 1:
                    user1_deck.append("queen")
                else:
                    user2_deck.append("queen")
                queen -= 1
                a += 1
            elif jjj == 4 and joker > 0:
                if user == 1:
                    user1_deck.append("joker")
                else:
                    user2_deck.append("joker")
                joker -= 1
                a += 1
print("User 1 deck", user1_deck)
print("User 2 deck", user2_deck)


# Функция для получения заявления игрока на основе стола
def get_player_claim():
    if storage == "ace table":
        return "ace"
    elif storage == "king table":
        return "king"
    else:
        return "queen"


while user1_deck and user2_deck:
    # Ход первого игрока
    print("\nUser 1's turn:")
    card = user1_deck.pop(0)
    # Первый игрок делает заявление
    if card == "joker":
        # Джокер может заявлять любую карту
        possible_claims = ["ace", "king", "queen"]
        claim = random.choice(possible_claims)
    else:
        claim = get_player_claim()
    print(f"User 1 says: This is a {claim}.")

    # Реакция второго игрока
    user2_guess = input(f"User 2, is it True or False? ").strip().lower()
    if card == "joker":
        # Особые правила для джокера
        if user2_guess == "false":
            print(f"User 2 guessed correctly! The card was a joker.")
        else:
            print(f"User 2 guessed wrong! The card was a joker and is now removed.")

    else:
        if (card == claim and user2_guess == "true") or (card != claim and user2_guess == "false"):
            print(f"User 2 guessed correctly! The card was a {card}")
        else:
            print(f"User 2 guessed wrong! The card was a {card} and is now removed.")

        if not user1_deck or not user2_deck:
            break

        # user 2 turn
        print("\nUser 2's turn:")
        card = user2_deck.pop(0)
        if card == "joker":
            # Джокер может заявлять любую карту
            possible_claims = ["ace", "king", "queen"]
            claim = random.choice(possible_claims)
        else:
            claim = get_player_claim()
        print(f"User 2 says: This is a {claim}.")

        # user 1 reaction
        user1_guess = input(f"User 2, is it True or False? ").strip().lower()
        if card == "joker":
            # Особые правила для джокера
            if user1_guess == "false":
                print(f"User 2 guessed correctly! The card was a joker.")
            else:
                print(f"User 2 guessed wrong! The card was a joker and is now removed.")

        else:
            if (card == claim and user1_guess == "true") or (card != claim and user1_guess == "false"):
                print(f"User 2 guessed correctly! The card was a {card}")
            else:
                print(f"User 2 guessed wrong! The card was a {card} and is now removed.")

# определение победителя

if not user1_deck:
    print("\nUser 2 wins the game!")
elif not user2_deck:
    print('\nUser 1 wins the game')