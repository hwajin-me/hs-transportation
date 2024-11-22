import dataclasses


@dataclasses.dataclass
class AddressData:
    def __init__(
            self,
            country_code: str,
            primary: str,
            secondary: str | None,
            postal_code: str
    ):
        self.country_code = country_code
        self.primary = primary
        self.secondary = secondary
        self.postal_code = postal_code
