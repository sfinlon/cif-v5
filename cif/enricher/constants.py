import os
from cifsdk.constants import RUNTIME_PATH

ENRICHER_ADDR = os.path.join(RUNTIME_PATH, 'enricher.ipc')
ENRICHER_ADDR = f"ipc://{ENRICHER_ADDR}"
ENRICHER_ADDR = os.getenv('CIF_ENRICHER_ADDR', ENRICHER_ADDR)

ENRICHER_SINK_ADDR = os.path.join(RUNTIME_PATH, 'enricher_sink.ipc')
ENRICHER_SINK_ADDR = f"ipc://{ENRICHER_SINK_ADDR}"
ENRICHER_SINK_ADDR = os.getenv('CIF_ENRICHER_SINK_ADDR', ENRICHER_SINK_ADDR)

SNDTIMEO = 5000
RCVTIMEO = 5000

ZMQ_HWM = os.getenv('ENRICHER_ZMQ_HWM', '10000')
ZMQ_HWM = int(ZMQ_HWM)

TRACE = False
if os.environ.get('CIF_ENRICHER_TRACE', '') == '1':
    TRACE = True

MIN_CONFIDENCE = os.getenv('CIF_ENRICHER_MIN_CONFIDENCE', 1.0)

THREADS = os.getenv('CIF_ENRICHMENT_THREADS', 1)

PLUGINS_NAMESPACE = 'csirtg_enrichment_'

LOGLEVEL = os.getenv('CIF_LOGLEVEL', 'ERROR')
