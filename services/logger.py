from pathlib import Path

LOG = Path("logs/events.log")

LOG.parent.mkdir(exist_ok=True)


def save(text):

    with open(LOG, "a", encoding="utf8") as f:

        f.write(text + "\n")