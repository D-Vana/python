class Television:
    MIN_VOLUME = 0 
    MAX_VOLUME = 2  
    MIN_CHANNEL = 0 
    MAX_CHANNEL = 3 

    def __init__(self):
        """
        Sets the base variables for the TV.
        """
        self._status = False 
        self._muted = False
        self._volume = Television.MIN_VOLUME
        self._channel = Television.MIN_CHANNEL

    def power(self):
        """
        Turns the power on and off.
        """
        self._status = not self._status

    def mute(self):
        """
        Sets volume to zero.
        """
        if self._status:
            self._muted = not self._muted

    def channel_up(self):
        """
        Method to increase TV channel.
        """
        if self._status:
            if self._channel < Television.MAX_CHANNEL:
                self._channel += 1
            else:
                self._channel = Television.MIN_CHANNEL 

    def channel_down(self):
        """
        Method to decrease TV channel.
        """
        if self._status:
            if self._channel > Television.MIN_CHANNEL:
                self._channel -= 1
            else:
                self._channel = Television.MAX_CHANNEL 

    def volume_up(self):
        """
        Method to increase volume.
        """
        if self._status:
            self._muted = False 
            if self._volume < Television.MAX_VOLUME:
                self._volume += 1

    def volume_down(self):
        """
        Method to decrease volume.
        """
        if self._status:
            self._muted = False 
            if self._volume > Television.MIN_VOLUME:
                self._volume -= 1 

    def __str__(self):
        """
        Displays the current stats on the TV.
        """
        volume = Television.MIN_VOLUME if self._muted else self._volume  
        return f'Power = {self._status}, Channel = {self._channel}, Volume = {volume}'