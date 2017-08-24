import json
import os
import traceback
from typing import Tuple

import pygame

from city.city import City
from game.constants import GameSettings
from game.user_event_dispatcher import UserEventDispatcher
from game.state import NormalState, PlacingNewBuildingState, GameState
from rendering.renderer import Renderer
from timing.game_timer import GameTimer
from ui.ui import UI


class Game(object):
    def __init__(self):
        self._SAVE_FILE_PATH = 'save.plsf'
        pygame.init()
        self._done = False
        self._event_dispatcher = UserEventDispatcher(self)
        self._renderer = Renderer(GameSettings.Screen.WIDTH, GameSettings.Screen.HEIGHT)
        self._timer = GameTimer()
        self._city = self.load_city()
        self._ui = UI(self)
        self._state = NormalState()

    def start(self) -> None:
        self._timer.reset()
        while not self._done:
            for user_event in pygame.event.get():
                self._event_dispatcher.dispatch(user_event)
            self._city.simulate()
            self._renderer.render(self._city, self._ui)

    def get_city(self) -> City:
        return self._city

    def get_state(self) -> GameState:
        return self._state

    def set_state(self, state: GameState) -> None:
        self._state = state

    def toggle_grid(self) -> None:
        self._ui.toggle_grid()

    def toggle_buildings_window(self) -> None:
        self._ui.toggle_buildings_window()

    def handle_mouse_down(self, position: Tuple) -> None:
        if type(self._state) is NormalState:
            self._ui.handle_mouse_down(position)

    def handle_mouse_up(self, position: Tuple) -> None:
        if type(self._state) is NormalState:
            self._ui.handle_mouse_up(position)
        elif type(self._state) is PlacingNewBuildingState:
            building = self._state.building
            building.set_position(
                (position[0] / GameSettings.Game.FIELD_SIZE, position[1] / GameSettings.Game.FIELD_SIZE))
            if not self._city.is_rectangle_ocuppied(building.position):
                self._city.add_building(building)
                self._state = NormalState()

    def save_game(self) -> None:
        json_data = self._city.jsonify()
        with open(self._SAVE_FILE_PATH, 'w') as save_file:
            save_file.write(json.dumps(json_data, indent=4))

    def load_city(self) -> City:
        city = City()
        if os.path.isfile(self._SAVE_FILE_PATH):
            with open('save.plsf') as save_file:
                data = json.load(save_file)
            try:
                city.load(data)
            except Exception:
                traceback.print_exc()
                city = City()

        return city

    def end_game(self) -> None:
        self.save_game()
        self._done = True
