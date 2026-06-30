from agents.collector import CollectorAgent
from agents.analyzer import AnalyzerAgent
from agents.decision import DecisionAgent
from agents.notifier import NotifierAgent

print("=" * 50)
print("SMA NETGUARD")
print("=" * 50)

collector = CollectorAgent()
analyzer = AnalyzerAgent()
decision = DecisionAgent()
notifier = NotifierAgent()

collector.start()
analyzer.start()
decision.start()
notifier.start()

# 🔥 mantém o programa vivo corretamente
try:
    while True:
        pass
except KeyboardInterrupt:
    print("\n[SISTEMA] Encerrando SMA NetGuard...")