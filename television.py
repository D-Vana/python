class Television:
    MIN_VOLUME = 0

    def __init__(self):
        self._muted = False
        self._volume = Television.MIN_VOLUME

    def power(self):
        pass

    def mute(self):
        pass

    def channel_up(self):
        pass

    def channel_down(self):
        if self._status:
            if self._channel > Television.MIN_CHANNEL:
                self._channel -= 1
            else:
                self._channel = Television.MAX_CHANNEL
        else:
            pass

    def volume_up(self):
        if self._status:
            self._muted = False
            if self._volume < Television.MAX_VOLUME:
                self._volume += 1

    def volume_down(self):
        pass

    def __str__(self):
        if self._muted:
            return f'Volume = {Television.MIN_VOLUME}'
        else:
            return f'xxx'