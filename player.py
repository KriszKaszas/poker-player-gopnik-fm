
class Player:
    VERSION = "Gopnik_FM_ver_1.0"

    def betRequest(self, game_state):
        our_bet = 0
        our_cards = None

        for players in game_state["players"]:
            if players["name"] == "Gopnik FM":
                our_cards = players["hole_cards"]

        if our_cards[0]["rank"] == our_cards[1]["rank"] and our_cards[0]["rank"] in ["J", "K", "Q", "A"]:
            if game_state["current_buy_in"] == 0:
                our_bet = 100
            else:
                our_bet = game_state["current_buy_in"] * 2

        return our_bet

    def showdown(self, game_state):
        pass

