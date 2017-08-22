import time


class GameTimer(object):

    def __init__(self):
        self._last_time = time.perf_counter()

    def reset(self) -> None:
        self._last_time = time.perf_counter()

    def tick(self) -> int:
        now = time.perf_counter()
        delta = now - self._last_time
        self._last_time = now

        return delta

