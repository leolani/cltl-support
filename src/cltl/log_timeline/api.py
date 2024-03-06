import abc
import dataclasses
from datetime import datetime
from typing import Any, Optional


@dataclasses.dataclass
class Event:
    key: Any
    start: Optional[int]
    end: Optional[int]
    delta: Optional[int]
    display: Optional[str]


class LogParser(abc.ABC):
    def is_logline(self, line: str) -> bool:
        raise NotImplementedError

    def parse(self, line: str) -> Event:
        raise NotImplementedError

    def merge(self, events):
        raise NotImplementedError


def to_millisec(time_str: str):
    parts = [int(p) for p in time_str.split(':')]
    return 1000 * (parts[0] * 3600 + parts[1] * 60 + parts[2])


def to_datetime(timestamp_ms):
    return datetime.fromtimestamp(timestamp_ms / 1000)

