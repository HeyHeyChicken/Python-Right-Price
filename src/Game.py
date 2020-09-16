import random
from Article import Article
from Player import Player


class Game:
    def __init__(self):
        self.articles = [
            Article("Vacuum"),
            Article("Smartphone"),
            Article("TV"),
            Article("Watch"),
            Article("Computer"),
            Article("Virtual reality headset")
        ]
        self.article = random.choice(self.articles)
        self.player = Player()
        self.price = random.randint(200, 800)

        self.init()

    def init(self):
        self.welcome()
        self.loop()

    def welcome(self):
        print("#####################################")
        print("# WELCOME TO THE \"RIGHT PRICE\" GAME #")
        print("#####################################")
        print("We are now playing for the following article : \"" + self.article.name + "\".")

    def loop(self):
        print("How much do you think this item costs ?")
        self.player.request_value()
        if self.player.proposal != self.price:
            if type(self.player.proposal) == type(0):
                if self.player.proposal > self.price:
                    print("It is less.")
                else:
                    print("It is more.")
            self.loop()
        else:
            print("BINGO ! You found the right price for our item in just {} round{}.".format(self.player.get_round(), "s" if self.player.get_round() > 1 else ""))
