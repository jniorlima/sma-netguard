import os
from datetime import datetime

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)


def write_log(file_name, message):
    timestamp = datetime.now().strftime("%H:%M:%S")
    path = os.path.join(LOG_DIR, file_name)

    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{timestamp} | {message}\n")