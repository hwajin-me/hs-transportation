from enum import Enum

from custom_components.transportation.components.device import TransportationDevice


class StationType(Enum):
    BUS = 'BUS',
    BYCYCLE = 'BYCYCLE',
    RAILWAY = 'RAILWAY',


class StationSearchService:
    """Station Search Service (Abstract)"""


class StationDevice(TransportationDevice):
    """Station Device (Abstract)"""

    def __init__(
            self,
            country_code: str
    ):
        super().__init__()
        self._country_code = country_code
