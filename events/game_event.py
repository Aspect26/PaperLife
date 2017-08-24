from abc import abstractmethod


class GameEvent(object):

    @abstractmethod
    def handle(self):
        pass

    def __gt__(self, obj):
        return True
