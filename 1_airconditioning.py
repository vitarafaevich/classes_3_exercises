class AirConditioning:
    """
    Class representing AirConditioning managing system.
    """
    min_temp = 0
    max_temp = 43
    base_temp = 18


    def __init__(self, status = False, temperature = None):
         self.__status = status
         self.__temperature = temperature


    def __str__(self):
        if self.__status is True:
            return f'Conditioner is on. Temperature settings: {self.__temperature} degrees celsius.'
        else:
            return f'Conditioner is off.'


    @property
    def status(self):
        return self.__status


    @status.setter
    def status(self, stat):
        """
        Method status(self, stat): to set conditioner status
        :param stat: new status (status info; temp condition)
        """
        if isinstance(stat, tuple) is True:
            #if we have data about temp
            if stat[1] is True:
                self.__status = stat[0]


    @property
    def temperature(self):
        return self.__temperature


    @temperature.setter
    def temperature(self, temp):
        """
        Method temperature(self, temp): to set conditioner temperature
        :param temp: new temp (temp info; status condition)
        """
        if isinstance(temp, tuple) is True:
            #if conditioner is on
            if temp[1] is True:
                self.__temperature = temp[0]


    def switch_on(self):
        """
        Method switch_on(self): to switch the conditioner on, unable while conditioner is on
        """
        if self.__status is False:
            self.status = (True, True)
            self.temperature = (self.base_temp, True)


    def switch_off(self):
        """
        Method switch_off(self): to switch the conditioner on, unable while conditioner is off
        """
        if self.__status is True:
            self.status = (False, True)
            self.temperature = (None, True)


    def reset(self):
        """
        Method reset(self): to reset condition to base settings
        """
        if self.__status is True:
            self.status = (True, True)
            self.temperature = (self.base_temp, True)


    def get_temperature(self):
        """
        Method get_temperature(self): to get current temperature on the conditioner
        """
        if self.__status is True:
            return self.__temperature


    def raise_temperature(self):
        """
        Method raise_temperature(self): to raise temperature
        """
        if self.__status is True and self.__temperature is not None:
            if self.__temperature < self.max_temp:
                self.temperature = (self.__temperature + 1, True)


    def lower_temperature(self):
        """
        Method raise_temperature(self): to lower temperature
        """
        if self.__status is True and self.__temperature is not None:
            if self.__temperature > self.min_temp:
                self.temperature = (self.__temperature - 1, True)


conditioning = AirConditioning()
print(conditioning)
print(conditioning.temperature)
print(conditioning.status)
conditioning.status = True
print(conditioning)
print(conditioning.status)
conditioning.temperature = 20
print(conditioning.temperature)
conditioning.reset()
print(conditioning)
print(conditioning.get_temperature())
conditioning.raise_temperature()
print(conditioning.get_temperature())
conditioning.lower_temperature()
print(conditioning.get_temperature())
conditioning.switch_on()
print(conditioning)
print(conditioning.get_temperature())
print(conditioning.temperature)
conditioning.temperature = 30
print(conditioning.temperature)
conditioning.status = False
print(conditioning)
for _ in range(16):
    conditioning.lower_temperature()
print(conditioning.get_temperature())
for _ in range(5):
    conditioning.lower_temperature()
print(conditioning.get_temperature())
for _ in range(40):
    conditioning.raise_temperature()
print(conditioning)
for _ in range(5):
    conditioning.raise_temperature()
print(conditioning)
conditioning.switch_off()
print(conditioning)

