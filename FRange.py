class frange (object):
    def __init__(self, start, stop, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step
        self.current = start - step

    def __iter__(self):
        return self

    def __next__(self):
        self.current += self.step
        func = self.current.__gt__

        if self.step < 0:
            func = self.current.__lt__

        # if self.current + self.step > self.stop:
        if func(self.stop):
            raise StopIteration("Done")

        return self.current



if __name__ == "__main__":
    print(list(frange(10, 1, 1)))
    print(list(frange(10, 11, 2)))
    print(list(frange(10, 11, -1)))
    print(list(frange(10, 20, -1)))
    print(list(frange(10, 20, .5)))
    print(list(frange(10, 11, .1)))
    print(list(frange(11, 10, -.1)))

