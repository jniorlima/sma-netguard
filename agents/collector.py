import time
from datetime import datetime

from agents.base_agent import BaseAgent
from core.monitor import NetworkMonitor
from core.events import Event
from core.queues import collector_queue
import config


class CollectorAgent(BaseAgent):

    def __init__(self):
        super().__init__()
        self.monitor = NetworkMonitor()
        usage = self.monitor.get_network_usage()
        self.last_packets = usage["packets_recv"]

    def run(self):

        print("[COLETOR] Monitorando rede...")

        while True:

            latency = self.monitor.get_ping(config.HOSTS["escritorio"])
            usage = self.monitor.get_network_usage()

            current = usage["packets_recv"]
            delta = current - self.last_packets
            self.last_packets = current

            event = Event(
                source="collector",
                host=config.HOSTS["escritorio"],
                event="NETWORK",
                value=delta
            )

            collector_queue.put({
                "event": event,
                "latency": latency,
                "traffic": delta
            })

            log = f"{datetime.now().strftime('%H:%M:%S')} | Ping={latency} | Tráfego={delta}"

            with open("logs/collector.log", "a", encoding="utf-8") as f:
                f.write(log + "\n")

            time.sleep(config.PING_INTERVAL)