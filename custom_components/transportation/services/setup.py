from custom_components.transportation.consts.country import COUNTRY_KOREA, COUNTRY_NAME_MAP


def country_list():
    return [COUNTRY_KOREA]


def country_name(country: str) -> str | None:
    if country in COUNTRY_NAME_MAP:
        return COUNTRY_NAME_MAP[country]
    return None


def service_list():
    return []
