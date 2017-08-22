from events.user_events.user_event import UserEvent


class ExitEvent(UserEvent):

    def handle(self, game_object) -> None:
        game_object.end_game()
