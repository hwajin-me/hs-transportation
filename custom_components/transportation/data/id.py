import dataclasses


@dataclasses.dataclass
class StationId:
    """Data class for station id."""

    def __init__(
            self,
            country_code: str
    ):
        self._country_code = country_code
