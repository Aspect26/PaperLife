from events.user_events.user_event import UserEvent


class ToggleBuildingsWindowEvent(UserEvent):

    def handle(self, game_object) -> None:
        game_object.toggle_buildings_window()
