from abc import abstractmethod, ABC


class Room(ABC):
    def __init__(self, features, price):
        self._features = features
        self.__price = price

    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def get_features(self):
        pass


class WiFiService:
    def get_wifi_description(self):
        return "халявный вифи"


class BreakfastService:
    def get_breakfast_description(self):
        return "ням ням"


class StandardRoom(Room):
    def __init__(self, features, price):
        super().__init__(features, price)

    def get_price(self):
        return self._Room__price

    def get_features(self):
        return self._features


class LuxuryRoom(Room, WiFiService, BreakfastService):
    def __init__(self, features, price):
        Room.__init__(self, features, price)
        WiFiService.__init__(self)
        BreakfastService.__init__(self)

    def get_price(self):
        return self._Room__price

    def get_features(self):
        return self._features + [self.get_wifi_description(), self.get_breakfast_description()]


class FamilyRoom(Room, WiFiService):
    def __init__(self, features, price):
        Room.__init__(self, features, price)
        WiFiService.__init__(self)

    def get_price(self):
        return self._Room__price

    def get_features(self):
        return self._features + [self.get_wifi_description()]


standard_room = StandardRoom(["tv", "konder", "shkaf"], 100)
luxury_room = LuxuryRoom(["tv", "konder", "2 shkaf", "3 krovat", "bar"], 175)
family_room = FamilyRoom(["tv", "konder", "shkaf", "2 krovat", "kuhnya"], 150)

print("Standard Room:")
print(f"Price: {standard_room.get_price()} $")
print("Features:", ", ".join(standard_room.get_features()))

print("\nLuxury Room:")
print(f"Price: {luxury_room.get_price()} $")
print("Features:", ", ".join(luxury_room.get_features()))

print("\nFamily Room:")
print(f"Price: {family_room.get_price()} $")
print("Features:", ", ".join(family_room.get_features()))
