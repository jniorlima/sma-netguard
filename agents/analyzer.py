# agents/analyzer.py

import time
import config
from agents.base_agent import BaseAgent
from services.log_writer import write_log


class AnalyzerAgent(BaseAgent):

    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):

        write_log("analyzer", "[ANALISADOR] Iniciado")

        while True:

            try:
                event = self.queue.get()

                latency = event.get("latency")
                traffic = event.get("traffic")

                alerts = []

                # OFFLINE
                if latency is None or latency == 0:
                    alerts.append("HOST_OFFLINE")

                else:
                    # LATENCY LEVELS
                    if latency >= config.PING_CRITICAL:
                        alerts.append("HIGH_LATENCY")
                    elif latency >= config.PING_WARNING:
                        alerts.append("MEDIUM_LATENCY")

                # TRAFFIC LEVELS
                if traffic >= config.TRAFFIC_CRITICAL:
                    alerts.append("HIGH_TRAFFIC")
                elif traffic >= config.TRAFFIC_WARNING:
                    alerts.append("MEDIUM_TRAFFIC")

                log = f"Alertas={alerts} | Latency={latency} | Traffic={traffic}"

                write_log("analyzer", log)

                # envia pro próximo estágio
                self.queue.put({
                    "source": "analyzer",
                    "alerts": alerts,
                    "latency": latency,
                    "traffic": traffic,
                    "event": event
                })

                time.sleep(1)

            except Exception as e:
                write_log("analyzer", f"[ERRO] {str(e)}")