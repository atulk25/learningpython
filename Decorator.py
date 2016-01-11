def logit(f):
    def wrapper(*args, **kwargs):
        print(f.__name__, "was called with args", args, kwargs)
        return f(*args, **kwargs)
    return wrapper

@logit
def add(n1, n2):
    return n1 + n2
# add = logit(add)

@logit
def mul(n1, n2):
    return n1 * n2


if __name__ == "__main__":
    print(add(1,2))
    print(mul(3,4))