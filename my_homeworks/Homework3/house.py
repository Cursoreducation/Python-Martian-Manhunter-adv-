class House:
    """
    This class describe a behavior of a House object.
    :param location: Place where house is located
    :type location: str
    :param area: Area of a house
    :type area: float, int
    :param cost: House price
    :type cost: int
    """
    def __init__(self, location: str, area: (float, int), cost: int):

        self._location = location
        self._area = area
        self._cost = cost

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        self._location = location

    @property
    def price_per_m2(self):
        return round(self._cost / self._area, 2)

    @property
    def area(self):
        return self._area

    @property
    def cost(self):
        return self._cost

    def apply_discount(self, discount=0.0):
        """
        Methods apply discount and updates house price accordingly.
        :param discount: amount of discount
        :type discount: float, optional
        :return: It returns updated house price
        :rtype: float
        """
        if discount > 0.0:
            self._cost = round(self._cost * (1 - discount), 2)
            return self._cost
        print('Unfortunately, there is not any discount for this house')
        return self._cost
