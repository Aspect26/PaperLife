from abc import abstractmethod


class GameEvent(object):

    @abstractmethod
    def handle(self):
        pass
