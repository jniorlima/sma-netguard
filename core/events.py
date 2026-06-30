from dataclasses import dataclass
from datetime import datetime

@dataclass
class Event:
    source: str
    host: str
    event: str
    value: float
    severity: str = "INFO"
    timestamp: str = ""

    def __post_init__(self):
        if not self.timestamp:
            self.timestamp = datetime.now().strftime("%H:%M:%S")