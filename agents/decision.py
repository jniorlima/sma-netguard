from agents.base_agent import BaseAgent
from core.queues import analysis_queue, decision_queue
from datetime import datetime


class DecisionAgent(BaseAgent):

    def run(self):

        print("[DECISOR] Pronto")

        while True:

            data = analysis_queue.get()

            alerts = data["alerts"]

            if not alerts:
                continue

            severity = "BAIXA"

            if "HOST_OFFLINE" in alerts:
                severity = "ALTA"

            elif "HIGH_TRAFFIC" in alerts:
                severity = "MEDIA"

            elif "HIGH_LATENCY" in alerts:
                severity = "MEDIA"

            log = f"{datetime.now().strftime('%H:%M:%S')} | Severidade={severity} | Alerts={alerts} | Event={data['event']}"

            with open("logs/decision.log", "a", encoding="utf-8") as f:
                f.write(log + "\n")

            decision_queue.put({
                "severity": severity,
                "alerts": alerts,
                "event": data["event"]
            })