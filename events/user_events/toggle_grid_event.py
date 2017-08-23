from events.user_events.user_event import UserEvent


class ToggleGridEvent(UserEvent):

    def handle(self, game_object) -> None:
        game_object.toggle_grid()
