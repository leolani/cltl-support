import re

from cltl.log_timeline.api import LogParser, Event, to_millisec


class WhisperLogParser(LogParser):
    PATTERN = r'Transcribed audio \(.+ sec\) in (.+)'

    def __init__(self, min_delta: int):
        self._min_delta = min_delta

    def is_logline(self, line: str) -> bool:
        return ('cltl.asr.whisper_asr' in line
                and "Transcribed audio" in line)

    def parse(self, line: str) -> Event:
        result = re.search(self.PATTERN, line)

        if not result:
            raise ValueError("No match in line :" + line)
        duration = max(int(float(result.group(1)) * 1000), self._min_delta)

        parts = line.split()
        end = to_millisec(parts[1])

        return Event((end, "Whisper"), end - duration, end, duration, None)

    def merge(self, events):
        if len(events) != 1:
            raise ValueError(events)

        return events[0]
