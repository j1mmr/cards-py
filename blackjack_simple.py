import os
from time import sleep
import cards

def get_score(hand):
    score = 0
    ace_count = 0
    for card in hand:
        value = card.value
        match value:
            case 'Ace':
                ace_count += 1
            case '2':
                score += 2
            case '3':
                score += 3
            case '4':
                score += 4
            case '5':
                score += 5
            case '6':
                score += 6
            case '7':
                score += 7
            case '8':
                score += 8
            case '9':
                score += 9
            case _:
                score += 10

    while ace_count > 0:
        if ace_count > 1:
            score += 1
            ace_count -= 1
        else:
            ace_count -= 1
            if score + 11 < 21:
                score += 11
            else:
                score += 1
    return score

clear_call = 'cls' if os.name == 'nt' else 'clear'

deck = cards.Deck()

player_can_hit = True
player_bust = False
dealer_bust = False

dealer_hand = []
player_hand = []

dealer_hand.append(deck.deal())
player_hand.append(deck.deal())
dealer_hand.append(deck.deal())
player_hand.append(deck.deal())

print("Dealer's First Card:")
print("\t" + str(dealer_hand[0]))

print("Player's Hand:")
for card in player_hand:
    print("\t" + str(card))


player_score = get_score(player_hand)

while player_can_hit:
    if input("Hit? (y/N):\t").upper()[0] != 'Y':
        player_can_hit = False
    else:
        new_card = deck.deal()
        player_hand.append(new_card)
        print("You got:\t"+str(new_card))
        player_score = get_score(player_hand)
        if player_score > 21:
            player_can_hit = False
            player_bust = True
            print("Bust")
sleep(3)
os.system(clear_call)
if not player_bust:
    print("Dealer's Hand:")
    for card in dealer_hand:
        print("\t" + str(card))
    dealer_score = get_score(dealer_hand)
    while dealer_score < 17:
        new_card = deck.deal()
        print("Dealer hits for:\t"+str(new_card))
        dealer_hand.append(new_card)
        dealer_score = get_score(dealer_hand)
        if dealer_score > 21:
            print("Dealer Bust - You win!")
            dealer_bust = True
        sleep(0.5)
    sleep(3)
    if not dealer_bust:
        os.system(clear_call)
        print("Dealer's Hand:")
        for card in dealer_hand:
            print("\t" + str(card))

        print("Player's Hand:")
        for card in player_hand:
            print("\t" + str(card))

        if dealer_score > player_score:
            print("Dealer Wins")
        elif dealer_score == player_score:
            print("Push")
        else:
            print("Player Wins!")
