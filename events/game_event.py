from abc import abstractmethod


class GameEvent(object):

    def __gt__(self, obj) -> bool:
        return True

    @abstractmethod
    def handle(self) -> None:
        pass
