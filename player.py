
class Player:
    VERSION = "Gopnik_FM_ver_1.0"

    def betRequest(self, game_state):
        our_bet = 0
        our_cards = None
        cards_on_table = []

        for card in game_state["community_cards"]:
            cards_on_table.append(card["rank"])

        for players in game_state["players"]:
            if players["name"] == "Gopnik FM":
                our_cards = players["hole_cards"]

        if our_cards[0]["rank"] == our_cards[1]["rank"] and our_cards[0]["rank"] in ["J", "K", "Q", "A"]:
            if game_state["current_buy_in"] == 0:
                our_bet = 100
            elif our_cards[0]["rank"] in cards_on_table:
                our_bet = game_state["current_buy_in"] + 100
            else:
                our_bet = game_state["current_buy_in"] * 2

        if len(cards_on_table) > 3:
            our_bet = 0

        return our_bet

    def showdown(self, game_state):
        pass

