

import time
from datetime import datetime

try:
    while True:
        now = datetime.now()
        print(now.strftime("%I:%M:%S %p") + "  -  " + now.strftime("%A, %B %d, %Y"), end="\r", flush=True)
        # Sleep until the start of the next second
        time.sleep(1 - now.microsecond / 1_000_000.0)
except KeyboardInterrupt:
    print("\nClock stopped.")
