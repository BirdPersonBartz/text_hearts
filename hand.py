from random import shuffle


players = ['Maggie','Kevin', 'Rory','Mom','Griff']
suits = ['hearts','diamonds','spades','clubs']
ranks = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
cards = [(suit, rank) for suit in suits for rank in ranks]
card_round = 0
players_hold = {}
round_order = None
#round_order = ['L','R','A','K','L','R','A','K','L','R','A','K','L','R','A','K','L','R','A','K']


player_choices = { 'Maggie':[('hearts', 'A'), ('hearts', 6), ('hearts', 'J')],
                    'Kevin':[('hearts', 2), ('hearts', 7), ('hearts', 'Q')],
                    'Rory':[('hearts', 3), ('hearts', 8), ('hearts', 'K')],
                    'Mom':[('hearts', 4), ('hearts', 9), ('diamonds', 'A')],
                    'Griff':[('hearts', 5), ('hearts', 10), ('diamonds', 2)]
                    }



def shuffle_deck(cards):
    shuffle(cards)
    return cards

def deal_deck(cards, players):
    count_p = len(players)
    remainder = len(cards) % count_p
    hole_cards = cards[-remainder:]
    del cards[-remainder:]
    splitdeck = (cards[i::count_p] for i in range(count_p))
    players_cards = zip(players, splitdeck)
    return players_cards, hole_cards


players_cards = [('Maggie', [('hearts', 'A'), ('hearts', 6), ('hearts', 'J'), ('diamonds', 3), ('diamonds', 8), ('diamonds', 'K'), ('spades', 5), ('spades', 10), ('clubs', 2),
                    ('clubs', 7)]), ('Kevin', [('hearts', 2), ('hearts', 7), ('hearts', 'Q'), ('diamonds', 4), ('diamonds', 9), ('spades', 'A'), ('spades', 6), ('spades', 'J'),
                    ('clubs', 3), ('clubs', 8)]), ('Rory', [('hearts', 3), ('hearts', 8), ('hearts', 'K'), ('diamonds', 5), ('diamonds', 10), ('spades', 2), ('spades', 7),
                    ('spades','Q'), ('clubs', 4), ('clubs', 9)]), ('Mom', [('hearts', 4), ('hearts', 9), ('diamonds', 'A'), ('diamonds', 6), ('diamonds', 'J'), ('spades', 3),
                    ('spades', 8), ('spades', 'K'), ('clubs', 5), ('clubs', 10)]), ('Griff', [('hearts', 5), ('hearts', 10), ('diamonds', 2), ('diamonds', 7), ('diamonds', 'Q'),
                    ('spades', 4), ('spades', 9), ('clubs', 'A'), ('clubs', 6), ('clubs', 'J')])]

def pass_style(players):
    if len(players) == 4:
        round_order = ['L','R','A','K','L','R','A','K','L','R','A','K','L','R','A','K','L','R','A','K','L','R','A','K']
    else:
        round_order = ['L','R','K','L','R','K','L','R','K','L','R','K','L','R','K','L','R','K','L','R','K','L','R','K']
    return round_order

def take_cards(players_cards, player_choices):
    for player_name, players_hand in players_cards:
        hold_cards =[x for x in players_hand if x not in(player_choices[player_name])]
        players_hold[player_name] = hold_cards
    return players_hold

def passing(player, pass_to, players_hold):
    update_hand = players_hold[pass_to] + (player_choices[player])
    players_hold[pass_to] = update_hand
    return players_hold

def pass_em(players_cards, player_choices, players, card_round):
    round_order = pass_style(players)
    direction = round_order[card_round]
    players_hold = take_cards(players_cards, player_choices)
    for p in players:
        if direction == 'L':
            pass_to = players[(players.index(p)-1)]
            players_hold = passing(p, pass_to, players_hold)
        elif direction == 'R':
            pass_to = players[(players.index(p)+1)]
            players_hold = passing(p, pass_to, players_hold)
        elif direction =='A':
            pass_to = players[(players.index(p)+2)]
            players_hold = passing(p, pass_to, players_hold)
        else:
            pass_to = p
            players_hold = passing(p, pass_to, players_hold)
    print("++++")
    print(players_hold)



#players_cards, hole = deal_deck(cards, players)
pass_em(players_cards, player_choices, players,card_round)
