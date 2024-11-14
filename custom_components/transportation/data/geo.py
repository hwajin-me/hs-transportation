import dataclasses


@dataclasses.dataclass
class Point:
    latitude: float
    longitude: float

    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude

    def __iter__(self):
        return iter((self.latitude, self.longitude))

    @staticmethod
    def from_dict(data: dict):
        return Point(data['latitude'], data['longitude'])
