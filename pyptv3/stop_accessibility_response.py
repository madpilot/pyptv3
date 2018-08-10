import pyptv3

class StopAccessibilityResponse:
    def __init__(self, response):
        self._lighting = response["lighting"]
        self._stairs = response["stairs"]
        self._escalator = response["escalator"]
        self._lifts = response["lifts"]
        self._hearing_loop = response["hearing_loop"]
        self._tactile_tiles = response["tactile_tiles"]
        self._wheelchair = None
        if response["wheelchair"] is not None:
            self._wheelchair = pyptv3.StopAccessibilityWheelchairResponse(response["wheelchair"])

    @property
    def lighting(self):
        return self._lighting

    @property
    def stairs(self):
        return self._stairs

    @property
    def escalator(self):
        return self._escalator

    @property
    def hearing_loop(self):
        return self._hearing_loop

    @property
    def tactile_tiles(self):
        return self._tactile_tiles

    @property
    def wheelchair(self):
        return self._wheelchair


    @property
    def lifts(self):
        return self._lifts

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Accessibility lighting:%r stairs:%r escalator:%r lifts:%r hearing_loop:%r wheelchair:%r>" %(self.lighting, self.stairs, self.escalator, self.lifts, self.hearing_loop, self.wheelchair)
