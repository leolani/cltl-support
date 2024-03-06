import argparse
from itertools import groupby

import pandas as pd
import plotly.express as px

from cltl.log_timeline.api import to_datetime
from cltl.log_timeline.mic_parser import MicLogParser
from cltl.log_timeline.topicworker_parser import TopicWorkerLogParser
from cltl.log_timeline.vad_parser import VadLogParser
from cltl.log_timeline.whisper_parser import WhisperLogParser


def parse_log(parser, log_file):
    with open(log_file) as file:
        parsed = (parser.parse(line) for line in file if parser.is_logline(line))
        parsed = sorted(parsed, key=lambda e: e.key)

    events = dict()
    for k, g in groupby(parsed, lambda e: e.key):
        event = parser.merge(list(g))
        if not event.start or not event.end:
            continue

        events[k] = {'event': event.key[0], 'service': event.key[1],
                     'start': to_datetime(event.start),
                     'end': to_datetime(event.end)}

    return events


def plot_events(events):
    event_df = pd.DataFrame(list(v for k, v in events.items() if (not services) or (k[1] in services)))
    fig = px.timeline(event_df, x_start="start", x_end="end", y="service", color="event")
    fig.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Analyse event timeline from logfile')
    parser.add_argument('--log', type=str, default='leolani.log',
                        help="Logfile to analyse")
    parser.add_argument('--service', type=str, required=False, nargs='+',
                        help="Services to include")
    parser.add_argument('--dt', type=int, required=False, default=1000,
                        help="Services to include")
    args, _ = parser.parse_known_args()

    services = set(args.service) if args.service is not None else {}
    # services = {'AsrService',
    #             # 'BDIService',
    #             # 'BackendService_scenario',
    #             'BackendService_tts',
    #             # 'ChatUiService',
    #             # 'ContextService',
    #             # 'EmissorDataService',
    #             # 'SpotDialogService',
    #             # 'SpotGameService',
    #             'VadService',
    #             'Whisper',
    #             'VAD',
    #             'MIC_MUTE',
    #             }

    # TODO move dt to plot_events
    parsers = [TopicWorkerLogParser(args.dt), WhisperLogParser(args.dt), VadLogParser(), MicLogParser()]
    events = {k: v for parser in parsers for k, v in parse_log(parser, args.log).items()}
    plot_events(events)
