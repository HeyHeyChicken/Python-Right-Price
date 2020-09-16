class Player:
    def __init__(self):
        self.__round = 0
        self.proposal = 0

    def request_value(self):
        self.__round = self.__round + 1
        self.proposal = input()
        try:
            self.proposal = int(self.proposal)
        except:
            print("Cannot cast value \"{}\" from type \"{}\" to type \"{}\" !".format(self.proposal, type(self.proposal), type(0)))

    def get_round(self):
        return self.__round
