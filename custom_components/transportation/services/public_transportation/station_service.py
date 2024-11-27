from custom_components.transportation.components.device import TransportationDevice


class Station(TransportationDevice):
    """"""
    def __init__(self, station_id: any):
        super().__init__()
        self._type = "station"
        self._name = "Station"
        self._state = None
        self._attributes = {}
