from abc import abstractmethod


class UserEvent(object):

    @abstractmethod
    def handle(self, game_object) -> None:
        pass
