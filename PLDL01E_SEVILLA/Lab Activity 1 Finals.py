#Laboratory Activity 1 Finals
from datetime import datetime

# Part A: Singleton Pattern
# Create Class named Logger
class Logger:
    _instance = None
    _log = []
# Create Methods
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def log(self, message):
        timestamp = datetime.now().strftime("%Y/%m/%d %H-%M-%S")
        self._log.append(f"[{timestamp}] {message}")

    def show_log(self):
        return self._log

# Demo
logger1 = Logger()
logger2 = Logger()

logger1.log("First Log Entry")
logger2.log("Second Log Entry")
# Display Logger timestamps
print(logger1.show_log())
print(f"Logger 1 is Logger 2: {logger1 is logger2}")