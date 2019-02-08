
class Player:
    VERSION = "Gopnik_FM_ver_1.0"



    def betRequest(self, game_state):
        print('-------------------------HELLLLLLOOOOO------------------------------')
        our_bet = 0
        values = {'2': 2,
                  '3': 3,
                  '4': 4,
                  '5': 5,
                  '6': 6,
                  '7': 7,
                  '8': 8,
                  '9': 9,
                  '10': 10,
                  'J': 11,
                  'Q': 12,
                  'K': 13,
                  'A': 14}


        #-----------------------CARDS----------------------------
        cards_on_table = []
        try:
            for card in game_state["community_cards"]:
                cards_on_table.append(card["rank"])
        except Exception:
            print('-----------------------------ERROR 1---------------------------')


        stack = 0
        our_cards = None
        try:
            for players in game_state["players"]:
                if players["name"] == "Gopnik FM":
                    our_cards = players["hole_cards"]
                    stack = players["stack"]
        except Exception:
            print('-----------------------------ERROR 2---------------------------')


        collection = our_cards + cards_on_table

        try:
            collection.sort(key=lambda x: values[x])
        except Exception:
            print('-----------------------------ERROR 3---------------------------')
        #---------------------------------------------------------


        cards = {}
        try:
            for card in collection:
                if card not in cards:
                    cards[card] = 1
                else:
                    cards[card] += 1
        except Exception:
            print('-----------------------------ERROR 4---------------------------')


        try:
            for rank,number in cards.items():
                if number == 2 and values[rank] >= 10:
                    our_bet += game_state["current_buy_in"] * 1.25
        except Exception:
            print('-----------------------------ERROR 5---------------------------')


        try:
            for rank,number in cards.items():
                if number == 3 and values[rank] >= 5:
                    our_bet = game_state["current_buy_in"] * 1.5
        except Exception:
            print('-----------------------------ERROR 6---------------------------')

        card_cnt = 0
        try:
            for i in range(len(collection) - 1):
                if values[collection[i + 1]] - values[collection[i]] > 1:
                    card_cnt = 0
                else:
                    card_cnt += 1

                if card_cnt == 4:
                    our_bet = game_state["current_buy_in"] * 1.75
                    break
        except Exception:
            print('-----------------------------ERROR 7---------------------------')

        if our_bet > stack:
            our_bet = stack

        return our_bet


    def showdown(self, game_state):
        pass








