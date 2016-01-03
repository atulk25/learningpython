def min_or_max(*args, compute_min=False):
    if compute_min:
        return min(args)
    else:
        return max(args)


if __name__ == "__main__":
    print(min_or_max(1,2,3,4))
    print(min_or_max(1))
    print(min_or_max(1,2,3,4, compute_min=True))