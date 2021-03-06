from inferno.lib.rule import chunk_json_stream
from inferno.lib.rule import InfernoRule
from inferno.lib.rule import Keyset
from infernyx.rules import combiner
from config_infernyx import *

AUTO_RUN = False


def count(parts, params):
    parts['count'] = 1
    yield parts


RULES = [

    InfernoRule(
        name='count_fetches',
        source_tags=['incoming:app'],
        day_range=1,
        map_input_stream=chunk_json_stream,
        parts_preprocess=[count],
        geoip_file=GEOIP,
        combiner_function=combiner,
        keysets={
            'stats': Keyset(
                key_parts=['date', 'ver', 'locale', 'action'],
                value_parts=['count'],
            ),
        },
    ),
]
