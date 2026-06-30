from threading import Thread

class BaseAgent(Thread):

    def __init__(self):

        super().__init__(daemon=True)

    def run(self):

        raise NotImplementedError