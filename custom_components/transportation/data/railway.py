from enum import Enum


class RailwayStatus(Enum):
    # 출발
    DEPARTED = "departed"

    # 도착
    ARRIVED = "arrived"

    # 지연
    DELAYED = "delayed"

    # 운행정보 없음
    NO_DATA = "no_data"

    # 결항
    CANCELLED = "cancelled"
