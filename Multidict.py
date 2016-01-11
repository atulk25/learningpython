class multidict (dict):
    def __getitem__(self, key):
        if isinstance(key, tuple):
            return tuple([dict.__getitem__(self, k) for k in key])
        else:
            return dict.__getitem__(self, key)



if __name__ == "__main__":
    d = multidict(name="Atul", age=32, height=164, weight=125)
    print(d["name"])
    print(d["age", "height"])