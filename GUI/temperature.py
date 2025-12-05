class Temperature:
    def __init__(self, celsius: float):
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, celsius: float):
        if celsius < -273.15:
            raise ValueError("celsius must be >= -273.15")
        self._celsius = celsius

    @property
    def fahrenheit(self) -> float:
        return (self.celsius * 9) / 5 + 32
    @ fahrenheit.setter
    def fahrenheit(self, fahrenheit: float):
        if fahrenheit < -459.67:
            raise ValueError("fahrenheit must be >= -457.67")
        self._celsius = (fahrenheit-32) * 5 / 9

    @property
    def kelvin(self) -> float:
        return (self.celsius + 273.15)
    @ kelvin.setter
    def kelvin(self, kelvin: float):
        if kelvin < -459.67:
            raise ValueError("fahrenheit must be >= -457.67")
        self._celsius = kelvin - 273.15

if __name__ == '__main__':
    temp = Temperature(celsius=55)
    print(temp.celsius)
    print(temp.fahrenheit)
    print(temp.kelvin)
    temp.farenheit = 72
    print(temp.celsius)
    print(temp.farenheit)
    print(temp.kelvin)

