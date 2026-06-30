import os

LOG_PATH = "logs"

def read_logs(agent_name, lines=20):
    file_path = os.path.join(LOG_PATH, f"{agent_name}.log")

    if not os.path.exists(file_path):
        return []

    with open(file_path, "r", encoding="utf-8") as f:
        data = f.readlines()

    return data[-lines:]