from time import clock


class Timer:
    def __init__(self):
        self.start_time = 0

    def start(self):
        self.start_time = clock()

    def stop(self):
        runtime = clock() - self.start_time
        self.start_time = 0
        return runtime

    def time(self, f, arg):
        self.start()
        f(*arg)
        return self.stop()
