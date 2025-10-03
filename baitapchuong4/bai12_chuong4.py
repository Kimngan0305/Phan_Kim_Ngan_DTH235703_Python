def oscillate(start, stop):
    for i in range(start, stop):
        yield i
        if i != 0:
            yield -i
