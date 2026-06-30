from agents.base_agent import BaseAgent
from core.queues import decision_queue
from datetime import datetime


class NotifierAgent(BaseAgent):

    def run(self):

        print("[NOTIFICADOR] Online")

        while True:

            data = decision_queue.get()

            log = f"{datetime.now().strftime('%H:%M:%S')} | ALERTA | Severidade={data['severity']} | Alerts={data['alerts']} | Event={data['event']}"

            with open("logs/notifier.log", "a", encoding="utf-8") as f:
                f.write(log + "\n")