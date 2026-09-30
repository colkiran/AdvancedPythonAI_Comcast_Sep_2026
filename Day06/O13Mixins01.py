class LoggingMixin:

    def log(self, message):
        print(f"[LOG]: {message}")

class Worker(LoggingMixin):

    def do_work(self):
        self.log("Work Started.....")
        print("Doing some work.....")
        self.log("Work finished.....")

w = Worker()
w.do_work()