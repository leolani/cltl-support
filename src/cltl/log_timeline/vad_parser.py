from cltl.log_timeline.api import Event, to_millisec, LogParser


class VadLogParser(LogParser):
    START = 'Started VAD with window '
    START_VA = 'Detected start of VA'
    END = 'Detected end of VA at'
    END_TOT = 'Detected VA of length'

    def __init__(self, start_pattern: str = START_VA, end_pattern: str = END_TOT):
        self._start = start_pattern
        self._end = end_pattern
        self._count = 0

    def is_logline(self, line: str) -> bool:
        return ('cltl.vad.frame_vad' in line
                and any(w in line for w in [self._start, self._end]))

    def parse(self, line: str) -> Event:
        parts = line.split()
        timestamp = to_millisec(parts[1])

        start, end = None, None
        if self._start in line:
            self._count += 1
            start = timestamp
        elif self._end in line:
            end = timestamp
        else:
            raise ValueError(line)

        return Event((self._count, "VAD"), start, end, None, None)

    def merge(self, events):
        event = events[0]
        for other in events[1:]:
            if event.key != other.key:
                raise ValueError("Keys not matching: " + event.key + " - " + other.key)

            event.start = event.start if event.start else other.start
            event.end = event.end if event.end else other.end

        return event