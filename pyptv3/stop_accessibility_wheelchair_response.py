from pyptv3 import TRAIN, TRAM, BUS, VLINE_TRAIN, NIGHT_BUS

class StopAccessibilityWheelchairResponse:
    def __init__(self, response):
        self._accessible_ramp = response["accessible_ramp"]
        self._accessible_parking = response["accessible_parking"]
        self._accessible_phone = response["accessible_phone"]
        self._accessible_toilet = response["accessible_toilet"]

    @property
    def accessible_ramp(self):
        return self._accessible_ramp

    @property
    def accessible_parking(self):
        return self._accessible_parking

    @property
    def accessible_phone(self):
        return self._accessible_phone

    @property
    def accessible_toilet(self):
        return self._accessible_toilet

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<AccessibilityWheelchair accessible_ramp:%r accessible_parking:%r accessible_phone:%r accessible_toilet:%r>" % (self.accessible_ramp, self.accessible_parking, self.accessible_phone, self.accessible_toilet)
