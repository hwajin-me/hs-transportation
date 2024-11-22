from enum import Enum


class RailwayStatus(Enum):
    DEPARTED = "departed"
    ARRIVED = "arrived"
    DELAYED = "delayed"
    NO_DATA = "no_data"
