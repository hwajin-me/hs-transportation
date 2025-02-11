from enum import Enum


class BusStatus(Enum):
    # 출발
    DEPARTED = "departed"

    # 도착
    ARRIVED = "arrived"

    # 운행정보 없음
    NO_DATA = "no_data"
