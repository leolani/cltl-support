from cltl.log_timeline.api import Event, to_millisec, LogParser


class TopicWorkerLogParser(LogParser):
    def __init__(self, min_delta: int):
        self._min_delta = min_delta

    def is_logline(self, line: str) -> bool:
        return ('cltl.combot.infra.topic_worker' in line
                and any(w in line for w in ['Processing', 'Processed']))

    def parse(self, line: str) -> Event:
        parts = line.split()

        if parts[4] == 'Processing':
            return Event((parts[6], parts[-1]), to_millisec(parts[1]), None, None, None)
        elif parts[4] == 'Processed':
            return Event((parts[6], parts[-1]), None, None, int(parts[8]), None)

    def merge(self, events):
        event = events[0]
        for other in events[1:]:
            if event.key != other.key:
                raise ValueError("Keys not matching: " + event.key + " - " + other.key)

            event.start = event.start if event.start else other.start
            event.delta = event.delta if event.delta else other.delta
            if not event.end and event.start and event.delta:
                event.end = event.start + max(event.delta, self._min_delta)
            event.display = event.display or other.display

        return event